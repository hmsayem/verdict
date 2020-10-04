from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
catagories = []
for item in choices:
    catagories.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'category', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': "", 'id': 'author', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a comment', 'rows': '3'}),
        }
        labels = {
            'body': '',
        }
