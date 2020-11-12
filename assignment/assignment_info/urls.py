from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='assignments'
urlpatterns=[
    path('', views.AssigmentList.as_view(),name='list'),
    path('submit/<int:pk>/', views.SubmissionFormView,name='submit'),
    path('create_assignment/', views.CourseView, name='create'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
