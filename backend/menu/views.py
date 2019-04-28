from django.shortcuts import render

# Create your views here.
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics, filters
from rest_framework.filters import SearchFilter



class ListMenu(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ListMenuFiltered(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    # search_fields = ('title')
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('title', 'type', 'price')
    ordering = ('title',)



class DetailMenu(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# class ListSortMenu(generics.ListCreateAPIView):
#     # print(kwargs)
#
#     def get_queryset(self):
#
#         print(self.kwargs)
#         params = self.kwargs['slug']
#         print(params)
#         sort_by, order = params.split('-')[1], params.split('-')[2]
#         print(sort_by, order)
#
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
