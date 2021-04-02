from django.db import models

# Create your models here.

AUTHORS = {
    'Goswami Jaideva0': {'name': 'Goswami Jaideva0'},
    'Goswami Jaideva1': {'name': 'Goswami Jaideva1'},
    'Goswami Jaideva2': {'name': 'Goswami Jaideva2'},
    'Goswami Jaideva3': {'name': 'Goswami Jaideva3'},
    'Goswami Jaideva4': {'name': 'Goswami Jaideva4'}
}

BOOKS = [
    {'name': 'Fundamentals of Wavelets0', 'authors': [AUTHORS['Goswami Jaideva0']]},
    {'name': 'Fundamentals of Wavelets1', 'authors': [AUTHORS['Goswami Jaideva1']]},
    {'name': 'Fundamentals of Wavelets2', 'authors': [AUTHORS['Goswami Jaideva2']]},
    {'name': 'Fundamentals of Wavelets3', 'authors': [AUTHORS['Goswami Jaideva3']]},
    {'name': 'Fundamentals of Wavelets4', 'authors': [AUTHORS['Goswami Jaideva4']]}
]
