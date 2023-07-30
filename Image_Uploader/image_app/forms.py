from django import forms
from .models import ImageUploader


class ImageUploaderForm(forms.ModelForm):
    class Meta:
        model=ImageUploader
        fields = '__all__'
        labels = {'image':""}
