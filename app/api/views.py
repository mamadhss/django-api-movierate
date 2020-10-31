from rest_framework import viewsets,status
from rest_framework.permissions import BasePermission,SAFE_METHODS,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import Movie,Rating
from rest_framework.response import Response
from .serializers import MovieSerializer,RatingSerializer


class ReadOnly(BasePermission):
    def has_permission(self,request,view):
        return request.method in SAFE_METHODS
            
        
        
        


class MovieViewSet(viewsets.ModelViewSet):
    queryset =  Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser|ReadOnly]



class RateViewSet(APIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self,request,movie_id=None):
        movie = Movie.objects.get(pk=movie_id)
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user,movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def get(self,request,movie_id=None):
        
        movie = Movie.objects.get(pk=movie_id)
        serializer = RatingSerializer(movie.rates,many=True)
        return Response(serializer.data)
           


    
