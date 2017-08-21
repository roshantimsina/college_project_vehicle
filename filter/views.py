from django.shortcuts import render
from browse.models import Browse

from .filters import BrowseFilter

# Create your views here.
def browsefilter(request):
	browse_list = Browse.objects.all()
	browse_filter = BrowseFilter(request.GET, queryset=browse_list)
	return render(request, 'browse_filter.html',{'filter':browse_filter})
