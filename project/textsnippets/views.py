
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from textsnippets.models import *
from rest_framework import authentication
from rest_framework import generics, permissions, serializers, authentication
from textsnippets.serializers import *

class TagsDetails(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TagSerializer
    queryset = Tags.objects.all()

    def get(self, request):
        queryset = Tags.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

class TextsnippetDetail(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TextsnippetsSerializer
    queryset = Textsnippet.objects.all()

    def get_queryset(self):
        data_queryset = Textsnippet.objects.all()
        return data_queryset

    def post(self, request, format=None):
        dataset = request.data
        serializer = TextsnippetsSerializer(data=dataset)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "0", "Message": " Successfully Created"})
        return Response({"Status": "1", "Message": serializer.errors})


class TextsnippetDataDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TextsnippetsSerializer

    def get(self, request, pk, format=None):
        details = None
        try:
            details = Textsnippet.objects.get(pk=pk)
        except:
            return Response({'Status': "1", 'Message': "Item not found"})
        serializer = TextsnippetsSerializer(details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        details = None
        try:
            details = Textsnippet.objects.get(pk=pk)
        except:
            return Response({'Status': "1", 'Message': "Item not found"})

        serializer = TextsnippetsSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': "0", 'Message': "Successfully Updated!", 'Body': serializer.data})
        return Response({'Status': "1", 'Message': serializer.errors}, )

    def delete(self, request, pk, format=None):
        details = None
        try:
            details = Textsnippet.objects.get(pk=pk)
        except:
            return Response({'Status': "1", 'Message': "Item not found"})
        try:
            details.delete()
            return Response({'Status': "0", 'Message': "Successfully Deleted!"})
        except:
            return Response({'Status': "1", 'Message': "Deletion failed!"})

class Tagdata(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TextsnippetsSerializer
    queryset = Textsnippet.objects.all()

    def get_queryset(self):
        tag_filter = self.request.query_params.get('tag')
        try:
            tagdetails = Tags.objects.get(Tag=tag_filter)
            details = Textsnippet.objects.filter(TagId=tagdetails.TagId)
        except:
            details = Textsnippet.objects.none()
        return details
