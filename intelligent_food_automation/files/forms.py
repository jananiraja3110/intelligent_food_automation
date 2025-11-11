from django import forms
from .models import EncryptedFile, FileTransfer

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = EncryptedFile
        fields = ['file_type']
    
    file = forms.FileField(
        label='Select File',
        help_text='Supported formats: Excel, CSV, TXT, JSON'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class FileTransferForm(forms.ModelForm):
    class Meta:
        model = FileTransfer
        fields = ['to_team', 'message']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'rows': 3})