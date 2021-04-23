from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Owner
from .serializers import OwnerSerializer

class OwnerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    pagination_class = None

class OwnerView(RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

# class TopSellerView(ListAPIView):
#     permission_classes = (permissions.AllowAny, )
#     queryset = Realtor.objects.filter(top_seller=True)
#     serializer_class = RealtorSerializer
#     pagination_class = None
