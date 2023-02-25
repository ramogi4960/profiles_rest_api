from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of API views feaatures"""
        an_apiview = [
            'uses HTTP methods as functions(get, post, put, patch, delete)',
            'I similar to a traditional django view',
            'Gives you the most control over your app\'s logic',
            'Is mapped manually to url'
        ]
        
        return Response({'Message':'Hello !\n\n', 'APIViews features': an_apiview})
