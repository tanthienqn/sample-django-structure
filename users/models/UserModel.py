import uuid
from django.db import models
from .BaseModel import BaseModel


class UserModel(BaseModel):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_code = models.CharField(max_length=80, null=False)
    username = models.CharField(max_length=80, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    location = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    is_actived = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
