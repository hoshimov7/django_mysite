from django import forms
from .models import Comment

<<<<<<< HEAD
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

=======
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
<<<<<<< HEAD
    to = forms.EmailField()
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
=======
    to =  forms.EmailField()
    contents = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model =  Comment
        fields = ['name', 'email', 'body']
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df

