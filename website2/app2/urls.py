from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('course',views.course,name='course'),
    path('services',views.services,name='services'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('registration',views.registration,name='registration'),
    path('details/<int:id>',views.details,name='details'),
    path('checkout/<int:id>',views.checkout,name='checkout'),
    path('addtowish/<int:id>',views.addtowish,name='addtowish'),

    path('confirmorder',views.confirmorder,name='confirmorder'),
    path('myorder',views.myorder,name='myorder'),
    path('wish',views.wish,name='wish'),



    # # admin pages 
    path('dashboard',views.dashboard,name='dashboard'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('contacts',views.contacts,name='contacts'),
    path('dashregistration',views.dashregistration,name='dashregistration'),
    path('editcourse/<int:id>',views.editcourse,name='editcourse'),
    path('viewcourse',views.viewcourse,name='viewcourse'),
    path('dashboardlogin',views.dashboardlogin,name='dashboardlogin'),
    path('dashlogout',views.dashlogout,name='dashlogout'),




]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)