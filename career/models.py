from django.db import models
from django.contrib.auth.models import User

from news.fields import DateTimeField

# Create your models here.

class Career(models.Model):
    CAREER_CHOICE = (
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Full Time', 'Full Time'),
    )
    title = models.CharField(max_length=255)
    term = models.CharField(max_length=50, choices=CAREER_CHOICE, default="Internship")
    function = models.TextField(max_length=500)
    # requirement = HTMLField()
    requirement = models.TextField()
    show = models.BooleanField(default=False)
    created = DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User,
                                   related_name='career_created',
                                   editable=False)
    modified = DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(User,
                                    related_name='career_modified',
                                    editable=False)
