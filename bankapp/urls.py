from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('demo/', views.demo, name='demo'),
    path('registration/', views.registration, name='registration'),

    path('person_change/<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-branch/', views.load_branch, name='ajax_load_branch'),

]