from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import  TextInput, PasswordInput


from .models import CustomUser

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Name'})
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Password'})
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Login'))
        self.helper.form_tag = False
    
    class Meta:
        model = CustomUser
        fields = ("username","password")
       
class CustomUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ""
        del self.fields['password2']
        
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Name'})
        self.fields['email'].widget = TextInput(attrs={'placeholder': 'Email'})
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password'})
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Signup'))
        self.helper.form_tag = False
       

    class Meta:
        model = CustomUser
        fields = ("username","email","password1")
        