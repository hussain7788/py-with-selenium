from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']


#### This is for Serializers Relations 
# class SingerSerializer(serializers.ModelSerializer):
#     song = serializers.StringRelatedField(many= True, read_only= True)
#     # song = serializers.PrimaryKeyRelatedField(many= True, read_only= True,)
#     # song = serializers.HyperlinkedRelatedField(many= True, read_only= True, view_name='song-detail')
#     # song = serializers.SlugRelatedField(many= True, read_only= True, slug_field='title')  # it will give fields in song model

#     class Meta:
#         model = Singer
#         fields = ['id', 'name', 'gender', 'song']


####### This is for Nested Serializer 
class SingerSerializer(serializers.ModelSerializer):
    ## Here 'song' variable is related_name field in models .Both should be same
    song = SongSerializer(many= True, read_only= True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']

