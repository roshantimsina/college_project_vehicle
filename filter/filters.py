from browse.models import Browse 

import django_filters


class BrowseFilter(django_filters.FilterSet):

	class Meta:
		model = Browse 
		fields = ['vehicle_type','source','destination','vehicle_name',]
