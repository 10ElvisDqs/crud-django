# title = models.CharField(max_length=200)
# description = models.TextField(blank=True)
# completed = models.BooleanField(default=False)
# created = models.DateTimeField(auto_now_add=True)
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description']
        # fields = '__all__'

