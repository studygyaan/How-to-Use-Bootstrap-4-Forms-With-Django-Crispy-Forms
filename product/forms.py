from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post
        self.helper.add_input(Submit('submit', 'Save Product'))