from django.db import models

# Create your models here.

class Contacts(models.Model):
    con_name =models.CharField(max_length=255)
    con_email = models.EmailField(max_length=255)
    con_message =models.TextField()
    def __str__(self):
        return self.con_name
    
class Course(models.Model):
    cou_name = models.CharField(max_length=255)
    cou_image =models.FileField(null=True,upload_to="course")
    cou_price = models.IntegerField(null=True)
    cou_text = models.TextField(null=True)
    cou_descri = models.TextField(null=True)
    course_user=models.CharField(null=True,max_length=255)
 
    def __str__(self):
        return self.cou_name
    
class Registration(models.Model):
    reg_email = models.EmailField(max_length=255)
    reg_password = models.CharField(max_length=255)
    reg_username = models.CharField(max_length=255)
    reg_phnum = models.CharField(max_length=255)
   
    def __str__(self):
        return self. reg_username
    
class Reviews(models.Model):
    rev_name = models.CharField(max_length=255)
    rev_img = models.FileField(null=True,upload_to="student")
    rev_text = models.TextField(null=True)


class Order(models.Model):
    order_user = models.CharField(max_length=250,default=None)
    order_name = models.CharField(max_length=250)
    order_price = models.FloatField(null=True)
    order_image = models.FileField(null=True)
    # order_qty = models.IntegerField()
    # order_amount = models.FloatField()
    order_address = models.TextField(null=True)
    order_dlvtype = models.CharField(null=True,max_length=10)
    order_status = models.IntegerField(default=0)
    def __str__(self):
        return self. order_name
    
class Wishlist(models.Model):
    wish_user = models.CharField(max_length=250,null=True)
    wish_proid = models.IntegerField(null=True)
    wish_name = models.CharField(max_length=250)
    wish_price = models.FloatField(null=True)
    wish_image = models.FileField(null=True)
    def __str__(self):
        return self.wish_name


class Dashregistration(models.Model):
   
    dash_password = models.CharField(max_length=255)
    dash_username = models.CharField(max_length=255)

    def __str__(self):
        return self. dash_username
    
    