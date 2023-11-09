"""
URL configuration for fourHTMLPages project.

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
from django.contrib import admin
from django.urls import path
from app.views import view1,view2,view3,view4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view1/',view1,name='view1'),
    path('view2/',view2,name='view2'),
    path('view3/',view3,name='view3'),
    path('view4/',view4,name='view4'),
]
