"""
URL configuration for gameland project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path

from task1.views import sign_up_by_html,sign_up_by_django,game,platform,cart,news

html_ = [
    path('admin/', admin.site.urls),


    path('platform/', platform),
    path('platform/news/', news),
    path('games/', game),
    path('cart/', cart),

    path('sign1/', sign_up_by_django),
    path('sign/', sign_up_by_html),

]
urlpatterns = html_

