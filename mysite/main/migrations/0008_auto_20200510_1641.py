# Generated by Django 3.0.3 on 2020-05-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200510_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(max_length=200),
        ),
    ]
