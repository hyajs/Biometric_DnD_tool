from django.db import models
import django.utils.timezone as timezone



class user_info(models.Model):
    YES_OR_NO_QUESTION = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    RACE_QUESTION = [
        ('Dwarf', 'Dwarf'),
        ('Elf', 'Elf'),
        ('Halfling', 'Halfling'),
        ('Human', 'Human'),
    ]
    CLASS_QUESTION = [
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Fighter', 'Fighter'),
        ('Rogue', 'Rogue'),
        ('Wizard', 'Wizard'),
    ]

    time = models.DateTimeField(default=timezone.now)
    first_survey_question = models.CharField(
        max_length=10,
        choices=YES_OR_NO_QUESTION,
    )
    second_survey_question = models.CharField(
        max_length=10,
        choices=RACE_QUESTION,
    )
    third_survey_question = models.CharField(
        max_length=10,
        choices=CLASS_QUESTION,
    )
    fourth_survey_question = models.CharField(
        max_length=10,
        choices=YES_OR_NO_QUESTION,
    )
    user_image = models.ImageField(upload_to='images')
    constitution = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    dexterity = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    wisdom = models.IntegerField(blank=True, null=True)
    alignment = models.TextField(max_length=20,blank=True, null=True)
    user_result = models.TextField(max_length=500,blank=True, null=True)

