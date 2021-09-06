from django import forms

from .models import STATUS_CHOICES, ToDo


class ToDoForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = ToDo
        fields = ('title', 'status')
