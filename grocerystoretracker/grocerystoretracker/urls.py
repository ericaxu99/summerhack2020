"""grocerystoretracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# forwards requests with the pattern catalog/ to the module catalog.urls (the file with the relative URL consumers/urls.py
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# redirects 127.0.0.1:8000/ to these below
urlpatterns += [
    path('', RedirectView.as_view(url='Catalog/', permanent=True)),
]

# allows use of static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
