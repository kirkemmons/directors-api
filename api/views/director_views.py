from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.director import Director
from ..serializers import DirectorSerializer

# Create your views here.


class DirectorsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DirectorSerializer

    def get(self, request):
        """Index request"""
        # Get all the directors:
        # directors = Director.objects.all()
        # Filter the directors by owner, so you can only see your owned directors
        directors = Director.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = DirectorSerializer(directors, many=True).data
        return Response({'directors': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['director']['owner'] = request.user.id
        # Serialize/create director
        director = DirectorSerializer(data=request.data['director'])
        # If the director data is valid according to our serializer...
        if director.is_valid():
            # Save the created director & send a response
            director.save()
            return Response({'director': director.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(director.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the director to show
        director = get_object_or_404(Director, pk=pk)
        # Only want to show owned directors?
        if request.user != director.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this director')

        # Run the data through the serializer so it's formatted
        data = DirectorSerializer(director).data
        return Response({'director': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate director to delete
        director = get_object_or_404(Director, pk=pk)
        # Check the director's owner against the user making this request
        if request.user != director.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this director')
        # Only delete if the user owns the  director
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Director
        # get_object_or_404 returns a object representation of our Director
        director = get_object_or_404(Director, pk=pk)
        # Check the director's owner against the user making this request
        if request.user != director.owner:
            raise PermissionDenied(
                'Unauthorized, you do not own this director')

        # Ensure the owner field is set to the current user's ID
        request.data['director']['owner'] = request.user.id
        # Validate updates with serializer
        data = DirectorSerializer(
            director, data=request.data['director'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
