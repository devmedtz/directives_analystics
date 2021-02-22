from django.shortcuts import render

from .models import School

def homepage(request):

	school_qs = School.objects.order_by('-created_at')

	if 'gender' in request.GET:
		gender = request.GET['gender']
		if gender:
			school_qs = school_qs.filter(gender=gender)

	if 'accomodation' in request.GET:
		accomodation = request.GET['accomodation']
		if accomodation:
			school_qs = school_qs.filter(accomodation_type=accomodation)

	if 'class_size' in request.GET:
		class_size = request.GET['class_size']
		if class_size:
			school_qs = school_qs.filter(class_size=class_size)

	if 'multicultural' in request.GET:
		multicultural = request.GET['multicultural']
		if multicultural:
			school_qs = school_qs.filter(school_multicultural=multicultural)

	if 'school_location' in request.GET:
		school_location = request.GET['school_location']
		if school_location:
			school_qs = school_qs.filter(school_location=school_location)

	if 'curricular_system' in request.GET:
		curricular_system = request.GET['curricular_system']
		if curricular_system:
			school_qs = school_qs.filter(curricular_system=curricular_system)

	if 'school_subjects' in request.GET:
		school_subjects = request.GET.getlist('school_subjects')
		if school_subjects:
			school_qs = school_qs.filter(school_subjects__in=school_subjects)

	print('school_qs:', school_qs)

	context = {
		'school_qs':school_qs,
		'values': request.GET,
		'subject_checked':school_subjects,
	}

	template_name = 'main/index.html'

	
	return render(request, template_name, context)