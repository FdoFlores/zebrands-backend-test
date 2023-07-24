from ..api.models import Brand, Product, User, Buyout
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

class BuyoutForm(forms.ModelForm):
    class Meta:
        model = Buyout
        fields = ['product', 'user', 'buyout_price']
        widgets = {
            'user': forms.HiddenInput(),
            'buyout_price': forms.HiddenInput()
        }
    def __init__(self, user, *args, **kwargs):
        super(BuyoutForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['buyout_price'].initial = 0
        self.fields['user'].widget.attrs['readonly'] = True

    def save(self):
        product = self.cleaned_data.get('product')
        if product:
            self.instance.buyout_price = product.price

        return super(BuyoutForm, self).save(commit=True)