from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_PER_PAGE = 10


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    template = 'posts/group_list.html'
    posts = group.posts.all().order_by('-pub_date')[:POSTS_PER_PAGE]
    return render(
        request,
        template,
        {'title': title, 'group': group, 'posts': posts, }
    )


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    # posts = Post.objects.order_by('-pub_date')[:POSTS_PER_PAGE]
    return render(
        request,
        template,
        context
    )
