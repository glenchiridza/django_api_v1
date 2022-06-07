from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


def test_view(request):
    data = {
        'name': 'glen',
        'age': 23
    }
    return JsonResponse(data)


#
# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'name': 'glen',
#             'age': 23
#         }
#         return Response(data)

class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        from core.models import Post
        query_set = Post.objects.all()
        serializer = PostSerializer(query_set, many=True)

        # no need to put many=True on single instance
        single_instance_query = Post.objects.first()
        serializer_single_post = PostSerializer(single_instance_query)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# using generics

class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # def perform_create(self, serializer):
    #     #put some custom logic in between the serializer being saved and method being called
    #     #eg send email
    #     serializer.save()

    def post(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


class PostCreate(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

