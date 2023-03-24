from django.db import models

# Age groups
U18 = 'U18'
U17 = 'U17'
U16 = 'U16'
U15 = 'U15'
U14 = 'U14'
U13 = 'U14'
U12 = 'U12'
U11 = 'U11'
U10 = 'U10'
U9 = 'U9'
U8 = 'U8'
    
AGE_GROUP_CHOICES = [
    (U18, 'U18'),
    (U17, 'U17'), 
    (U16, 'U16'),
    (U15, 'U15'),
    (U14, 'U14'),
    (U13, 'U13'),
    (U12, 'U12'),
    (U11, 'U11'), 
    (U10, 'U10'), 
    (U9, 'U9'),
    (U8, 'U8'),
]

# Create your models here.

class Leader(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    role = models.CharField(max_length=40)
    bio = models.TextField(default="bio needed")
    

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
class Coach(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    role = models.CharField(max_length=40)
    team = models.ForeignKey('Team', on_delete=models.DO_NOTHING, default= None, null=True )
    bio = models.TextField(default="bio needed")
    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.role}, {self.team}"

class Team(models.Model):

    age_group = models.CharField(max_length=3, choices=AGE_GROUP_CHOICES)
    GIRLS = 'Girls'
    BOYS = 'Boys'
    SIDE_CHOICES = [(BOYS, 'Boys'), (GIRLS, 'Girls')]
    side = models.CharField(max_length=5, choices=SIDE_CHOICES)
    BLACK = 'BLK'
    YELLOW ='YLW'
    SILVER = 'SLVR'
    LEVEL_CHOICES = [( BLACK, 'BLK'), (YELLOW, 'YLW'), (SILVER, 'SLVR')]
    level = models.CharField(max_length=4, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.age_group} {self.side} | {self.level}"
    
class Manager(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    team = models.ForeignKey('Team', on_delete=models.DO_NOTHING, default= None, null=True )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


