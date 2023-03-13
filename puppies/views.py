from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # get details of a single puppy
    if request.method == 'GET':
        return Response({})
    # delete a single puppy
    if request.method == 'DELETE':
        return Response({})
    # update a single puppy
    if request.method == 'PUT':
        return Response({})
    
@api_view(['GET', 'POST'])
def get_post_puppy(request):
    # get all puppy
    if request.method == 'GET':
        return Response({})
    # add a single puppy    
    if request.method == 'POST':
        return Response({})