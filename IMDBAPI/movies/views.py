# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Genre, Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import GenreSerializer, MovieSerializer, MovieDetailsSerializer


# Create your views here.
class MovieList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieDetailsSerializer(movies, many=True)
        return Response(serializer.data)

    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        data = request.data
        count=0

        for genre in data['genre']:
            count += 1
            Genre.objetcs.get_or_create(name=genre)

        if count == 0:
            return Response({"Genre is not found in Input JSON"},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            movie_name = data['movie']
            director = data['director']
            Movie.objects.get(name=movie_name, director=director)
            return Response("[Movie, Director]: ["+movie_name+", "+director+
                            "] is already present in Record",
                            status=status.HTTP_304_NOT_MODIFIED)
        except Movie.DoesNotExist:
            serializer = MovieSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.initial_data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class MovieDetails(APIView):

    def get(self, request, pk, format=None):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieDetailsSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response("Movies Key : "+pk+" not found in record",
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            movie = Movie.objects.get(pk=pk)
            data = request.data
            count = 0

            for genre in data['genre']:
                count += 1
                Genre.objects.get_or_create(name=genre)

            if count == 0:
                return Response({"Genre not present in input JSON"},
                                status=status.HTTP_404_NOT_FOUND)
            serializer = MovieDetailsSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save(owner=self.request.user)
                return Response(serializer.initial_data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Movie.DoesNotExist:
            return Response({"Movie Key : "+pk+" not found in record"},
                            status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({"Movie Key : "+pk+" deleted from record"},
                            status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response({"Movie Key : "+pk+" not found in record"},
                            status=status.HTTP_404_NOT_FOUND)


class MovieSearch(generics.ListAPIView):
    serializer_class = MovieDetailsSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()

        name = self.request.query_params.get('name', None)
        imdb_score = self.request.query_params.get('imdb_score', None)
        director = self.request.query_params.get('director', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if imdb_score is not None:
            queryset = queryset.filter(imdb_score=imdb_score)
        if director is not None:
            queryset = queryset.filter(director__icontains=director)

        return queryset