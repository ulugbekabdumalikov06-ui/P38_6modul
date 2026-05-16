from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField, AutoField


class Register(Model):

    class Users(models):
        id = AutoField(primary_key=True)
        first_name = CharField(max_length=100)
        last_name = CharField(max_length=100)
        email = EmailField()
        password = CharField(max_length = 100)
        is_active = BooleanField(default=True)
        created_at = DateTimeField(auto_now_add=True)

    class Posts:
        id = AutoField(primary_key=True)
        comments = TextField()
        author_id = ForeignKey(Users, on_delete=CASCADE)
        created_at = DateTimeField(auto_now_add=True)
        updated_at = DateTimeField(auto_now=True)
    class Comments:
        id = AutoField(primary_key=True)
        content = TextField()
        author_id  = DateTimeField(auto_now=True)
        post_id = AutoField(primary_key=True)
        created_at = DateTimeField(auto_now_add=True)