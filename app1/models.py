from asyncio import constants
from tokenize import ContStr
from unittest.mock import DEFAULT
from django.db import models
from  embed_video.fields  import  EmbedVideoField

# Create your models here.


choicesGender = [
    ('Male', 'Male'),
    ('Female',"Female"),
    ('Other',"Other")
]
choicesPosition = [
    ('Goalkeeper', 'Goalkeeper'),
    ('Defender',"Defender"),
    ('Midfielder',"Midfielder"),
    ('Forward',"Forward"),
]

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique=True)
    gender = models.CharField(max_length=30,choices= choicesGender)
    position = models.CharField(max_length=30,choices= choicesPosition)
    photo = models.ImageField(null=True,blank=True,upload_to='teams')

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30,choices= choicesGender)
    position = models.CharField(max_length=30,choices= choicesPosition)
    photo = models.ImageField(null=True,blank=True,upload_to='teams')

class Find(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)

class Fan(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique=True)

class Forgot(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30,unique=True)

class Reset(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30,unique=True)
    new_password = models.CharField(max_length=30)
    confirm_new_password = models.CharField(max_length=30)

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    team1 = models.CharField(max_length=30)
    team1_logo = models.ImageField(null=True,blank=True,upload_to='matches')
    team2 = models.CharField(max_length=30)
    team2_logo = models.ImageField(null=True,blank=True,upload_to='matches')
    location = models.CharField(max_length=30)
    date = models.DateField()
    score_team1 = models.IntegerField(null=True)
    score_team2 = models.IntegerField(null=True)
    priceA = models.IntegerField()
    priceB = models.IntegerField()
    priceC = models.IntegerField()
    num_ticketsA = models.IntegerField()
    num_ticketsB = models.IntegerField()
    num_ticketsC = models.IntegerField()
    streaming_title = models.CharField(max_length=200)
    streaming_body = models.TextField()
    streaming_video = EmbedVideoField()
    class  Meta:
        verbose_name_plural = "Match"
    def  __str__(self):
        return  str(self.streaming_title) if  self.streaming_title  else  " "

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    department_expense = models.CharField(max_length=30)
    department_name = models.CharField(max_length=30)
    expense_name = models.CharField(max_length=30)
    expense_date = models.CharField(max_length=30)


class Revenue(models.Model):
    id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    item_name = models.CharField(max_length=30)
    item_date = models.CharField(max_length=30)
    item_price = models.CharField(max_length=30)
    item_amount = models.CharField(max_length=30)
    
choicesMonth = [
    ('January', 'January'),
    ('February',"February"),
    ('March',"March"),
    ('April',"April"),
    ('May',"May"),
    ('June',"June"),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December')
]



class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    Month = models.CharField(max_length=30,choices= choicesMonth)
    Name = models.CharField(max_length=30)
    Department = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    news_title = models.CharField(max_length=100)
    news_main = models.CharField(max_length=500)
    news_date = models.DateField(null=True)
    news_image = models.ImageField(null=True,blank=True,upload_to='news')
    news_number = models.IntegerField()

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    item = models.CharField(max_length=30,unique=True)
    price = models.IntegerField()
    amount = models.IntegerField()

class Price(models.Model):
    id = models.IntegerField(primary_key=True)

class CreditCard(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    experation_date = models.CharField(max_length=5)
    CCV = models.IntegerField()

class Merchandise(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=30)
    price = models.IntegerField()
    item_image = models.ImageField(upload_to= 'merch')
    stock = models.IntegerField()

class Purchases(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    item = models.CharField(max_length=30)
    price = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField(null=True)

class LeaguesMen(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name= models.CharField(max_length=100)
    points=models.IntegerField()
    rank = models.IntegerField()

class LeaguesWomen(models.Model):
    id = models.IntegerField(primary_key=True)
    team_name= models.CharField(max_length=100)
    points=models.IntegerField()
    rank = models.IntegerField()


