from django.db import models
from django.conf import settings

# Create your models here.
class Member(models.Model):
    user_id = models.CharField(max_length = 24, blank = True, unique = True)
    user_name = models.CharField(max_length = 20)
    user_email = models.CharField(max_length = 64)
    password  = models.CharField(max_length = 64)


    def __unicode__(self):
        return u"{0}".format(self.user_name)



class MemberProfile(models.Model):
    GENDER_KIND = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(Member, unique = True)
    gender  = models.CharField(max_length = 1)
    address = models.CharField(max_length = 128)
    phone   = models.CharField(max_length = 16)


    def __unicode__(self):
        return u"{0}".format(self.user_id)



class FreeBoard(models.Model):
    """question
    about questions users added
    """
    user = models.ForeignKey(Member, unique = True)
    title = models.CharField(max_length=300)
    content = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return u"{0}".format(self.title)


class Tag(models.Model):
    """Tag
    Tag about question
    """
    name = models.CharField(max_length=80, blank=True, unique = True)
    freeboard = models.ManyToManyField('FreeBoard')

    def __unicode__(self):
        return u"{0}".format(self.name)