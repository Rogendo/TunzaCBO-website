from django.urls import path
from. import views



app_name= 'Tunza'

urlpatterns =[
	path('', views.index,name='index'),
	path('gallery', views.gallery,name='gallery'),
    path('contact', views.submit, name='submit'),
	path('about', views.about, name='about'),

]