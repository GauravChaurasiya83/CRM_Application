from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add = True)

    first_name = models.CharField(max_length = 100)

    last_name = models.CharField(max_length = 100)

    email = models.CharField(max_length = 250)

    phone_number = models.CharField(max_length = 30)

    address = models.CharField(max_length = 200)

    province = models.CharField(max_length = 200)

    country = models.CharField(max_length = 200)


    def __str__(self):

        return self.first_name + "   " + self.last_name



