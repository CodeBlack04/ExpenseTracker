from django import forms

from .models import Transaction

input_classes = 'w-full py-4 px-6 rounded-xl bg-teal-100 text-black'

class NewTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'notes', 'category', 'new_category', 'amount')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name of your transaction',
                'class': input_classes,
            }),

            'notes': forms.TextInput(attrs={
                'placeholder': 'Add a simple note',
                'class': input_classes,
            }),

            'category': forms.Select(attrs={
                'placeholder': 'Choose a category',
                'class': input_classes,
            }),

            'new_category': forms.TextInput(attrs={
                'placeholder': 'Enter a new category',
                'class': input_classes,
            }),

            'amount': forms.TextInput(attrs={
                'placeholder': 'Enter amount',
                'class': input_classes,
            }),
        }