from django import forms

from .models import Pizza, Topping#, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Topping
        #model = Comment
        fields = ['name']
        #fields = ['text']
        labels = {'name':''}
        #labels = {'name':'Comment:'}

        widgets = {'name': forms.Textarea(attrs={'cols': 80})}

        