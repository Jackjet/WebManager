# Generated by Django 2.1.5 on 2019-01-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0007_auto_20190129_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policycard',
            name='policy_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='政策编号'),
        ),
    ]
