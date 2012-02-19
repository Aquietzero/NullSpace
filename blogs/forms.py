from django import forms
from NullSpace.blogs.models import *

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length=50)
    website = forms.URLField(required=False)
    email   = forms.EmailField(required=False)
    content = forms.CharField(widget=forms.Textarea)

    def clean_visitor(self):
        visitor = self.cleaned_data['visitor']
        # use re to examine visitor.
        # if something wrong:
        #     raise forms.ValidationError('error')

        if len(visitor) == 0:
            raise form.ValidateError("Please at least leave a name")

        return visitor
