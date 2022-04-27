from django.db import models
from datetime import datetime, timedelta
from .utils import *
# Create your models here.
class PrsignUp(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField()
    password = models.CharField(default='', max_length=15)
    confirmPassword = models.CharField(default='', max_length=15)
    link=models.CharField(max_length=55,default='')
    # recommend_by=models.ForeignKey(CasignUp,on_delete=models.CASCADE,null=True,blank=True)
    recommend_by=models.CharField(max_length=30,default='',blank=False)
    payment_due_date = models.DateField(default=datetime.now()+timedelta(days=15))
    
    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
        code=genrated_ref_code()
        self.link="http://127.0.0.1:8000/prsignup/"+str(code)
        super().save(*args,**kwargs)         

class CasignUp(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField()
    password = models.CharField(default='', max_length=15)
    confirmPassword = models.CharField(default='', max_length=15)
    link=models.CharField(max_length=55,default='')
    payment_due_date = models.DateField(default=datetime.now()+timedelta(days=15))
    subuser=models.ForeignKey(PrsignUp,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
        code=genrated_ref_code()
        self.link="http://127.0.0.1:8000/prsignup/"+str(code)
        super().save(*args,**kwargs)    


class ContactForm(models.Model):
    fname = models.CharField(max_length=30, default='')
    lname = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField(default='')
    details = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.fname
    
    
class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
<<<<<<< HEAD
        ordering = ('date_added',)
        
=======
        ordering = ('date_added',)
>>>>>>> 1f48c6b25ae716c12ffe748fb8de316323967623
