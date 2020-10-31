from rest_framework import serializers
from .models import Movie,Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Rating
        fields = ('user','stars')


class MovieSerializer(serializers.ModelSerializer):
    rates = RatingSerializer(many=True,read_only=True)
    number_of_rates = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('id','title','description','rates','number_of_rates','avg_rating')

    def get_number_of_rates(self,obj):
        return Rating.objects.filter(movie=obj).count()  


    def get_avg_rating(self,obj):
        ratings = Rating.objects.filter(movie=obj)
        total = 0 
        for rating in ratings:
            total += rating.stars

        if len(ratings) > 0 :
            return total / len(ratings)
        return 0        


              


            


