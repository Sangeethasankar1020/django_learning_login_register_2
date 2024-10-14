# db.py
from pymongo import MongoClient
from django.conf import settings

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['django_learning']
col = db['login']  # Use the collection for storing user data
