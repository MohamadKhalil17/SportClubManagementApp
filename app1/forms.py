from django.forms import ModelForm, widgets
from .models import LeaguesMen, LeaguesWomen,Player,Find,Fan,Staff,Forgot,Reset, Expenses, Revenue, Report, Cart, Price, CreditCard, choicesMonth, Match, Merchandise, News,Team, choicesPosition, choicesGender
from django import forms

# Create the form class.
class CreatePlayerForm(ModelForm):
	class Meta:
		model = Player
		fields = ['name','username', 'email', 'password', 'confirm_password', "gender", "position","photo"]
		widgets ={
			'name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your name", 'style':'padding: 10px 10px 10px 10px'}),
			'username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a User Name", 'style':'padding: 10px 10px 10px 10px'}),
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email", 'style':'padding: 10px 10px 10px 10px'}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'confirm_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'gender' : forms.Select(choices=choicesGender,attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Select your gender",  'style':'padding: 10px 10px 10px 10px'}),
			'position' : forms.Select(choices=choicesPosition,attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Select your position",  'style':'padding: 10px 10px 10px 10px'}),
			"photo" : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
		}

class CreateForm(ModelForm):
	class Meta:
		model = Player
		fields = ['name', 'username', 'email', 'password', 'confirm_password']
		widgets ={
			'name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your name", 'style':'padding: 10px 10px 10px 10px'}),
			'username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a User Name", 'style':'padding: 10px 10px 10px 10px'}),
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email", 'style':'padding: 10px 10px 10px 10px'}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'confirm_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),

		}

class FindForm(ModelForm):
	class Meta:
		model = Find
		fields = ['username', 'password']
		widgets ={
			'username' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),
			'password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password'}),

		}

class ForgotForm(ModelForm):
	class Meta:
		model = Forgot
		fields = ['email']
		widgets ={
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your User Name"}),

		}
class ResetForm(ModelForm):
	class Meta:
		model = Reset
		fields = ['email','new_password','confirm_new_password']
		widgets ={
			'email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your email", 'style':'padding: 10px 10px 10px 10px'}),
			'new_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),
			'confirm_new_password' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Re-enter a password", 'type':'password', 'style':'padding: 10px 10px 10px 10px'}),

		}

class ExpenseForm(ModelForm):
	class Meta:
		model = Expenses
		fields = ['department_expense','department_name','expense_name','expense_date']
		widgets ={
			'department_expense' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter the expense amount", 'style':'padding: 10px 10px 10px 10px'}),
			'department_name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your department name",  'style':'padding: 10px 10px 10px 10px'}),
			'expense_name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter the type of expense", 'style':'padding: 10px 10px 10px 10px'}),
			'expense_date' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter the date of expense", 'style':'padding: 10px 10px 10px 10px'}),

		}


class ReportForm(ModelForm):
	class Meta:
		model = Report
		fields = ['Month','Name','Department','Email']
		widgets ={
			'Month' : forms.Select(choices=choicesMonth,attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Name",  'style':'padding: 10px 10px 10px 10px'}),
			'Name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Name",  'style':'padding: 10px 10px 10px 10px'}),
			'Department' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Department Name", 'style':'padding: 10px 10px 10px 10px'}),
			'Email' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle','placeholder':"Enter Email", 'style':'padding: 10px 10px 10px 10px'}),
		}

class GetPrice(ModelForm):
	class Meta:
		model = Price
		fields = []

class CreditCardForm(ModelForm):
	class Meta:
		model = CreditCard
		fields = ['name','card_number','experation_date', 'CCV']
		widgets = {
			'name' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Your Name",  'style':'padding: 10px 10px 10px 10px'}),
			'card_number' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"____ ____ ____ ____",  'style':'padding: 10px 10px 10px 10px'}),
			'experation_date' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"YY/MM",  'style':'padding: 10px 10px 10px 10px'}),
			'CCV' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"___",  'style':'padding: 10px 10px 10px 10px'}),
		}


