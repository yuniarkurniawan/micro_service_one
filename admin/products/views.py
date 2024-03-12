from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Products, User
from . serializers import ProductSerializer
from . producer import publish
import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        product = Products.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retreive(self, request, id=None):
        product = Products.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, id=None):
        product = Products.objects.get(id=id)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        product = Products.objects.get(id=id)
        product.delete()
        publish('product_deleted', id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):

    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)

        return Response({
            'id': user.id,
        })
