from django.contrib import admin
from django.urls import path, include
from quiz.views import register
from quiz.views import log_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]

