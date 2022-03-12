# Generated by Django 4.0.2 on 2022-03-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(default='', max_length=30)),
                ('mobile', models.CharField(default='', max_length=30)),
                ('Refered', models.CharField(default='NA', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.CharField(default='', max_length=30, null=True)),
                ('name', models.CharField(default='', max_length=300, null=True)),
                ('location', models.CharField(default='', max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('answer', models.TextField(blank=True, max_length=2000)),
                ('answer_set', models.TextField(blank=True, default='', max_length=2000)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hirementor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(default='', max_length=30, null=True)),
                ('mobile', models.CharField(default='', max_length=30, null=True)),
                ('area', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Mobileno', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=100)),
                ('Profession', models.CharField(blank=True, default='', max_length=200)),
                ('Mentor_Img', models.ImageField(blank=True, default='', upload_to='')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Primemember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Mobileno', models.CharField(max_length=50)),
                ('Refered', models.CharField(default='', max_length=20)),
                ('Plan', models.CharField(default='', max_length=20)),
                ('Query', models.CharField(default='', max_length=100)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.CharField(default='', max_length=30, null=True)),
                ('name', models.CharField(default='', max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_by', models.CharField(max_length=100)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=100)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transcatid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('transcation_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]
