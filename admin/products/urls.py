from django.urls import path
from . views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('products/<str:id>', ProductViewSet.as_view({
        'get': 'retreive',
        'put': 'update',
        'delete': 'delete',
    })),

    path('users', UserAPIView.as_view()),
]