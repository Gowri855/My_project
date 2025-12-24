# create_superuser_once.py
from django.contrib.auth import get_user_model

User = get_user_model()

username = "gowri855"        # choose what you want
email = "whoops855@gmail.com"
password = "AjaigowriAlohomora@855"  # choose a strong temp password

if not User.objects.filter(is_superuser=True).exists():
    print("No superuser found. Creating one...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")
else:
    print("Superuser already exists. Skipping.")
