from django.shortcuts import render
from datetime import datetime, timedelta
from django.db.models import Max, Min, Sum, Count, Avg

from .models import *

from .forms import SchoolForm

from .filter import SchoolFilter


def school_list(request):

	f = SchoolFilter(request.GET, queryset=School.objects.all())

	if 'exam_4_review' in request.GET:
		exam_4_review = request.GET.get('exam_4_review', '')
		start_o_year = (datetime.now() - timedelta(days=int(exam_4_review)*365)).year
		end_o_year = datetime.now().year

		# users = UserClasses.objects.filter(class_id=data['class_id'])
		# user_details = User.objects.filter(id__in=users.values_list('id', flat=True))

		schools = f.qs

		print(schools)

		dv1T = ExamResult.objects.filter(school_id__in=schools.values_list('id'), classe=4, year__range=(start_o_year,end_o_year)).annotate(total=Sum('division_one'))

		rank = ExamRank.objects.filter(school__in=schools.values_list('id'))

		for e in f.qs:
			
			dv2T = (ExamResult.objects.filter(school=e.id, classe=4, year__range=(start_o_year,end_o_year)).aggregate(total=Sum('division_two')))

			dv3T = (ExamResult.objects.filter(school=e.id, classe=4, year__range=(start_o_year,end_o_year)).aggregate(total=Sum('division_three')))

			dv4T = (ExamResult.objects.filter(school=e.id, classe=4, year__range=(start_o_year,end_o_year)).aggregate(total=Sum('division_four')))

			dv0T = (ExamResult.objects.filter(school=e.id, classe=4, year__range=(start_o_year,end_o_year)).aggregate(total=Sum('division_zero')))

		

			# total_points = dv1T['total']*5.5 + dv2T['total']*1.5 + dv3T['total']*0.25 + dv4T['total']*-1.5 + dv0T['total']*-5.5

			# print('total_points',total_points)

	if 'exam_6_review' in request.GET:
		exam_6_review = request.GET.get('exam_6_review', '')
		start_a_year = (datetime.now() - timedelta(days=int(exam_6_review)*365)).year
		end_a_year = datetime.now().year

		print(start_a_year)
		print(end_a_year)

	context = {
		'filter': f,
		# 'total_points':total_points,
		'dv1T':dv1T,
		'rank':rank,

	}

	return render(request, 'main/school_list.html', context)



def homepage(request):

	school_qs = School.objects.order_by('-created_at')
	form = SchoolForm(use_required_attribute=False)


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
		print('school_subjects:',school_subjects)
		if school_subjects:
			school_qs = school_qs.filter(school_subjects=school_subjects)
			print('school_qs2:',school_qs)

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

		print('combination:', combination)
		if combination:
			school_qs = school_qs.filter(subject_combination__in=combination)
			print('sq:',school_qs)

	# if 'fee_from' and 'fee_to' in request.GET:
	# 	fee_from = request.GET.get('fee_from', 0)
	# 	fee_to = request.GET.get('fee_to', 50000000)
	# 	if fee_from and fee_to:
	# 		school_qs = school_qs.filter(average_tution_fee__gte=fee_from).filter(average_tution_fee__lte=fee_to)


	# if 'charity_support' in request.GET:
	# 		charity_support = request.GET.get('charity_support', 0)
	# 		print(charity_support)
	# 		if charity_support:
	# 			school_qs = school_qs.filter(no_fee=charity_support)
		


	print('school_qs:', school_qs)
	 
	subjects = SchoolSubject.objects.all()
	combination = SubjectCombination.objects.all()
	# print('school_subjects:',school_subjects)

	context = {
		'school_qs':school_qs,
		'values': request.GET,
		'subjects':subjects,
		'combinations':combination,
		'form':form,
	}

	template_name = 'main/index.html'

	
	return render(request, template_name, context)