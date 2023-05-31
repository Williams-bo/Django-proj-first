from django.urls import path

from .views import post_list, post_detail, post_create, post_edit, base_list

urlpatterns = [
    path('', post_list),
    path('base/', base_list),
    path('create/', post_create),
    path('<post_id>/', post_detail),
    path('<post_id>/<edit>/', post_edit)
]