from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

class DimSection(models.Model):
    id_section = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=40)
    location_address = models.CharField(max_length=80)
    manager_name = models.CharField(max_length=50)
    manager_tel = models.CharField(max_length=20)
    main_section = models.CharField(max_length=20)
    inner_section = models.CharField(max_length=40)
    region = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.location_name} - {self.main_section} - {self.inner_section}"


class Report(models.Model):
    id_report = models.AutoField(primary_key=True)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id_report} - {self.report_date.strftime('%Y-%m-%d')}"

class FactIncidences(models.Model):
    id_incidence = models.AutoField(primary_key=True)
    id_section = models.ForeignKey(DimSection, on_delete=models.CASCADE, related_name="incidences")
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="incidences", default=1)
    photo_1 = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/', blank=True, null=True)
    incidence_date = models.DateTimeField(default=timezone.now)
    descrip = models.CharField(max_length=100)
    urgency = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"{self.id_incidence}: {self.descrip} - Urgency: {'High' if self.urgency else 'Low'}"


class GeneralData(models.Model):
    incidence_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)
    main_section = models.CharField(max_length=255)
    inner_section = models.CharField(max_length=255)
    photo_1 = models.CharField(max_length=255, blank=True, null=True)
    photo_2 = models.CharField(max_length=255, blank=True, null=True)
    photo_3 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    urgency = models.CharField(max_length=15)
    registro_fecha_hora = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="general_data_set", null=True)
    class Meta:
        db_table = 'general_data'

        


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dim_sections = models.ManyToManyField(DimSection, blank=True)  # Cambiado a ManyToManyField
    # otros campos necesarios para el perfil del usuario

    def __str__(self):
        sections = ', '.join([section.location_name for section in self.dim_sections.all()])
        return f"{self.user.username} - Sections: {sections}"
