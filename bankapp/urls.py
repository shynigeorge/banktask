from . import views
from django.urls import path

urlpatterns = [
     path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-branch/', views.load_branch, name='ajax_load_branch'),
    path('demo/', views.demo, name='demo'),

]
