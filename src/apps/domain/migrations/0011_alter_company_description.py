# Generated by Django 4.0.4 on 2022-10-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0010_alter_company_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Description'),
        ),
    ]