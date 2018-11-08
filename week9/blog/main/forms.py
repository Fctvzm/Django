from django import forms
from .models import Post, Comment
import datetime

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'main_text']
		widgets = { 
            'main_text': forms.Textarea(attrs={'placeholder': u'Post Content'}),
        } 

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'rating']
		widgets = { 
            'content': forms.Textarea(attrs={'placeholder': u'Comment Content'}),
        } 