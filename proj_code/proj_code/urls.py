"""proj_code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500

from .views import index,register_page,login_page,leaderboard,logout_page,rules,question,admin_view,soon_view
from django.conf.urls.static import static
# from verify.views import gen2
from .views import comp

urlpatterns = [
    path('admin/', admin_view),
    path('', comp),
    path('signup/', comp),
    path('login/', comp),
    path('logout/', logout_page),
    path('leaderboard/', leaderboard),
    path('f061q2h/', admin.site.urls),
    #path('upgrade/', upgrade),
    path('dashboard/', comp),
    path('rules/', comp),
    path("404/", admin_view),


    path('sign/', comp),
    path('log/', comp),
    path('log/', logout_page),
    path('leader/', comp),
    path('dash/', comp),
]


handler404=admin_view
handler500=admin_view
