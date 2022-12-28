from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('register/', RegisterView.as_view(), name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('student/', StudentAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
