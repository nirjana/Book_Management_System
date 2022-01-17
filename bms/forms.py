from django import forms
from socket import fromshare


from .models import Image

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  labels = {'photo':''}

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=200,label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Enter book title','id':'title'}))
    author=forms.CharField(label='Author',max_length=200,label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Author name','id':'author'}))
    price=forms.CharField(label='Price',label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Book Price','id':'price'}))
    publisher=forms.CharField(label='Publisher',max_length=200,label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Book publisher','id':'publisher'}))
 

class SearchForm(forms.Form):
    title=forms.CharField(label="Title",max_length=200)
