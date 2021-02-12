from .models import GalleryImage
from rest_flex_fields import FlexFieldsModelSerializer


class GalleryImageSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'
