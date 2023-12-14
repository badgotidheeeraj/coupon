# Generated by Django 4.2.6 on 2023-12-14 11:56

import core.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[core.models.no_email_validation], verbose_name='email address')),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('is_expert', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, max_length=1000, null=True, verbose_name='About Yourself')),
                ('area', models.CharField(blank=True, max_length=50, null=True, verbose_name='Area')),
                ('domain', models.CharField(blank=True, max_length=50, null=True, verbose_name='Domain')),
                ('whatsApp_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='WhatsApp No')),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone No')),
                ('phone_same_as_whatsapp', models.BooleanField(blank=True, default=False, verbose_name='Phone No same as WhatsApp No')),
                ('email_is_verified', models.BooleanField(blank=True, default=False, verbose_name='Email Verified')),
                ('phone_is_verified', models.BooleanField(blank=True, default=False, verbose_name='Phone Verified')),
                ('whatsApp_no_is_verified', models.BooleanField(blank=True, default=False, verbose_name='WhatsApp No Verified')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Address')),
                ('userAccount', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Link a User Account')),
            ],
        ),
    ]
