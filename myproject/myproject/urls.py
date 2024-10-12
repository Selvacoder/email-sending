# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp import views  # Import views from myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Route for your app
    path('', views.send_email, name='sendMail'),  # Root URL -> home view
]
