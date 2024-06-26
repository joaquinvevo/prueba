import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba.settings')
django.setup()
print("Django is set up correctly")