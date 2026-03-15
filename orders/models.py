from django.db import models


class Facility(models.Model):
    FACILITY_TYPE = [
        ('hospital','Hospital'),
        ('clinic','Wound Care Clinic'),
        ('research','Research Institution'),
    ]

    name = models.CharField(max_length=200)
    facility_type = models.CharField(max_length=20, choices=FACILITY_TYPE)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class HealthcareProvider(models.Model):

    ROLE_CHOICES = [
        ('nurse','Wound Care Nurse'),
        ('mo','Medical Officer'),
        ('co','Clinical Officer'),
        ('surgeon','Surgeon'),
        ('researcher','Researcher')
    ]

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MaggotOrder(models.Model):

    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    provider = models.ForeignKey(HealthcareProvider, on_delete=models.CASCADE)

    wound_type = models.CharField(max_length=200)
    wound_size = models.CharField(max_length=50)
    urgency = models.CharField(max_length=50)

    larvae_units = models.IntegerField()

    application_type = models.CharField(max_length=50)

    delivery_date = models.DateField()

    notes = models.TextField(blank=True)

    contact_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.facility}"