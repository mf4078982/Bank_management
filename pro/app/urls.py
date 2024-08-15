from django.urls import path
from .import views


urlpatterns = [
    path('',views.add,name='add'),
    path('home/',views.home,name='home'),
    path('deposit/',views.deposit,name='deposit'),
    path('withdraw/',views.withdraw,name='withdraw'),
    path('exit/',views.exit,name='exit'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]
