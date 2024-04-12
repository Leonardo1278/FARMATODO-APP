# Generated by Django 5.0.2 on 2024-02-26 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DimSection',
            fields=[
                ('id_section', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=40)),
                ('location_address', models.CharField(max_length=80)),
                ('manager_name', models.CharField(max_length=50)),
                ('manager_tel', models.CharField(max_length=20)),
                ('main_section', models.CharField(max_length=20)),
                ('inner_section', models.CharField(max_length=40)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id_report', models.AutoField(primary_key=True, serialize=False)),
                ('signature', models.ImageField(blank=True, null=True, upload_to='signatures/')),
                ('report_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralData',
            fields=[
                ('incidence_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=255)),
                ('main_section', models.CharField(max_length=255)),
                ('inner_section', models.CharField(max_length=255)),
                ('photo_1', models.CharField(blank=True, max_length=255, null=True)),
                ('photo_2', models.CharField(blank=True, max_length=255, null=True)),
                ('photo_3', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('urgency', models.CharField(max_length=15)),
                ('registro_fecha_hora', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_data_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'general_data',
            },
        ),
        migrations.CreateModel(
            name='FactIncidences',
            fields=[
                ('id_incidence', models.AutoField(primary_key=True, serialize=False)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('incidence_date', models.DateTimeField(auto_now_add=True)),
                ('descrip', models.CharField(max_length=100)),
                ('urgency', models.BooleanField(default=False)),
                ('id_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidences', to='incidencias.dimsection')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidences', to='incidencias.report')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim_sections', models.ManyToManyField(blank=True, to='incidencias.dimsection')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
