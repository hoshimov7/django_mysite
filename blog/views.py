from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = "blog/post/list.html"


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts':posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__day=day,
        publish__month=month
        )

    return render(request, 'blog/post/detail.html', {'post':post})



def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED    
    )
    send = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        
        if form.is_valid():

            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = (
                f'{cd['name']}  recommentds you read \n'
                f'{post.title}'
            )
            message = (
                f"Read {post.title} at {post_url}\n\n "
                f"{cd['name']}\'s comments: {cd['comment']}"
            )
            send_mail(
                subject,
                message,
                'shirinmohim8@gmail.com',
                [cd['to']]
            )
            send = True
    else:
        form = EmailPostForm()
    
    return render(
        request,
        'blog/post/share.html',
        {
            'post':post,
            'form':form,
            'send':send,
        }
    )