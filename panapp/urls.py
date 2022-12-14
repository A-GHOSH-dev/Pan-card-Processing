from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),

    path('pan-list/', views.ShowAll, name='pan-list'),
    path('pan-detail/<int:pk>/', views.ViewPan, name='pan-detail'),
    path('pan-create/', views.CreatePan, name='pan-create'),
    path('pan-update/<int:pk>/', views.updatePan, name='pan-update'),
    path('pan-delete/<int:pk>/', views.deletePan, name='pan-delete'),


]