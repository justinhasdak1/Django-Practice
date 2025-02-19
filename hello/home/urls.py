from django.contrib import admin
from django.urls import path
admin.site.site_header = "Hasdak Admin"
admin.site.site_title = "Hasdak Admin Portal"
admin.site.index_title = "Welcome to Hasdak Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]