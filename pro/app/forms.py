from django import forms
from .models import Bank


class Bankform(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['id','acc_no','acc_holder','acc_balance']
        widgets = {
            'acc_no': forms.TextInput(attrs={'class':'form-control'}),
            'acc_holder': forms.TextInput(attrs={'class':'form-control'}),
            'acc_balance': forms.TextInput(attrs={'class':'form-control'}),
        }
        

class DepositForm(forms.Form):
    Account_no = forms.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = forms.DecimalField(max_digits=10, decimal_places=2)
