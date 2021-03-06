from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Full Name',
        'autocmplete': 'name'}),
        required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'autocomplete': 'email'}),
        required=True)
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number',
        'autocomplete': 'number'}),
        required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'cols': '40',
        'rows': '10'}),
        required=True)
