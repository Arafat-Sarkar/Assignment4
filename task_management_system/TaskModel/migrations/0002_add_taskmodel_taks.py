# Generated by Django 4.2.7 on 2023-12-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCategory', '0002_remove_addcategory_tasks'),
        ('TaskModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_taskmodel',
            name='taks',
            field=models.ManyToManyField(to='TaskCategory.addcategory'),
        ),
    ]
