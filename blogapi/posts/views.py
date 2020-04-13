from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
