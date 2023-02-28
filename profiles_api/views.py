from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers
from . import models
from . import permissions


# All my views here

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API views features"""
        an_apiview = [
            'uses HTTP methods as functions(get, post, put, patch, delete)',
            'I similar to a traditional django view',
            'Gives you the most control over your app\'s logic',
            'Is mapped manually to url'
        ]

        return Response({'Message': 'Hello !', 'APIViews features': an_apiview})

    def post(self, request):
        """Create a hello message with our API"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'Message': 'Put'})

    def patch(self, request, pk=None):
        """ Handle partial update of object """
        return Response({'Message': 'Patch'})

    def delete(self, request, pk=None):
        """ Deletes an object """
        return Response({'Method': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """ Tests API viewsets """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            'Uses actions: create, retrieve, ipdate, partal update',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]
        return Response({'Message': 'Hello', 'Viewsets about': a_viewset}
                        )

    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'Message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting object by ID """
        return Response({'http_method': 'Get'})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'http_method': 'Put'})

    def partial_update(self, request, pk=None):
        """ Handles updating part of an object"""
        return Response({'http_method': 'Patch'})

    def destroy(self, request, pk=None):
        """ Handles deleting an object"""
        return Response({'http_method': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    extra_kwargs = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """ Sets the user profile to the logged user """
        serializer.save(user_profile=self.request.user)
