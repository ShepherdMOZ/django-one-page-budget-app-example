from django import forms
from .models import Transaction

class NewTransactionForm(forms.ModelForm):

    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Transaction
        fields = '__all__'