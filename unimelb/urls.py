"""unimelb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import  settings
from django.views.static import serve
from django.urls import path
import face
from face.views import home_view,survey_view,page_not_found
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('survey/',survey_view),
    path('result/', survey_view),
    url(r'^media/images/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
]
handler404 = face.views.page_not_found
