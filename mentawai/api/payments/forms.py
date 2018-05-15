from django import forms

from mentawai.apps.payment_histories.models import PaymentHistory


class PaymentForm(forms.Form):
    amount = forms.FloatField()
    number_of_visits = forms.IntegerField()
    payment_id = forms.CharField()

    def save(self, user):
        payment = user.payment_histories.create(
            value=self.cleaned_data['amount'],
            payment_id=self.cleaned_data['payment_id'],
            number_of_visits=self.cleaned_data['number_of_visits'],
            status=PaymentHistory.STATUS.new
        )

        return payment
