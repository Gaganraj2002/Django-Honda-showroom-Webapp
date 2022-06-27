from django.db import models

# Create your models here.


class Staff(models.Model):
    Staffname = models.CharField(max_length=20)
    Staffid = models.IntegerField(primary_key=True)
    Address = models.CharField(max_length=20)
    PanCard = models.CharField(max_length=20)
    AdharcardNo = models.CharField(max_length=20)
    Phno = models.IntegerField()
    mail = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)


class Vehicle(models.Model):
    VehicleType = models.CharField(max_length=20)
    VehicleNo = models.IntegerField(primary_key=True)
    Company = models.CharField(max_length=20)


class VehicleDetails(models.Model):
    VehicleNo = models.OneToOneField(
        Vehicle, on_delete=models.CASCADE, primary_key=True)
    VehicleName = models.CharField(max_length=20)
    VehiclePrice = models.IntegerField()
    VehicleDesc = models.CharField(max_length=100)
    VehicleImg = models.ImageField(upload_to="showroom\static\images")


class Stock(models.Model):
    Stock = models.IntegerField()
    VehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Stockid = models.IntegerField(primary_key=True)


class Bookingbystaff(models.Model):
    Bookingid = models.IntegerField(primary_key=True)
    Stockid = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Staffid = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Customer(models.Model):
    Custname = models.CharField(max_length=20)
    Custid = models.IntegerField(primary_key=True)
    Address = models.CharField(max_length=20)
    PanCard = models.CharField(max_length=20)
    AdharcardNo = models.CharField(max_length=20)
    Phno = models.IntegerField()
    mail = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)


class Bookingbycustomer(models.Model):
    Bookingid = models.IntegerField(primary_key=True)
    Stockid = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Custid = models.ForeignKey(Customer, on_delete=models.CASCADE)


class feedback(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Feedback = models.TextField()
