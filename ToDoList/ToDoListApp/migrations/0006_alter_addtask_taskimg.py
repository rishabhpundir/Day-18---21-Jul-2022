# Generated by Django 3.2.4 on 2022-07-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListApp', '0005_alter_addtask_taskimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='TaskImg',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]