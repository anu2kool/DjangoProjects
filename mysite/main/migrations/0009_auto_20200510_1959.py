# Generated by Django 3.0.3 on 2020-05-10 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200510_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TutorialCategory', verbose_name='Categories'),
        ),
    ]
