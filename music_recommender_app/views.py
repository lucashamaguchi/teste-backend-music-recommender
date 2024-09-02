from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from music_recommender_app.services import MusicRecommender

# Create your views here.


class MusicViewSet(viewsets.ViewSet):
    permission_classes = []

    def list(self, request, *args, **kwargs):
        if len(request.query_params.get('long', list())) < 1:
            return Response({"message": "Missing long parameter"})
        if len(request.query_params.get('lat', list())) < 1:
            return Response({"message": "Missing lat parameter"})

        music_recommender_service = MusicRecommender()
        response = music_recommender_service.get_song_indications_by_location(request.query_params['lat'], request.query_params['long'])
        return Response(response)
