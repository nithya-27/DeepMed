# Generated by Django 4.2.14 on 2024-08-21 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField()),
                ('Gender', models.IntegerField()),
                ('Polyuria', models.CharField(max_length=10)),
                ('Polydipsia', models.CharField(max_length=10)),
                ('sudden_weight_loss', models.CharField(max_length=10)),
                ('weakness', models.CharField(max_length=10)),
                ('Polyphagia', models.CharField(max_length=10)),
                ('Genital_thrush', models.CharField(max_length=10)),
                ('visual_blurring', models.CharField(max_length=10)),
                ('Itching', models.CharField(max_length=10)),
                ('Irritability', models.CharField(max_length=10)),
                ('delayed_healing', models.CharField(max_length=10)),
                ('partial_paresis', models.CharField(max_length=10)),
                ('muscle_stiffness', models.CharField(max_length=10)),
                ('Alopecia', models.CharField(max_length=10)),
                ('Obesity', models.CharField(max_length=10)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('label', models.CharField(default='data', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
