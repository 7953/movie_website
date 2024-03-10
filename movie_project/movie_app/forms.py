from django import forms
from .models import products,Comment,Rating
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['name', 'poster', 'description', 'release_date', 'actors', 'category_id', 'trailer_link']
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
