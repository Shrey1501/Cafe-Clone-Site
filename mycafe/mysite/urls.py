from django.urls import path
from mysite import views

app_name = 'mysite'

urlpatterns = [

path('reserve/',views.reserve,name='reserve'),
path('serviceone/',views.serviceone,name='serviceone'),
path('servicetwo/',views.servicetwo,name='servicetwo'),
path('servicethree',views.servicethree,name='servicethree'),

]
