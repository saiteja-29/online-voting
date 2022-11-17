from django.db import models

# Create your models here.
class feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    
class Poll(models.Model):
    question=models.TextField()
    
    option_one=models.CharField(max_length=30)
    option_two=models.CharField(max_length=30)
    option_three=models.CharField(max_length=30)
    option_four=models.CharField(max_length=30)
    
    option_one_count=models.IntegerField(default=0)
    option_two_count=models.IntegerField(default=0)
    option_three_count=models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)
    
    def total(self):
        return self.option_one_count+self.option_two_count+self.option_three_count
    
class Feedback(models.Model):
    feedback=models.TextField()