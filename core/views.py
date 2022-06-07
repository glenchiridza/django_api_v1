from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

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
    def get(self, request, *args, **kwargs):
        from core.models import Post
        query_set = Post.objects.all()
        serializer = PostSerializer(query_set, many=True)

        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



