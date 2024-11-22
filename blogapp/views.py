from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  ListView , CreateView ,UpdateView ,DeleteView

from blogapp.models import BlogPost
# Create your views here.
class BlogView(ListView) : 
    model = BlogPost 
    context_object_name ='posts'
    template_name = 'blogview.html'  


class blogcreate (CreateView) : 
    model = BlogPost
    fields = ['title','content','author','created_on']
    template_name ='blogcreate.html'
    success_url =reverse_lazy('blogapp:listhtml') 

class blogdelete (DeleteView) :
    model =BlogPost
    pk_url_kwarg ='pk'
    template_name = 'blogdelete.html'
    success_url = reverse_lazy('blogapp:listhtml')
