
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from api.models import Profile, Book


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class ProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'profile_type', 'user']
        depth = 1


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre']


# Example of a simple Authenticated GET request, get the profile for the user making the request, if they have one
class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.get(user=request.user)
            return Response(ProfileSerializer(profile).data)
        return Response(status=HTTP_404_NOT_FOUND)


# Example of authenticated CRUD operations on a Book table using Generic Views:
#   https://www.django-rest-framework.org/api-guide/generic-views/
# The "ListCreate" view will handle GET requests for a list of books, as well as POST requests to create a new book
# The default behavior can be overridden by overwriting the "list" and "create" methods in the class
class BookListCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


# The "RetrieveUpdateDestroy" view will handle GET, PUT, and DELETE requests by id (or whatever the lookup_field is)
# default behaviors can be overridden using the "retrieve", "update", or "destroy" methods
class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
