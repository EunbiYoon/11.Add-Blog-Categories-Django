from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date'] 
    #ordering=['-id']

    def get_context_data(self, *args, **kwargs):
        #name is only thing -> all = name
        cat_menu=Category.objects.all()
        context=super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request,category_detail):
    category_posts=Post.objects.filter(category=category_detail.replace('-',' '))
    return render(request, 'categories.html', {'category_detail':category_detail.title().replace('-',' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'


class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'

class AddCategoryView(CreateView):
    model=Category
    template_name='add_category.html'
    fields="__all__"



class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'


class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
