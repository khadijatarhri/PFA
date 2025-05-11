from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
=======
    path('detect/', views.detect_sensitive_info, name='detect_sensitive_info'),
>>>>>>> Debut de l integration de presidio dans le backend
]