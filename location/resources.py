from import_export import resources
from import_export.fields import Field

from .models import Region, District


class RegionResource(resources.ModelResource):

    class Meta:
        model = Region
        fields = ('id', 'name','capital','districts','area','population','postcode','zone',)


class DistrictResource(resources.ModelResource):

    class Meta:
        model = District
        fields = ('id', 'region', 'name', 'population', )