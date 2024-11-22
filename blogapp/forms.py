from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'created_on']  # Include the created_on field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the content here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}),
            'created_on': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  # Enables the HTML5 calendar widget
            }),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Content',
            'author': 'Author',
            'created_on': 'Created On',
        }
