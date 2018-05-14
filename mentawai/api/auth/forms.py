from django import forms

from mentawai.apps.users.models import User
from mentawai.core.fields import MobileNumberField


class RegistrationForm(forms.Form):
    password = forms.CharField(max_length=255)
    email = forms.EmailField()
    name = forms.CharField(max_length=30)
    nationaly = forms.CharField(max_length=50)
    pasport_number = forms.CharField(max_length=30)
    mobile_number = MobileNumberField()
    gender = forms.ChoiceField(choices=User.GENDER)
    push_notification_key = forms.CharField(max_length=254, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email already exists")
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        if User.objects.filter(mobile_number=mobile_number).exists():
            raise forms.ValidationError("User with this mobile number already exists")
        return mobile_number

    def clean_name(self):
        return self.cleaned_data['name'].title()

    def clean_nationaly(self):
        return self.cleaned_data['nationaly'].title()

    def save(self, *args, **kwargs):
        user = User.objects.create(
            email=self.cleaned_data['email'],
            name=self.cleaned_data['name'],
            mobile_number=self.cleaned_data['mobile_number'],
            gender=self.cleaned_data['gender'],
            push_notification_key=self.cleaned_data['push_notification_key'],
            nationaly=self.cleaned_data['nationaly'],
            pasport_number=self.cleaned_data['pasport_number'],
        )

        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
