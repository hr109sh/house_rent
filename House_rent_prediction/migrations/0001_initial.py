# Generated by Django 2.0.5 on 2019-06-29 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City_selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State_selection',
            fields=[
                ('state_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='city_selection',
            name='state_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='House_rent_prediction.State_selection'),
        ),
    ]
