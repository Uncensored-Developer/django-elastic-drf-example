from django.urls import path
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Here add your URL's
    path('articles/', include('articles.urls')),
]
