from . import views
from django.urls import path


urlpatterns = [
    # path('', views.ListMenu.as_view()),  # just list
    # path('', views.ListMenuFiltered.as_view()),
    path('', views.ListMenu.as_view()),
    path('<int:pk>/', views.DetailMenu.as_view()),
    # path('<slug:slug>/', views.ListSortMenu.as_view()),
]
