from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'role', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make role field required
        self.fields['role'].required = True
        
        # Add CSS classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
        # Customize password help text
        self.fields['password1'].help_text = "Your password must contain at least 8 characters."
        self.fields['password2'].help_text = "Enter the same password as before, for verification."

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})