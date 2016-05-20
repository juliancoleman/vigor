import datetime
import os
from decimal import Decimal, ROUND_DOWN

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import utc
from timezone_field import TimeZoneField


# Create your models here.
class SystemMessage(models.Model):
    message = models.CharField(max_length = 500)
    author = models.ForeignKey(User, related_name = 'sys_message')
    users_read = models.ManyToManyField(User, related_name = 'read_sys_message', blank = True)
    date_sent = models.DateField(auto_now_add = True)
    important = models.BooleanField(default = False)

    def has_read(self, user):
        if user in self.users_read.all():
            return True
        return False

    def __unicode__(self):
        return '%s: %s...' % (self.author.username, self.message[:50])

    class Meta:
        verbose_name_plural = 'System Messages'
        ordering = ['-date_sent']

class UserPrefs(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    DETERMINATIONS = (
        ('Gain Weight', 'Gain Weight'),
        ('Maintain Weight', 'Maintain Weight'),
        ('Lose Weight', 'Lose Weight'),
    )
    ETHNICITIES = (
        ('White', 'White'),
        ('European', 'European'),
        ('African American', 'African American'),
        ('Hispanic / Latino', 'Hispanic / Latino'),
        ('Asian', 'Asian'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Pacific Islander', 'Pacific Islander'),
        ('Native American / Alaskan', 'Native American / Alaskan'),
    )
    DATE_FORMATS = (
        ('MM/DD/YYYY', 'MM/DD/YYYY'),
        ('DD/MM/YYYY', 'DD/MM/YYYY'),
    )

    user = models.OneToOneField(User, primary_key = True, related_name = 'prefs')
    # Profile Settings
    gender = models.CharField(max_length = 1, choices = GENDERS, null = True, blank = True)
    birth_year = models.IntegerField(null = True, blank = True)
    birth_month = models.IntegerField(null = True, blank = True)
    birth_day = models.IntegerField(null = True, blank = True)
    ethnicity = models.CharField(max_length = 25, choices = ETHNICITIES, default = 'White')
    height_feet = models.IntegerField(null = True, blank = True)
    height_inches = models.IntegerField(null = True, blank = True)
    weight = models.IntegerField(null = True, blank = True)
    determination = models.CharField(max_length = 15, choices = DETERMINATIONS, default = 'Gain Weight')
    time_zone = TimeZoneField(null = True, blank = True)
    date_format = models.CharField(max_length=10, choices=DATE_FORMATS, default='MM/DD/YYYY')

    def get_today(self, pobj = False):
        today = datetime.datetime.utcnow().replace(tzinfo = utc)
        if self.time_zone:
            today = today.astimezone(self.time_zone)
            if pobj:
                return today
        return today.strftime(self.get_date_format())

    def get_date_format(self):
        if self.date_format == 'MM/DD/YYYY':
            return '%m/%d/%Y'
        elif self.date_format == 'DD/MM/YYYY':
            return '%d/%m/%Y'

    def is_male(self):
        return self.gender == 'M'

    def is_female(self):
        return self.gender == 'F'

    def get_age(self):
        if self.birth_year and self.birth_month and self.birth_day:
            today = self.get_today(pobj = True)
            return today.year - self.birth_year - ((today.month, today.day) < (self.birth_month, self.birth_day))

    def is_adult(self):
        return self.get_age() > 18

    def get_calorie_regimen(self):
        if self.determination == 'Gain Weight':
            if self.gender == 'M':
                return 10 * self.weight + 6.25 * (((self.height_feet * 12) + self.height_inches) * 2.54) - 5 * self.get_age() + 505
            elif self.gender == 'F':
                return 10 * self.weight + 6.25 (((self.height_feet * 12) + self.height_inches) * 2.54) - 5 * self.get_age() + 500 - 161
        elif self.determination == 'Maintain Weight':
            if self.gender == 'M':
                return 10 * self.weight + 6.25 * (((self.height_feet * 12) + self.height_inches) * 2.54) - 5 * self.get_age() + 5
            elif self.gender == 'F':
                return 10 * self.weight + 6.25 (((self.height_feet * 12) + self.height_inches) * 2.54) - 5 * self.get_age() - 161
        elif self.determination == 'Lose Weight':
            if self.gender == 'M':
                return 10 * self.weight + 6.25 * (((self.height_feet * 12) + self.height_inches) * 2.54) - 5 * self.get_age() + 5 - 500
            elif self.gender == 'F':
                return 10 * self.weight + 6.25 (((self.height_feet * 12) + self.height_inches) * 2.54) - 5 * self.get_age() - 161 - 500

    def __unicode__(self):
        return 'Preferences for user: %s' % self.user.username

    class Meta:
        verbose_name_plural = 'User Preferences'
        ordering = ['user']

class Meal(models.Model):
    name = models.CharField(max_length = 100)
    submission_date = models.DateField(null = True, blank = True)
    calories = models.IntegerField(null = True, blank = True)
    class Meta:
        ordering = ['name']
