from django.contrib import admin
from django.urls import path
from . import views

app_name ='level5_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('registration/',views.registration,name='registeration'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='logout'),
]