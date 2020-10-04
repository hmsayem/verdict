from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


# Create your views hereW.

def HomeView(request):
    object_list = Post.objects.all()
    cats = Category.objects.all()
    return render(request, 'blog/home.html', {'object_list': object_list, 'cats': cats})


def CategoryView(request, cat):
    category_post = Post.objects.filter(category=cat)
    cats = Category.objects.all()
    context = {
        'cat': cat,
        'cats': cats,
        'category_post': category_post
    }
    return render(request, 'blog/category.html', context)


def DetailView(request, pk):
    post = get_object_or_404(Post, id=pk)
    likes_count = post.total_likes()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    cats = Category.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()
            return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'cats': cats,
        'likes_count': likes_count,
        'is_liked': is_liked,
        'comment_form': comment_form,
    }
    return render(request, 'blog/detail.html', context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
