# Generated by Django 4.2.7 on 2023-12-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0012_placed_studdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdb',
            name='Pancard',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentdb',
            name='adhaar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]