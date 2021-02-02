from django.urls import path
from .views import(
 blog_post_view, post_list_view,
 create_post_view, dynamic_lookup_view, post_delete_view
)

app_name = 'blog'
urlpatterns = [
    path('post', blog_post_view, name='post'),
    path('create_view', create_post_view),
    path('post/<int:id>/', dynamic_lookup_view, name='post-view'),
    path('post/<int:id>/delete/', post_delete_view, name='post'),
    path('list/', post_list_view, name='list')
]