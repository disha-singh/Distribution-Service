# Generated by Django 3.0.8 on 2020-07-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_merge_20200726_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributioncentre',
            name='administrator',
        ),
        migrations.RemoveField(
            model_name='fooddonation',
            name='distributionCentre',
        ),
        migrations.RemoveField(
            model_name='fooddonation',
            name='donatedFood',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pin',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='clothDonation',
        ),
        migrations.DeleteModel(
            name='DistributionCentre',
        ),
        migrations.DeleteModel(
            name='foodDonation',
        ),
    ]