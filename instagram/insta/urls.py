
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='main'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('new/', views.new, name="new"),
    path("<int:post_pk>/edit/", views.edit, name='edit'),
    path("<int:post_pk>/delete/", views.delete, name="delete"),
    path('<int:post_pk>/comment/', views.create_comment, name="create_comment"),
    path("<int:post_pk>/comment_edit/", views.comment_edit, name="comment_edit"),
    path("<int:post_pk>/comment_delete/", views.comment_delete, name="comment_delete"),

]

