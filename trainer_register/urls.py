from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainer_form,name='trainer_insert'),
    path('<int:id>/', views.trainer_form,name='trainer_update'),
    path('delete/<int:id>/',views.trainer_delete,name='trainer_delete'),    
    path('list/',views.trainer_list,name='trainer_list'),
    path('rain/',views.rain,name='rain')
]