from django import forms
from django.forms import RadioSelect

from main.models import School
from location.models import Region, District


class HorizontalRadioSelect(RadioSelect):
	template_name = 'admin/horizontal_radios.html'
	option_template_name = 'admin/horizontal_option.html'


GENDER = (
	('Boys', 'Boys'),
	('Girls', 'Girls'),
	('Co-ed/boys and girls', 'Co-ed/boys and girls'),
)

class FilterForm(forms.Form):
	gender = forms.ChoiceField(choices=GENDER, label='test', widget=HorizontalRadioSelect())


class SchoolForm(forms.ModelForm):
	region = forms.ModelChoiceField(Region.objects.all(), empty_label='Select Region',required=False)
	district = forms.ModelChoiceField(District.objects.none(), empty_label='Select District',required=False)

	class Meta:
		model = School
		fields = ['region','district',]

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