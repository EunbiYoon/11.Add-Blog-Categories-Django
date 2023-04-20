from django import forms
from .models import Post, Category

cats=Category.objects.all().values_list('name','name')
choice_list=[]
for item in cats:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag', 'author', 'category','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is title_tag'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'This is body'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag', 'body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is title_tag'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'This is body'}),
        }