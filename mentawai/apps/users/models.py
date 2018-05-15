from datetime import timedelta

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)

from django.db import models
from django.utils import timezone

from mentawai.apps.payment_histories.models import PaymentHistory
from mentawai.core.validators import validate_mobile_phone

from model_utils import Choices


class CustomUserManager(UserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        now = timezone.now()
        user = self.model(email=email, is_active=True, is_tourist=True,
                          last_login=now, is_superuser=False,
                          date_joined=now, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_tourist = False
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    email and password are required.
    """
    # Name, email and mobile needs to be case insensitive indexed in postgres
    email = models.EmailField(unique=True, null=True,
                              max_length=254, db_index=True)
    name = models.CharField('Nama', max_length=255, blank=True)
    nationaly = models.CharField('Kebangsaan', max_length=255, blank=True)
    pasport_number = models.CharField('Nomor Paspor', max_length=255, blank=True)
    GENDER = Choices(
        (1, 'male', 'Male'),
        (2, 'female', 'Female'),
    )
    gender = models.PositiveSmallIntegerField('Jenis Kelamin', choices=GENDER, blank=True, null=True)
    mobile_number = models.CharField('Nomor Ponsel', max_length=30, unique=True,
                                     null=True, db_index=True, blank=True,
                                     validators=[validate_mobile_phone])
    push_notification_key = models.CharField(blank=True, default='', max_length=254)
    is_tourist = models.BooleanField('Turis', default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField('Status aktif', default=True)
    date_joined = models.DateTimeField('Tanggal Terdaftar', default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.name or self.email or 'User #%d' % (self.id)

    def get_short_name(self):
        return self.email

    def get_payment_active(self):
        payments = self.payment_histories.filter(status=PaymentHistory.STATUS.completed).order_by('-id')
        for payment in payments:
            max_date = (payment.created + timedelta(days=payment.number_of_visits))\
                .replace(hour=0, minute=0, second=0, microsecond=0)
            now = timezone.localtime(timezone.now())

            if now <= max_date:
                return payment
                break

        return None


def cached_auth_preprocessor(user, request):
    if not user.is_authenticated():
        return user
    return user
