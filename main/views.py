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
			pass
			#school_qs = school_qs.filter(school_subjects__in=school_subjects)

	if 'exam_4_review' in request.GET:
		exam_4_review = request.GET['exam_4_review']
		if exam_4_review:
			pass
			#school_qs = school_qs.filter(curricular_system=curricular_system)

	if 'exam_6_review' in request.GET:
		exam_6_review = request.GET['exam_6_review']
		if exam_6_review:
			pass
			#school_qs = school_qs.filter(curricular_system=curricular_system)

	if 'combination' in request.GET:
		combination = request.GET.getlist('combination')
		if combination:
			pass
			#school_qs = school_qs.filter(subject_combination__in=combination)

	if 'fee_from' and 'fee_to' in request.GET:
		fee_from = request.GET.get('fee_from', 0)
		fee_to = request.GET.get('fee_to', 50000000)
		if fee_from and fee_to:
			school_qs = school_qs.filter(average_tution_fee__gte=fee_from).filter(average_tution_fee__lte=fee_to)


	if 'charity_support' in request.GET:
			charity_support = request.GET.get('charity_support', 0)
			print(charity_support)
			if charity_support:
				school_qs = school_qs.filter(no_fee=charity_support)
		


	print('school_qs:', school_qs)
	 
	school_subjects = request.GET.getlist('school_subjects')
	combination = request.GET.getlist('combination')

	context = {
		'school_qs':school_qs,
		'values': request.GET,
		'subject_checked':school_subjects,
		'combinations':combination,
	}

	template_name = 'main/index.html'

	
	return render(request, template_name, context)