from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Detail,Project,Comment

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date','user', 'detail', 'votes']

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        exclude = ['user']     

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'comment' ]