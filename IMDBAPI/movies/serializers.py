from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    genre = serializers.SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Movie
        fields = ('owner', 'name', 'popularity', 'director',
                  'imdb_score', 'genre')


class MovieDetailsSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Movie
        fields = ('name', 'popularity', 'director', 'imdb_score', 'genre')