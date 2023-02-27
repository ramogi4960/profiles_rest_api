from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets

# Create your views here.
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

    def  create(self, request):
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