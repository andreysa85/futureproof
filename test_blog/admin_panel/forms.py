from django import forms
from blog.models import Post


class AddPostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_name', 'post', 'author', 'time_creation', 'time_publication', 'image')


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_name', 'post', 'author', 'time_creation', 'time_publication',
                  'time_update', 'image', )
