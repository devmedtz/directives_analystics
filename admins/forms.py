from django import forms
from django.forms.formsets import formset_factory

from main.models import School, SchoolExamResult
from location.models import Region, District

class SchoolForm(forms.ModelForm):
	region = forms.ModelChoiceField(Region.objects.all(), empty_label='Select Region')

	class Meta:
		model = School
		exclude = ['created_at', 'modified_at', 'created_by', ]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['district'].queryset = District.objects.none()

		if 'region' in self.data:
			try:
				region_id = int(self.data.get('region'))
				self.fields['district'].queryset = District.objects.filter(region=region_id).order_by('id')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['district'].queryset = self.instance.region.district_set.order_by('id')


class SchoolExamResultForm(forms.ModelForm):

	class Meta:
		model = SchoolExamResult
		fields = ['year', 'division_one', 'division_two', 'division_three', 'division_four', 'division_zero',]

SchoolExamResultFormSet = formset_factory(SchoolExamResultForm, extra=0)

SchoolExamResultInlineFormSet = forms.inlineformset_factory(School, SchoolExamResult, fields = ('id','year', 'division_one', 'division_two', 'division_three', 'division_four', 'division_zero',), extra=1)