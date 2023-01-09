from django.urls import path

from api.views import ProfileView, BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('book', BookListCreate.as_view()),
    path('book/<int:id>', BookRetrieveUpdateDestroy.as_view()),
]
