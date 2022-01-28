from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core import serializers
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
@csrf_exempt
def idHospital(request,myid):
    # print(myid, '...............................')
    # items = Hosp.objects.filter(pk=myid)
    ###items = Hosp.objects.get(id=myid)
    # print(items, type(items))
    # print(items, type(items))
    ###response = serializers.serialize("json", [items, ])
    # response = json.dumps(list(items))
    # return HttpResponse(response, content_type="application/json")
    item = False
    try:
        item = Hosp.objects.get(id = myid)
    except Hosp.DoesNotExist:
        item = None
    if item != None:
        if request.method == 'GET':
            return getHospitalById(request, myid)
        elif request.method == 'PUT':
            return editHospitalById(request, myid)
        elif request.method == 'DELETE':
            return deleteHospitalById(request, myid)
    else:
        return HttpResponseNotFound("Data Doesn't Exist")

@csrf_exempt
def getHospitalById(request, myid):
    # print("get hospital by id is executed.................")
    item = Hosp.objects.values().filter(id=myid)
    response = json.dumps(list(item))
    # print(item, type(item))
    # response = serializers.serialize("json", [item, ])
    return HttpResponse(response, content_type="application/json")

"""
we need to check into the reponse of the below two methods as described in the 
schema. There nothing is mentioned about the response.
"""

@csrf_exempt
def editHospitalById(request, myid):
    print("edit hospital by id is executed...................")
    item = Hosp.objects.values().filter(id=myid)
    response = json.dumps(list(item))
    return HttpResponse(response, content_type="application/json")

@csrf_exempt
def deleteHospitalById(request, myid):
    print("delete hospital by id is executed...................")
    item = Hosp.objects.values().filter(id=myid)
    response = json.dumps(list(item))
    Hosp.objects.get(id = myid).delete()
    # here the deleted hospital is being returned which is not specified in the schema
    return HttpResponse(response, content_type="application/json")
