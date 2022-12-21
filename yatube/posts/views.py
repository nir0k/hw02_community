from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User

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


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.author_posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    fullname = author.first_name + ' ' + author.last_name
    title = f'Профайл пользователя {fullname}'
    context = {
        'title': title,
        'fullname': fullname,
        'page_obj': page_obj,
        'posts_count': post_list.count(),
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, id=post_id)
    posts_count = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'posts_count': posts_count,
    }
    return render(request, 'posts/post_detail.html', context)
