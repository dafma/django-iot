from rest_framework import routers, serializers, viewsets
from iot.models import Device, DeviceType, DeviceData

# Serializers define the API representation.
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('url', 'id', 'name', 'description', 'variables', 'commands', 'device_type')

# ViewSets define the view behavior.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# Serializers define the API representation.
class DeviceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceType
        fields = ('url', 'id', 'name', 'description')

# ViewSets define the view behavior.
class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer


# Serializers define the API representation.
class DeviceDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceData
        fields = ('url', 'id', 'device', 'variable', 'value', 'timestamp')

# ViewSets define the view behavior.
class DeviceDataViewSet(viewsets.ModelViewSet):
    queryset = DeviceData.objects.all()
    serializer_class = DeviceDataSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = DeviceData.objects.all()
        pk = self.request.query_params.get('pk', None)
        if pk is not None:
            queryset = queryset.filter(device__id=pk)
        return queryset



iot_router = routers.DefaultRouter()
iot_router.register(r'device-types', DeviceTypeViewSet)
iot_router.register(r'devices', DeviceViewSet)
#figure out how to filter down to specific device, and
#better, variable  (might have to use fn based views?)
iot_router.register(r'device-data', DeviceDataViewSet)
# iot_router.register(r'device/update', )