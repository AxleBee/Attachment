from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

  path('register/', register, name ='register'),
  path('login/', login_view, name ='login'),
  path('add_attachment/', add_attachment, name="add_attachment"),
  path('student_profile/', add_profile, name="student_profile"),
  path('logout/', logout_view, name ='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
