#Modified after meeting on 20150411

from django.shortcuts import render
from .ccm_forms import SearchForm
from .ccm_forms import PInfoForm
from .models import Property
from .models import Broker
from .models import PropertyStatus
from cgi import parse_qs
from datetime import date
from datetime import timedelta

# Create your views here.
def PostAdvertise(request):
	form = PInfoForm(request.POST or None)	
	context = {"form":form}
	template= "ccm/ccm_home.html"

	if form.is_valid():
		new_property = form.save(commit=True)
		Property_ID = form.cleaned_data['Property_ID']
		new_property_old,created = Property.objects.get_or_create(Property_ID=Property_ID)
		#context = {}
		Properties = Property.objects.all()	
		context = {'Properties':Properties}
		template= "ccm/ccm_SearchResult.html"
		#new_property.save()
	 	if(created is True):
			print "this object is created"

	return render(request,template,context)

def SearchProperty(request):
	form = SearchForm(request.POST or None)
	if form.is_valid():
		region =  form.cleaned_data['Region']
		bedroom =  form.cleaned_data['Bedroom']
		bathroom =  form.cleaned_data['Bathroom']
		lowerPrice =  form.cleaned_data['LowerPrice']
		upperPrice =  form.cleaned_data['UpperPrice']
		convenientPoint =  form.cleaned_data['ConvenientPoint']

	context = {"form":form}
	template= "ccm/ccm_search.html"
	return render(request,template,context)


def SearchResult(request):
	region = request.POST['Region']
	bedroom = request.POST['Bedroom']
	bathroom = request.POST['Bathroom']
	lowerPrice = request.POST['LowerPrice']
	upperPrice = request.POST['UpperPrice']
	convenientPoint = request.POST['ConvenientPoint']

	#print form.is_valid()

	try:
		a_15d = date.today()-timedelta(days=15)
		print a_15d
		soldout_a_15d_list = PropertyStatus.objects.filter(Sold_Flag = True, Sold_Date__lt=a_15d).values_list('Property_ID')
		#print soldout_a_15d_list
		Properties = Property.objects.exclude(Property_ID__in = soldout_a_15d_list)

		if len(region) > 0:
			Properties = Property.objects.filter(City = region)	   
		if len(bedroom) > 0:
			Properties = Properties.filter(Bedroom_Number = bedroom)	   
		if len(bathroom) > 0:
			Properties = Properties.filter(Bathroom_Number = bathroom)	    
		if len(lowerPrice) > 0:
			Properties = Properties.filter(Price__gte=lowerPrice)	   
		if len(upperPrice) > 0:
			Properties = Properties.filter(Price__lte=upperPrice)	

	except Property.DoesNotExist:
		return HttpResponseRedirect('/')
	context = {'Properties':Properties}
	template= "ccm/ccm_SearchResult.html"
	return render(request,template,context)


def DisplayProperty(request,propertyID):
	a_property = Property.objects.get(Property_ID=propertyID)
	a_broker = Broker.objects.get(Broker_ID=a_property.Broker_ID.Broker_ID)

	a_3d = date.today()-timedelta(days=3)
	strStatus = ''

	try:
		a_property_status=PropertyStatus.objects.get(Property_ID=propertyID)
		if(a_property_status.Sold_Flag):
			strStatus = 'sold out on ' + unicode(a_property_status.Sold_Date)
		elif(a_property_status.Offer_Flag and a_property_status.Offer_date>= a_3d):
			strStatus = 'offered on ' + unicode(a_property_status.Offer_date)
		else:
			strStatus = 'Available'
	except PropertyStatus.DoesNotExist:
		strStatus = 'Available'

	context = {'AProperty': a_property,'A_broker':a_broker,'strStatus':strStatus}
	template= "ccm/ccm_PropertyInfo.html"
	return render(request,template,context)

