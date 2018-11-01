from django import forms

from .models import Post, Comment, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'name', 'good_points', 'improving_points', 'another_points',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'name',)

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('user_id', 'user_pw', 'user_name', 'user_nickname', 'user_email',)