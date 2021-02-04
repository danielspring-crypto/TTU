from django.db import models

# Create your models here.
class ချိုးဖောက်မှုပုဒ်မများ(models.Model):
    ပုဒ်မ = models.CharField(max_length=255)
    အကြောင်းအရာ = models.TextField()
    ကျူးလွန်သည့်အကြောင်းအရာ = models.TextField()

    def __str__(self):
        return self.ပုဒ်မ

class အချက်အလက်များ(models.Model):
    အကြောင်းအရာ = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    image = models.ImageField(upload_to='data')

    def __str__(self):
        return self.အကြောင်းအရာ

class ထောက်ခံချက်များ(models.Model):
    image = models.ImageField(upload_to='thumbs_up')
        