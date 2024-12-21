from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_view),  # Default endpoint
    path('sum/', views.sum_view),  # Sum endpoint
]
