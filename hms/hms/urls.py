from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import LoginView
from user.views import user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
