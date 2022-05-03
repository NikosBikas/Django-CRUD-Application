from django import forms
from .models import Trainer

class TrainerForm(forms.ModelForm):
    
    class Meta:
        model = Trainer
        fields = ('first_name', 'last_name', 'course', 'subject')

    def __init__(self, *args, **kwargs):
        super(TrainerForm,self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = "Select"
        self.fields['subject'].empty_label = "Select"