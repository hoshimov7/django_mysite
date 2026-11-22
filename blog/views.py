from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = "blog/post/list.html"
=======
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


class PostListViev(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df


def post_list(request):
    post_list = Post.published.all()
<<<<<<< HEAD
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
=======
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
<<<<<<< HEAD
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

    comment = post.comments.filter(active=True)
    form = CommentForm()
    
    return render(request, 'blog/post/detail.html', {'post':post, 'comments':comment, 'form':form})
=======
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'posts':posts})



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                              slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             status=Post.Status.PUBLISHED)
    comment = post.comments.filter(active=True)
    
    return render(request,
                  'blog/post/detail.html', 
                  {'post':post})



>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df


def post_share(request, post_id):

<<<<<<< HEAD
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
                f'{cd['name']}  recommentds you read '
                f'{post.title}'
            )
            message = (
                f"Read {post.title} at {post_url}\n\n "
                f"{cd['name']}\'s comments: {cd['comment']}"
            )
            from django.conf import settings
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
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



@require_POST

def post_comment(request, post_id):
    post = get_object_or_404(
        Post, 
        id=post_id,
        status=Post.Status.PUBLISHED
    )
=======
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    send = False

    
    if request.method == "POST":
        form  = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url)
            subject = (f'{cd['name']} recomends you read {post.title}')
            message = (f'Read {post.title} at  {post_url} \n\n  {cd['name']} \'s comments: {cd['contents']}')

            send_mail(subject, message, ['your_account@gamil.com'], [cd['to']] )
            send = True
    else:
        form = EmailPostForm()

    return render(request,
                   'blog/post/share.html',  
                   {'post':post, 'form':form, 'send':send})


#-----------------------------------------------------------------------------
#    Bu Commentariya

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id = post_id,
                             status = Post.Status.PUBLISHED)
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
    comment = None

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
<<<<<<< HEAD
=======

>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
        comment.save()

        return render(
            request,
<<<<<<< HEAD
            'blog/post/comment.html',
            {
                'post':post,
                'form':form,
                'comment':comment   
=======
            'blog/post/commnet.html',
            {
                'post':post, 
                'form':form,
                'comment':comment
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
            }
        )