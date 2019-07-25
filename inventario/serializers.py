from .models import proteinasModel
from .models import glutaminasModel
from .models import aminoacidosModel
from rest_framework import routers, serializers, viewsets

class proteinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = proteinasModel
        fields = ('__all__')

class glutaminasSerializer(serializers.ModelSerializer):
    class Meta:
        model = glutaminasModel
        fields = ('__all__')
class aminoacidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = aminoacidosModel
        fields = ('__all__')
