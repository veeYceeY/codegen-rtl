from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('logout/',views.logout),
    path('adminhome/',views.adminhome),
    path('viewemployee/',views.viewemployee),
    path('addemployee/',views.addemployee),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)