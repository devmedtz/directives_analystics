from django.shortcuts import render, redirect
from tablib import Dataset
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .resources import RegionResource, DistrictResource
from .models import Region, District

@login_required
def import_region(request):
    if request.method == 'POST':
        region_resource = RegionResource()
        dataset = Dataset()
        region = request.FILES['importRegion']

        if not region.name.endswith('.xls'):
            messages.error(request, 'File format format not allowed',
                       extra_tags='alert alert-danger')
            return render(request, 'location/import_region.html')

        imported_data = dataset.load(region.read(),format='xls')
        result = region_resource.import_data(dataset, dry_run=True)                                                   

        if not result.has_errors():
            # Import now
            region_resource.import_data(dataset, dry_run=False)
            
            messages.success(request, 'Success, Regions imported successfully', extra_tags='alert alert-success')
        else:
            messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

    region_list = Region.objects.all()
    context = {
        'region_list':region_list
    }

    return render(request, 'location/import_region.html', context)


@login_required
def import_district(request):
    if request.method == 'POST':
        district_resource = DistrictResource()
        dataset = Dataset()
        district = request.FILES['importDistrict']

        if not district.name.endswith('.xls'):
            messages.error(request, 'File format format not allowed',
                       extra_tags='alert alert-danger')
            return render(request, 'location/import_district.html')

        imported_data = dataset.load(district.read(),format='xls')
        result = district_resource.import_data(dataset, dry_run=True)                                                   

        if not result.has_errors():
            # Import now
            district_resource.import_data(dataset, dry_run=False)
            
            messages.success(request, 'Success, Districts imported successfully', extra_tags='alert alert-success')
        else:
            messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

    district_list = District.objects.all()

    context = {
        'district_list':district_list
    }

    return render(request, 'location/import_district.html', context)


def load_district(request):
	region_id = request.GET.get('region')
	district = District.objects.filter(region=region_id).order_by('id')
	return render(request, 'location/district_dropdown_list_options.html', {'districts': district})