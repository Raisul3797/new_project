from django.urls import path
from .import views
# from student.views import home,about,education,contact,data
urlpatterns = [

   path('', views.index,name='home'),
   path('about/', views.about,name='about'),
   path('education/', views.education,name='education'),
   path('contact/', views.contact,name='contact'),
   #path('data/', views.contact,name='data')
   ]



  

   