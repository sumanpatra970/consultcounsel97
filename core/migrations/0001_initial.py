# Generated by Django 4.0.2 on 2022-03-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=90)),
                ('Email', models.CharField(blank=True, default='', max_length=50)),
                ('Amount', models.IntegerField(default=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Mobileno', models.CharField(blank=True, default='', max_length=100)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=30)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Query', models.CharField(default='', max_length=500)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='free_sessionform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.CharField(default='', max_length=30, null=True)),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('field', models.CharField(default='', max_length=30, null=True)),
                ('doubt', models.CharField(default='', max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.CharField(default='', max_length=30, null=True)),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('field', models.CharField(default='', max_length=30, null=True)),
                ('cv', models.FileField(blank=True, upload_to='cv')),
            ],
        ),
    ]