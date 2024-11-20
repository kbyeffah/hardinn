# Generated by Django 5.1.1 on 2024-11-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='ProductImages/')),
                ('quantity', models.IntegerField()),
                ('code', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]