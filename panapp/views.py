from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PanCardSerializer
from .models import PanCard

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/pan-list/',
        'Detail View': '/pan-detail/<int:id>/',
        'Create': '/pan-create/',
        'Update': '/pan-update/<int:id>/',
        'Delete': '/pan-detail/<int:id>/',
    }
    return Response(api_urls);


@api_view(['GET'])
def ShowAll(request):
    pans = PanCard.objects.all()
    #pans = PanCard.objects.only('pan_id', 'pan_details')
    serializer = PanCardSerializer(pans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewPan(request, pk):
    pan = PanCard.objects.get(id=pk)
    serializer = PanCardSerializer(pan, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreatePan(request):
    serializer = PanCardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updatePan(request, pk):
    pan = PanCard.objects.get(id=pk)
    serializer = PanCardSerializer(instance=pan, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deletePan(request, pk):
    pan = PanCard.objects.get(id=pk)
    pan.delete()

    return Response('Items delete successfully!')




