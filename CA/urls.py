from django.urls import path
from . import views

urlpatterns = [
    path('casignup/',views.SignupView,name='CASIGNUP'),
    path('login/',views.login,name='CALOGIN'),
    path('calogout/',views.userLogOut,name='CALOGOUT'),

# -------------------------------------------------------------------------
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
    path('faq/',views.faq, name='faq'),

    path('',views.home, name='home'),
    
# ----------------------------For CHAT---------------------------------------------
    path('index', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

]
