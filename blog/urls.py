<<<<<<< HEAD
from  django.urls import path
from . import views



app_name='blog'

urlpatterns = [

    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]


=======
from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.PostListViev.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment')
    
]
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
