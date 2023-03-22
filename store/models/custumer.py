from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    #salvar a data
    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False