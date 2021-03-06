#Modified after meeting on 20150411

from django.db import models

# Create your models here.
class Property(models.Model):
	Property_ID = models.CharField(max_length=15,primary_key=True)
	Price = models.DecimalField(max_digits=12,decimal_places=2)
	Bedroom_Number = models.SmallIntegerField()
	Bathroom_Number = models.SmallIntegerField()
	Address = models.CharField(max_length=30)
	City = models.CharField(max_length=35)
	Post_code = models.CharField(max_length=6)
	Description = models.TextField()
	Photo_link = models.URLField()
	#Photo_img = models.ImageField()
	MI_Build_Type  = models.CharField(max_length=1)
	MI_Land_Size = models.DecimalField(max_digits=8,decimal_places=2)
	MI_Land_Size_Unit = models.CharField(max_length=10)
	MI_Build_In = models.CharField(max_length=4)
	MI_Storeys_Number = models.SmallIntegerField()
	MI_Municipal_Assessment  = models.DecimalField(max_digits=12,decimal_places=2)
	CD_Garage_Flag = models.BooleanField()
	CD_Metro_Flag = models.BooleanField()
	CD_Highway_Flag = models.BooleanField()
	CD_Communicty_Center_F = models.BooleanField()
	CD_Culture_Center_F = models.BooleanField()
	CD_Shopping_Mall_Flag = models.BooleanField()
	CD_PARK_Hospital_Flag = models.BooleanField()
	CD_School_Flag = models.BooleanField()
	#Agent_ID  = models.CharField(max_length=10)
	Broker_ID = models.ForeignKey('Broker')
	timestamp = models.DateTimeField(auto_now_add = True)
	#Status  = models.CharField(max_length=1)

class Broker(models.Model):
	Broker_ID = models.CharField(max_length=8,primary_key=True) 
	Company_ID = models.CharField(max_length=8)
	Company_Name = models.CharField(max_length=30)
	Broker_Name = models.CharField(max_length=30)
	Company_Address = models.CharField(max_length=30)
	Company_City = models.CharField(max_length=35)
	Company_Post_Code = models.CharField(max_length=6)
	Broker_Phone = models.CharField(max_length=11) 
	Broker_Email = models.EmailField(max_length=50)

class PropertyStatus(models.Model):
	Property_ID = models.CharField(max_length=15,primary_key=True)
	#Property_ID = models.ForeignKey('Property')
	Offer_Flag = models.BooleanField()
	Offer_date = models.DateField(auto_now_add = False)
	Offer_price = models.DecimalField(max_digits=12,decimal_places=2)
	Sold_Flag = models.BooleanField()
	Sold_Date = models.DateField(auto_now_add = False)
	Sold_Price = models.DecimalField(max_digits=12,decimal_places=2)