import json
import os
import random
import time
from dotenv import load_dotenv
from datetime import date, datetime, timedelta

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Command(BaseCommand):
    help = "Seed the database's permissions"

    def handle(self, *args, **options):
        run_seed()
        self.stdout.write("Finished data seeding.")

def create_groups():
    password = make_password("12345")
    admin, created = User.objects.get_or_create(
        username = 'admin',
        defaults = {
            'first_name' : 'admin',
            'last_name' : 'admin',
            'email' : os.getenv('ADMIN_EMAIL'),
            'password' : password
        }
    )

    admin2, created = User.objects.get_or_create(
        username = 'admin2',
        defaults = {
            'first_name' : 'admin2',
            'last_name' : 'admin2',
            'email' : os.getenv('ADMIN_EMAIL'),
            'password' : password
        }
    )

    anon, created = User.objects.get_or_create(
        username = 'anon',
        defaults = {
            'first_name' : 'anon',
            'last_name' : 'anon',
            'email' : 'anon@gmail.com',
            'password' : password
        }
    )

    admin_group = Group.objects.create(name='Admin')
    admin_group.save()
    user_group = Group.objects.create(name='Anonymous User')
    user_group.save()

    anon.groups.add(user_group)
    admin.groups.add(admin_group)
    admin2.groups.add(admin_group)

    admin_permissions = [
        'add_user',
        'change_user',
        'delete_user',
        'view_user',

        'add_brand',
        'change_brand',
        'delete_brand',
        'view_brand',
        
        'add_product',
        'change_product',
        'delete_product',
        'view_product',

        'add_buyout',
        'change_buyout',
        'delete_buyout',
        'view_buyout',
    ]
    for permission in admin_permissions:
        permission = Permission.objects.get(codename=permission)
        admin_group.permissions.add(permission)

    anon_permissions = [
        'view_brand',
        'view_product',
        'view_buyout',
    ]

    for permission in anon_permissions:
        permission = Permission.objects.get(codename=permission)
        user_group.permissions.add(permission)

def run_seed():
    print('Seeding data...')
    create_groups()
    print('Seeding finished.')