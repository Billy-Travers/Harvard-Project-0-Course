from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("lookup/", views.lookup, name="lookup"),
    path("new/", views.page_new_create, name="page_new_create"),
    path("edit/", views.edit, name="edit"),
    path("edit_record/", views.edit_record, name="edit_record"),
    path("page_random/", views.page_random, name="page_random")
]
