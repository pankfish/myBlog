from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author
from .forms import PostForm
from django.http import Http404
# Create your views here.

def create_post_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    print(request.user)
    print(Author.objects.get(username=request.user.get_username()))
    form.author_id = request.user.id
    if form.is_valid():
        title = form.cleaned_data['title']
        topic = form.cleaned_data['topic']
        content = form.cleaned_data['content']
        author = request.user
        blog_post = Post(title=title, topic=topic, content=content, author=author)
        #form = PostForm()
        form.author_id = request.user.id
        print(blog_post.content)
        blog_post.save()
        print(f'user_id = {request.user.id}')

    context = {
        'form': form
    }
    return render(request, "blog/create_post.html", context)
def blog_post_view(request):
    obj = Post.objects.get(id=1)
    context = {
        'obj': obj
    }
    return render(request, "blog/post.html", context)

def dynamic_lookup_view(request, id):
    try:
        obj = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    context = {'object': obj}
    return render(request, "blog/post.html", context)

def post_delete_view(request, id):
    obj = get_object_or_404(Post, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../..')
    context = {
        "object": obj
    }
    return render(request, "blog/post_delete.html", context)

def post_list_view(request):
    queryset = Post.objects.all()
    context = {
        'object': queryset
    }

    return render(request, "blog/post_list.html", context)

