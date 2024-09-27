from django import forms
from myApp.models import Model

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['rental_space', 'file_path', 'uploaded_by']
