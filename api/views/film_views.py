from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.film import Film
from ..serializers import FilmSerializer

# Create your views here.


class FilmsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FilmSerializer

    def get(self, request):
        """Index request"""
        # Get all the films:
        # films = Film.objects.all()
        # Filter the films by owner, so you can only see your owned films
        films = Film.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = FilmSerializer(films, many=True).data
        return Response({'films': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['film']['owner'] = request.user.id
        # Serialize/create film
        film = FilmSerializer(data=request.data['film'])
        # If the film data is valid according to our serializer...
        if film.is_valid():
            # Save the created film & send a response
            film.save()
            return Response({'film': film.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(film.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the film to show
        film = get_object_or_404(Film, pk=pk)
        # Only want to show owned films?
        if request.user != film.owner:
            raise PermissionDenied('Unauthorized, you do not own this film')

        # Run the data through the serializer so it's formatted
        data = FilmSerializer(film).data
        return Response({'film': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate film to delete
        film = get_object_or_404(Film, pk=pk)
        # Check the film's owner against the user making this request
        if request.user != film.owner:
            raise PermissionDenied('Unauthorized, you do not own this film')
        # Only delete if the user owns the  film
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Film
        # get_object_or_404 returns a object representation of our Film
        film = get_object_or_404(Film, pk=pk)
        # Check the film's owner against the user making this request
        if request.user != film.owner:
            raise PermissionDenied('Unauthorized, you do not own this film')

        # Ensure the owner field is set to the current user's ID
        request.data['film']['owner'] = request.user.id
        # Validate updates with serializer
        data = FilmSerializer(film, data=request.data['film'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
