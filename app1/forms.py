from django import forms
from app1.models import StockerRegister,Dispatcher_Register,Product_Details

class Stocker_Register_forms(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput,min_length=5)
    class Meta:
        model = StockerRegister
        fields = "__all__"



class Dispatcher_Register_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,min_length=5)
    class Meta:
        model = Dispatcher_Register
        fields = '__all__'

class Product_Details_Form(forms.ModelForm):
    class Meta:
        model = Product_Details
        fields = "__all__"