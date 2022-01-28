from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def pathHospital(request):
    if(request.method == 'GET'):
        return listHospitals(request)
    else:
        return addHospital(request)


def listHospitals(request):
    # print(request)
    # items = Hosp.objects.values()
    # data = list(items)
    # response = json.dumps(data)
    response = Hosp.getHospitalsAsPerQuery(request)
    return HttpResponse(response, content_type="application/json", status=201)



@csrf_exempt
def addHospital(request):
    # print("..................the post request is reaching here...............")
    # print(request.body)
    # print("......................................................")
    # print(json.loads(request.body))
    # print("......................................................")
    # print(type(json.loads(request.body)))
    # print(".......................................................")

    # name = request.POST.get('name', '')
    # speciality = request.POST.get('speciality', '')
    # costWard = request.POST.get('costWard', '')
    # rating = request.POST.get('rating', '')
    # typeGP = request.POST.get('typeGP', '')
    # contact = request.POST.get('contact', '')
    # covid = request.POST.get('covid', '')
    # army = request.POST.get('army', '')
    # availableBeds = request.POST.get('availableBeds', '')
    # state = request.POST.get('state', '')
    # district = request.POST.get('district', '')
    # pincode = request.POST.get('pincode', '')
    # timings = request.POST.get('timings', '')
    
    received_json_data=json.loads(request.body)
    # Hospital = Hosp(name=name,speciality=speciality,costWard=costWard,rating =rating , typeGP=typeGP, contact=contact,covid=covid,army=army,availableBeds=availableBeds,state=state,district=district,pincode=pincode,timings=timings)
    Hospital = Hosp(**received_json_data)
    Hospital.save()
    response = json.dumps(received_json_data)
    return HttpResponse(response, content_type="application/json", status=201)

# This is not yet finalised 
def getHospitalbyid(request,myid):
    items = Hosp.objects.get(pk=myid)
    response = json.dumps(list(items))
    return HttpResponse(response, content_type="application/json")
