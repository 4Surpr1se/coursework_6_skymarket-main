
from rest_framework import pagination, viewsets, status

from ads.models import Ad, Comment
from ads.serializers import AdSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import BoundField

from ads.serializers import AdDetailSerializer, CommentDetailSerializer, CommentSerializer

from users.models import User

from ads.permissions import AdAndCommentPermission


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    # TODO как изменить отправляемый данные обратно через сериализатор??!!!!! Я ПОНЯЛ - ВСЕ НОРМ!
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = dict(serializer.data)
        author_queryset = User.objects.get(pk=response.get('author'))
        response['author_first_name'] = author_queryset.first_name
        response['author_last_name'] = author_queryset.last_name
        response['author_id'] = response.pop('author')
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'partial_update']:
            self.serializer_class = AdDetailSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        elif self.action in ['destroy', 'partial_update']:
            permission_classes = [IsAuthenticated, AdAndCommentPermission]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]


class AdMeAPIView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Ad.objects.all().filter(author_id=request.user.id)
        return self.list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = dict(serializer.data)
        author_queryset = User.objects.get(pk=response.get('author'))
        response['author_first_name'] = author_queryset.first_name
        response['author_last_name'] = author_queryset.last_name
        response['author_id'] = response.pop('author')
        response['author_image'] = author_queryset.image.url if author_queryset.image else None

        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        print(self.action)
        if self.action in ['retrieve', 'partial_update']:
            self.serializer_class = CommentDetailSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = []
        elif self.action in ['destroy', 'partial_update']:
            permission_classes = [IsAuthenticated, AdAndCommentPermission]
        else:
            permission_classes = [IsAuthenticated, ]
        return [permission() for permission in permission_classes]

