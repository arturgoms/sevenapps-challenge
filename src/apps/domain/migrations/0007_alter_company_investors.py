# Generated by Django 4.0.4 on 2022-10-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0006_alter_company_founding_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='investors',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Investors'),
        ),
    ]
