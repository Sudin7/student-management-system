from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='home'),
    path('api/v1/',include('api.urls')),
    path('students/', include('students.urls')),
    path('register/', AccountViews.register.as_view(), name='register'),
    path('login/', AccountViews.login.as_view(), name='login'),
    path('logout/', AccountViews.logout.as_view(), name='logout'),

]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)