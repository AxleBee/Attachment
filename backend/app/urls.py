from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    ## authentication paths
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),
    ## student paths
    path('add_attachment/', add_attachment, name="add_attachment"),
    path('view_attachments/', view_attachments, name='view_attachments'),
    path('delete_attachment/', delete_attachment, name="delete_attachment"),
    path('student_profile/', student_profile, name="student_profile"),
    path('add_logbook/', add_logbook, name="add_logbook"),
    path('search_logbook/', search_logbook, name="search_logbook"),
    
   ## supervisor paths
   path('supervisor_dashboard/', supervisor_dashboard, name="supervisor_dashboard"),
   path('supervisor_feedback/<str:email>', supervisor_feedback, name="supervisor_feedback"),
   path('log_feed/<int:log_id>', logbook_comment, name="logbook_comment"),
   path('supervisor_profile/', supervisor_profile, name='supervisor_profile'),
   
   path('employer_dashboard/', employer_dashboard, name="employer_dashboard"),
   path('employer_comment/<str:email>', employer_comment, name="employer_comment"),
   path('employer_profile/', employer_profile, name = "employer_profile" )
   
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