class AddMatch(ModelForm):
	class Meta:
		model = Match
		fields = ['team1','team1_logo', 'team2','team2_logo','location','date','score_team1','score_team2','priceA','priceB','priceC','num_ticketsA','num_ticketsB','num_ticketsC','streaming_title','streaming_body','streaming_video']
		widgets = {
			'team1' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Team 1 Name",  'style':'padding: 10px 10px 10px 10px'}),
			'team1_logo' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
			'team2' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Team 2 Name",  'style':'padding: 10px 10px 10px 10px'}),
			'team2_logo' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
			'date' : forms.DateInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px','type': 'date'}),
			'score_team1' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Score Team 1",  'style':'padding: 10px 10px 10px 10px'}),
			'score_team2' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Score Team 2",  'style':'padding: 10px 10px 10px 10px'}),
			'location' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Match Location",  'style':'padding: 10px 10px 10px 10px'}),
			'priceA' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Price Zone A",  'style':'padding: 10px 10px 10px 10px'}),
			'priceB' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Price Zone B",  'style':'padding: 10px 10px 10px 10px'}),
			'priceC' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Price Zone C",  'style':'padding: 10px 10px 10px 10px'}),
			'num_ticketsA' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Total Number of Tickets for Zone A",  'style':'padding: 10px 10px 10px 10px'}),
			'num_ticketsB' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Total Number of Tickets for Zone B",  'style':'padding: 10px 10px 10px 10px'}),
			'num_ticketsC' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Total Number of Tickets for Zone C",  'style':'padding: 10px 10px 10px 10px'}),
			'streaming_title' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter The Streaming Title",  'style':'padding: 10px 10px 10px 10px'}),
			'streaming_body' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter The Streaming Description",  'style':'padding: 10px 10px 10px 10px'}),
			'streaming_video' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Streaming Link",  'style':'padding: 10px 10px 10px 10px'}),
		}

class AddMerchandise(ModelForm):
	class Meta:
		model = Merchandise
		fields = ['item_name','price','item_image', 'stock']
		widgets = {
			'item_name' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Item Name",  'style':'padding: 10px 10px 10px 10px'}),
			'price' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Item Price",  'style':'padding: 10px 10px 10px 10px'}),
			'item_image' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
			'stock' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Available Stock",  'style':'padding: 10px 10px 10px 10px'}),
		}

class AddNews(ModelForm):
	class Meta:
		model = News
		fields = ['news_title','news_main', 'news_image','news_date','news_number']
		widgets = {
			'news_title' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter News Title",  'style':'padding: 10px 10px 10px 10px'}),
			'news_main' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter News Main",  'style':'padding: 10px 10px 10px 10px'}),
			'news_image' : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
			'news_date' : forms.DateInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px','type': 'date'}),
			'news_number' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter News number",  'style':'padding: 10px 10px 10px 10px'}),
		}

class AddMenLeague(ModelForm):
	class Meta:
		model = LeaguesMen
		fields = ['team_name','points', 'rank']
		widgets = {
			'team_name' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Team name",  'style':'padding: 10px 10px 10px 10px'}),
			'points' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Points",  'style':'padding: 10px 10px 10px 10px'}),
	
			'rank' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Rank",  'style':'padding: 10px 10px 10px 10px'}),
		}

class AddWomenLeague(ModelForm):
	class Meta:
		model = LeaguesWomen
		fields = ['team_name','points', 'rank']
		widgets = {
			'team_name' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Team name",  'style':'padding: 10px 10px 10px 10px'}),
			'points' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Points",  'style':'padding: 10px 10px 10px 10px'}),
	
			'rank' : forms.TextInput(attrs={'class': 'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter Rank",  'style':'padding: 10px 10px 10px 10px'}),
		}

class AddTeam(ModelForm):
	class Meta:
		model = Team
		fields = ['name',"gender", "position",'photo']
		widgets = {
			'name' : forms.TextInput(attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Enter your name", 'style':'padding: 10px 10px 10px 10px'}),
			'gender' : forms.Select(choices=choicesGender,attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Select your gender",  'style':'padding: 10px 10px 10px 10px'}),
			'position' : forms.Select(choices=choicesPosition,attrs={'class':'u-grey-5 u-input u-input-rectangle', 'placeholder':"Select your position",  'style':'padding: 10px 10px 10px 10px'}),
			"photo" : forms.FileInput(attrs={'class': 'u-input', 'style':'padding: 10px 10px 10px 10px'}),
		}

