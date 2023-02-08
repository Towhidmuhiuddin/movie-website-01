from django.urls import path
from store import views

urlpatterns = [
    path('',views.home,name='home'),
    path('collections/',views.collections, name='collections'),
    path('collections/<str:slug>',views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:mov_slug>',views.moviesview, name='movieview'),

]
