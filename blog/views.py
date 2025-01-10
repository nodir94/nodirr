from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Barcha postlarni olish
    return render(request, 'blog/post_list.html', {'posts': posts})  # To'g'ri shablon nomi

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})  # To'g'ri shablon nomi
