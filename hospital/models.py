from django.db import models
import json





# Create your models here.
class Hosp(models.Model):
    name = models.CharField(max_length=100, default="")
    speciality = models.CharField(max_length=100, default="")
    costWard = models.IntegerField(default=0)
    typeGP = models.BooleanField()
    rating = models.IntegerField(default=0)
    contact = models.CharField(max_length=50, default="")
    covid = models.BooleanField()
    availableBeds=models.IntegerField(default=0)
    timings=models.CharField(max_length=100, default="")
    pincode=models.IntegerField(default=0)
    army = models.BooleanField()
    state = models.CharField(max_length=50, default="")
    district = models.CharField(max_length=50, default="")
    
    


    def getHospitalsAsPerQuery(request):
        # items = Hosp.objects.values()
        # data = list(items)
        # response = json.dumps(data)

        # print("this is the request : ", request.GET)
        # print(bool(request.GET))

        all_hospitals = Hosp.objects.values()

        # print(all_hospitals)

        
        if(request.GET):
            # print("its false")  
            for i in request.GET:

                # print(i, type(i))
                # print(request.GET.get(i))

                demo=request.GET.get(i)

                if i=="covid" or i=="typeGP" or i=="army":
                    if demo == 'true':
                        demo = True
                    else:
                        demo = False
                
                model_cri = {i:demo}
                # print(type(request.GET.get(i)))
                all_hospitals = all_hospitals.filter(**model_cri)

                # print(all_hospitals)        

        return json.dumps(list(all_hospitals))


    # image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.name

