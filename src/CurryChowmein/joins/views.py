# from django.conf import settings
# from django.shortcuts import render, HttpResponseRedirect, Http404

# # Create your views here.
# from .forms import EmailForm, JoinForm
# from .models import Join


# #str(user_id)[:11].replace('-', '').lower()
# import uuid

# def get_ref_id():
# 	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
# 	#ref_id = '9f16a22615'
# 	try:
# 		id_exists = Join.objects.get(ref_id=ref_id)
# 		get_ref_id()
# 	except:
# 		return ref_id



# def share(request, ref_id):
# 	#print ref_id
# 	try:
# 		join_obj = Join.objects.get(ref_id=ref_id)
# 		friends_referred = Join.objects.filter(friend=join_obj)
# 		count = join_obj.referral.all().count()
# 		ref_url = settings.SHARE_URL + str(join_obj.ref_id)

# 		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
# 		template = "share.html"
# 		return render(request, template, context)
# 	except:
# 		raise Http404



# def home(request):
# 	try:
# 		join_id = request.session['join_id_ref']
# 		obj = Join.objects.get(id=join_id)
# 	except:
# 		obj = None

# 	form = JoinForm(request.POST or None)
# 	if form.is_valid():
# 		new_join = form.save(commit=False)
# 		email = form.cleaned_data['email']
# 		new_join_old, created = Join.objects.get_or_create(email=email)
# 		new_join.save()
# 		# if created:
# 		# 	new_join_old.ref_id = get_ref_id()
# 		# 	# add our friend who referred us to our join model or a related
# 		# 	if not obj == None:
# 		# 		new_join_old.friend = obj
# 		# 	new_join_old.ip_address = get_ip(request)
# 		# 	new_join_old.save()
		
# 		#print all "friends" that joined as a result of main sharer email
# 		#print Join.objects.filter(friend=obj).count()
# 		#print obj.referral.all().count()

# 		#redirect here
# 		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

# 	context = {"form": form}
# 	template = "home.html"
# 	return render(request, template, context)





























#-----------------------------------------------------#
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
# from django.core.mail import send_mail


# Create your views here.

from .forms import EmailForm, JoinForm
from .models import Join




def home(request):

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join, created = Join.objects.get_or_create(email=email)
		# message = 'Thank you for signing up. We will be in touch!'
		# new_join.save()
	 	
		# sent = send_mail('New Sign Up', str(new_join.email) + 'has signed up',
		# 				['karan.mkkr@gmail.com'],[new_join.email], fail_silently = True)
		#return render_to_response('form.html',{'message':message},context_instance=RequestContext(request))

	context = {"form": form}
	template = "home.html"
	return	render(request, template, context)




	#print request.META.get("REMOTE_ADDRESS")
	#print request.POST["email"]


	#This is using Regular Django forms
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print new_join, created
	# 	print new_join.timestamp
	# 	if created:
	#		print "This obj was created"

	#this is using Model Form
	

# def home2(request):
# 	form = EmailForm()
# 	context = {"form": form}
# 	template = "home2.html"
# 	return	render(request, template, context)