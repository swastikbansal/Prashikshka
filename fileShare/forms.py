from django import forms
from .models import FileModel

class UploadFileForm(forms.ModelForm):    
    # title = forms.CharField( label="Title", max_length=50 )
    # file = forms.FileField()
    
    class Meta:
        model = FileModel  # Specify the model associated with this form
        fields = ['title', 'file']  # Specify which fields should be included in the form