from django import forms
from bank.models import Customer, Transaction

class CustomerForm(forms.ModelForm):

    class Meta():
        model = Customer
        fields = ('name','account_number','balance','phone_number')
        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : "form-control",
                'placeholder' : 'Name',
                'style' : 'max-width: 300px',
            }),
            'account_number' : forms.NumberInput(attrs = {
                'class' : "form-control",
                'placeholder' : 'Account Number',
                'style' : 'max-width: 300px',
            }),
            'balance' : forms.NumberInput(attrs = {
                'class' : "form-control",
                'placeholder' : 'Balance',
                'style' : 'max-width: 300px',
            }),
            'phone_number' : forms.TextInput(attrs = {
                'class' : "form-control",
                'placeholder' : 'Phone Number',
                'style' : 'max-width: 300px',
            })

        }

class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transaction
        fields = ('sender_name','receiver_name','amount','date')
