from ..api.models import Brand, Product, User
from django import forms

class CreateBrandForm(forms.Form):
    brand = forms.CharField(max_length=100)

class UpdateBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs.update({'class': 'custom-class'})

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'price', 'brand']

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']