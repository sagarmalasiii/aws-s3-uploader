from django.urls import path
from .views import UploadFileView, ListFilesView, DeleteFileView

urlpatterns = [
    path('upload/', UploadFileView.as_view()),
    path('files/', ListFilesView.as_view()),
    path('delete/<str:filename>/', DeleteFileView.as_view()),
]
