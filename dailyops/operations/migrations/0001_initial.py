# Generated by Django 2.2.2 on 2019-06-07 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('departments', models.CharField(choices=[('TECH', 'Tech'), ('MLAB', 'Mlab'), ('ACADAMY', 'Acadamy')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('info_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='operations.Info')),
                ('operation', models.CharField(choices=[('U', 'Utensil'), ('H', 'HALL')], max_length=1)),
            ],
            bases=('operations.info',),
        ),
    ]
