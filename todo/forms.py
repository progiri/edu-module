from django import forms

from .models import STATUS_CHOICES, ToDo


class ToDoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        required=False
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = ToDo
        fields = ('title', 'status')
