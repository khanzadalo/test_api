from django.contrib import admin
from django.urls import path
from test_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test_api),

]
