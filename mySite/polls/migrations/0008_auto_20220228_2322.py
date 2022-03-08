# Generated by Django 3.2.7 on 2022-02-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20220228_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='is_admin',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
