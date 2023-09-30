from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    # Define similar patterns for other models
]
