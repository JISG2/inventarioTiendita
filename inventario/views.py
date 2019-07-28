from inventario.models import proteinasModel
from inventario.models import glutaminasModel
from inventario.models import aminoacidosModel
from .serializers import proteinasSerializer
from .serializers import glutaminasSerializer
from .serializers import aminoacidosSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import JSONParser
# Create your views here.

class proteinasView(APIView):
    def get(self,request,format=None):
        queryset =proteinasModel.objects.all()
        serializer = proteinasSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = proteinasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response,status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        inventario = proteinasModel.objects.get(id=pk)
        serializer = proteinasSerializer(inventario, data=data)
        if serializer.is_valid():
            proteinaUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,format=None):
        proteina = get_object_or_404(proteinasModel.objects.all(), pk=pk)
        proteina.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

class aminoacidosView(APIView):
    def get(self,request,format=None):
        queryset =aminoacidosModel.objects.all()
        serializer = aminoacidosSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = aminoacidosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response,status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        aminoacido = aminoacidosModel.objects.get(id=pk)
        serializer = proteinasSerializer(aminoacido, data=data)
        if serializer.is_valid():
            aminoacidosUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,format=None):
        aminoacido = get_object_or_404(aminoacidosModel.objects.all(), pk=pk)
        aminoacido.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

class glutaminasView(APIView):
    def get(self,request,format=None):
        queryset =glutaminasModel.objects.all()
        serializer = glutaminasSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = glutaminasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response,status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = request.data
        glutamina = glutaminasModel.objects.get(id=pk)
        serializer = glutaminasSerializer(glutamina, data=data)
        if serializer.is_valid():
            glutaminaUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,format=None):
        glutamnia = get_object_or_404(glutaminasModel.objects.all(), pk=pk)
        glutamnia.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

class proteinasView2(APIView):
    def put(self, request, pk):
        data = request.data
        inventario = proteinasModel.objects.get(id=pk)
        serializer = proteinasSerializer(inventario, data=data)
        if serializer.is_valid():
            proteinaUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,format=None):
        proteina = get_object_or_404(proteinasModel.objects.all(), pk=pk)
        proteina.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

    def get_object(self,pk):
        try:
            return proteinasModel.objects.get(pk=pk)
        except proteinasModel.DoesNotExist:
            return "NO"
    def get(self,request,pk,format=None):
        ID = self.get_object(pk)
        ID = proteinasSerializer(ID)
        return Response(ID.data)

class aminoacidosView2(APIView):
    def put(self, request, pk):
        data = request.data
        inventario = aminoacidosModel.objects.get(id=pk)
        serializer = aminoacidosSerializer(inventario, data=data)
        if serializer.is_valid():
            aminoacidoUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,format=None):
        aminoacido = get_object_or_404(aminoacidosModel.objects.all(), pk=pk)
        aminoacido.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

    def get_object(self,pk):
        try:
            return aminoacidosModel.objects.get(pk=pk)
        except aminoacidosModel.DoesNotExist:
            return "NO"
    def get(self,request,pk,format=None):
        ID = self.get_object(pk)
        ID = aminoacidosSerializer(ID)
        return Response(ID.data)

class glutaminasView2(APIView):
    def put(self, request, pk):
        data = request.data
        inventario = glutaminasModel.objects.get(id=pk)
        serializer = glutaminasSerializer(inventario, data=data)
        if serializer.is_valid():
            glutaminaUpdate = serializer.save()
            return Response({'ok':"actualizado"})
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,format=None):
        glutamina = get_object_or_404(glutaminasModel.objects.all(), pk=pk)
        glutamina.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

    def get_object(self,pk):
        try:
            return glutaminasModel.objects.get(pk=pk)
        except glutaminasModel.DoesNotExist:
            return "NO"
    def get(self,request,pk,format=None):
        ID = self.get_object(pk)
        ID = glutaminasSerializer(ID)
        return Response(ID.data)

