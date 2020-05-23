from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import ImageUploadForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Post
from .forms import IngredientsFormset

from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('author')
    serializer_class = PostSerializer



#this added for dynamic
def create_ingredient_normal(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = IngredientsFormset(request.GET or None)
    elif request.method == 'POST':
        formset = IngredientsFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                if name:
                    Ingredients(name=name).save()
            return redirect('recipes')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


def home(request):
    model = Post
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'recipes/home.html', context)


def search_post(request):
    query = request.GET.get('q')
    if query:
            results = Post.objects.filter(Q(title__icontains=query))
    else:
        results = Post.objects.all()
    context = {
        'posts': results
    }
    return render(request, "recipes/home.html", context)







def favorite_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.favorite.filter(pk=request.user.pk).exists():
        print("hello")
        is_favorite = True
        post.favorite.remove(request.user)
    else:
        is_favorite = False
        post.favorite.add(request.user)
        print("hi")
    return HttpResponseRedirect(post.get_absolute_url()) # this is the fk up


def recipesfavorites(request):
    user = request.user
    favorite_post = user.favorite.all()
    context = {
        'favorite_post': favorite_post,
        'is_favorite': is_favorite,
    }
    return render(request, 'recipesfavorites.html', context)

#def fav(request):
    #model = favorite
















class PostDetailView(DetailView):
    model = Post
    #do the same thing with search the whole query = but with model.


class PostListView(ListView):
    model = Post
    template_name = 'recipes/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class UserPostListView(ListView):
    model = Post
    template_name = 'recipes/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','description', 'Ingredients', 'Steps', 'Additional', 'Diet', 'recipe_image']

    def form_valid( self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def model_form_upload(self):
        if request.method == 'POST':
            i_form = ImageUploadForm(self.request.POST, self.request.FILES)
            if i_form.is_valid():
                i_form = Post(recipe_image=self.request.FILES['recipe_image'])
                i_form.save()
            return redirect('recipe/')
        else:
            i_form = ImageUploadForm()
        return render(self.request, 'recipe/post.html', { 'i_form': i_form })
        print(self.request)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ImageUploadForm):
    model = Post
    fields = ['title','description', 'Ingredients', 'Steps', 'Additional', 'Diet', 'recipe_image' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def model_form_upload(self):
        if request.method == 'POST':
            i_form = ImageUploadForm(self.request.POST, self.request.FILES)
            if i_form.is_valid():
                i_form.save()
            return redirect('recipe')
        else:
            i_form = ImageUploadForm()
            return render(request, 'recipe/post.html', { 'form': i_form })


    def test_func(self):
        print("hit3")
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/recipes'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'recipes/about.html')

def blog(request):
    return render(request, 'recipes/blog.html')


