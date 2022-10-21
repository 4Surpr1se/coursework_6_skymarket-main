from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_image = serializers.CharField(source='author.image')

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
