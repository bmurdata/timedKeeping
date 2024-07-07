# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.backends import BaseBackend
#from . import extras

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=97)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

class OurBackend(BaseBackend):
    def authenticate(self, request, username, password):
        assert(None not in [username, password])
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        pwrd_valid = extras.check_password(user, password)
        if pwrd_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# Employees have title, IDs, Name, etc
class Employees(models.Model):
    emplID= models.AutoField(primary_key=True)
    internalID=models.IntegerField()
    externalID=models.IntegerField()
    prefix=models.CharField(max_length=10)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    titleCode=models.ForeignKey('api.Titles',on_delete=models.DO_NOTHING)
    HireDate=models.DateField()
    Status=models.CharField(max_length=256)
    JobNum=models.ForeignKey('api.Jobs',on_delete=models.DO_NOTHING)

class Titles(models.Model):
    titleCode=models.CharField(max_length=20,primary_key=True)
    Level=models.CharField(max_length=2)
    Salary=models.FloatField()
    PromotesTo=models.IntegerField()
    EmployeeType=models.CharField(max_length=100)

class Balances(models.Model):
    balanceCode=models.CharField(max_length=10)
    emplID=models.ForeignKey('api.Employees',on_delete=models.DO_NOTHING)
    Amount=models.IntegerField()
    Type=models.CharField(max_length=100)
    BalanceComment=models.CharField(max_length=500)

# Link to Absence or OT entry, 
# Subtracts or adds to Balances as needed
class Balance_Transactions(models.Model):
    balanceCode=models.ForeignKey('api.Balances',on_delete=models.DO_NOTHING)
# Jobs are the internal IDs, correspond 
# to tasks or roles filled by Employees of Titles
class Jobs(models.Model):
    jobNum=models.CharField(primary_key=True,max_length=20)
    EligibleTitles=models.ForeignKey('api.Titles',on_delete=models.DO_NOTHING)
    Location=models.CharField(max_length=256)
    JobType=models.CharField(max_length=256)
    AssignedBy=models.ForeignKey('api.Employees',on_delete=models.DO_NOTHING)
    Flag=models.CharField(max_length=1000)
    Note=models.CharField(max_length=500)

# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50, unique=True)
#     product_image_path = models.CharField(max_length=100, unique=True)
#     recommended_price = models.IntegerField()
#     description = models.CharField(max_length=250)

# class Card(models.Model):
#     id = models.AutoField(primary_key=True)
#     data = models.BinaryField(unique=True)
#     product = models.ForeignKey('api.Product', on_delete=models.CASCADE, default=None)
#     amount = models.IntegerField()
#     fp = models.CharField(max_length=100, unique=True)
#     user = models.ForeignKey('api.User', on_delete=models.CASCADE)
#     used = models.BooleanField(default=False)
