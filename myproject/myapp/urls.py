from django.urls import path
# allows to have multiple urls in the list
from.import views
urlpatterns = [
    path('', views.index,name='index'),
    # when quotes are empty it is main page
    # path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('post/<str:pk>',views.post,name='post'),
    path('profile',views.profile,name='profile'),
    path('index',views.index,name='index'), 
    path('home',views.home,name='home'),
    path('create',views.create,name='create'),
    path('vote',views.vote,name='vote'),
    path('results',views.results,name='results'),
    path('contact',views.contact,name='contact'),
    path('list',views.list,name='list'),   
]
