from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Thing
from .serializers import ThingSerializer
from .permissions import OwnerOnly

class ThingListCreateView(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer



class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer 
    permission_classes=[OwnerOnly]   