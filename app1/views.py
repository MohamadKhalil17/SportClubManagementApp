from tkinter import CENTER
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import AddMenLeague, AddNews, AddWomenLeague, CreatePlayerForm,CreateForm,FindForm,ForgotForm,ResetForm, ExpenseForm, ReportForm, GetPrice, CreditCardForm, AddMatch, AddMerchandise, AddNews, AddTeam
from .models import Player, Fan, Staff,Team, Match, Expenses, Revenue, News, Cart, Price, CreditCard, Merchandise, Purchases, Report, LeaguesMen, LeaguesWomen
from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse
from reportlab.platypus import Table, Frame, Paragraph, Spacer, SimpleDocTemplate, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import pandas as pd
from datetime import date, datetime
import pytz
import csv
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet


def index(request):
	request.session['user'] = None
	request.session['staff'] = None
	request.session['player'] = None
	request.session['fan'] = None
	request.session['match'] = None
	request.session['buying'] = None
	Cart.objects.all().delete()
	player = request.session['player']
	fan = request.session['fan']
	news = News.objects.all()
	return render(request,'index.html', {'player':player, 'fan':fan, 'news1':news[0],'news2':news[1]})

def home_main(request):
	player = request.session['player']
	fan = request.session['fan']
	news = News.objects.all()
	return render(request,'HOME.html', {'player':player, 'fan':fan, 'news1':news[0],'news2':news[1]})

def subpage(request,id):
	user = request.session['user']
	player = request.session['player']
	fan = request.session['fan']
	news = News.objects.get(id = id)
	news_title = news.news_title
	news_image=news.news_image
	return render(request,'News-Subpage.html',{ 'user':user, 'news':news, 'news_title':news_title, 'news_image':news_image, 'player':player, 'fan':fan})

def leagues(request):
	leaguemen = LeaguesMen.objects.all().order_by('rank')
	leaguewomen = LeaguesWomen.objects.all()
	user = request.session['user']
	staff = request.session['staff']
	return render(request, 'leagues.html', {'user':user, 'staff':staff,'leaguemen':leaguemen, 'leaguewomen':leaguewomen})

def teams(request):
	staff = request.session['staff']
	user = request.session['user']
	player = request.session['player']
	playerMenForward = Team.objects.all().filter(gender="Male",position="Forward")
	playerMenDefender = Team.objects.all().filter(gender="Male",position="Defender")
	playerMenGoalkeeper = Team.objects.all().filter(gender="Male",position="Goalkeeper")
	playerMenMidfielder = Team.objects.all().filter(gender="Male",position="Midfielder")
	playerWomenForward = Team.objects.all().filter(gender="Female",position="Forward")
	playerWomenDefender = Team.objects.all().filter(gender="Female",position="Defender")
	playerWomenGoalkeeper = Team.objects.all().filter(gender="Female",position="Goalkeeper")
	playerWomenMidfielder = Team.objects.all().filter(gender="Female",position="Midfielder")
	playerOtherForward = Team.objects.all().filter(gender="Other",position="Forward")
	playerOtherDefender = Team.objects.all().filter(gender="Other",position="Defender")
	playerOtherGoalkeeper = Team.objects.all().filter(gender="Other",position="Goalkeeper")
	playerOtherMidfielder = Team.objects.all().filter(gender="Other",position="Midfielder")
	return render(request, 'teams.html', { "user":user,"staff":staff, "playerMenForward":playerMenForward, "playerMenDefender": playerMenDefender,
	"playerMenGoalkeeper":playerMenGoalkeeper,"playerMenMidfielder":playerMenMidfielder, "playerWomenForward":playerWomenForward,
	"playerWomenDefender": playerWomenDefender, "playerWomenGoalkeeper": playerWomenGoalkeeper,"playerWomenMidfielder": playerWomenMidfielder,
	"playerOtherForward":playerOtherForward, "playerOtherDefender" : playerOtherDefender, "playerOtherGoalkeeper": playerOtherGoalkeeper,
	"playerOtherMidfielder":playerOtherMidfielder, 'player':player})
	

def delete_team(request,id):
	Team.objects.all().filter(id=id).first().delete()
	return HttpResponseRedirect('teams')\

def add_team(request):
	if request.method == 'POST':
		form = AddTeam(request.POST, request.FILES)
		if form.is_valid():
			Teamform = form.cleaned_data
			name = Teamform['name']
			gender = Teamform['gender']
			position = Teamform['position']
			photo = Teamform['photo']
			try:
				player = Player.objects.get(name=name)
			except Player.DoesNotExist:
				player = None
			if(player):
				next_id = 1
				if(Team.objects.all()):
					next_id = Team.objects.last().id + 1
				if photo is not None:
					Team.objects.create(id=next_id,name=name,gender=gender,position=position,photo=photo)
				else :
					Team.objects.create(id=next_id,name=name,gender=gender,position=position,photo=player.photo)
				return HttpResponseRedirect('teams')
			else:
				form = AddTeam()
				message = "Player does not exist!"
				return render(request, 'Add-Team.html', {'form': form, "message": message})
		return render(request, 'Add-Team.html', {'form': form})
	form = AddTeam()
	return render(request,'Add-Team.html',{'form':form})

def edit_team(request,id):
	if request.method == 'POST':
		form = AddTeam(request.POST, request.FILES)
		if form.is_valid():
			Teamform = form.cleaned_data
			name = Teamform['name']
			gender = Teamform['gender']
			position = Teamform['position']
			photo = Teamform['photo']
			for e in Team.objects.all():
				if e.id==id:
					e.gender = gender
					e.name = name
					e.position = position
					if photo is not None:
						e.photo = photo
					e.save()
					return HttpResponseRedirect('teams')
		form = AddTeam()
		return render(request, 'Edit-Team.html', {'form': form})
	form = AddTeam()
	return render(request,'Edit-Team.html',{'form':form})


def home_staff(request):
	staff = request.session['staff']
	player = request.session['player']
	fan = request.session['fan']
	news = News.objects.all()
	return render(request,'HOME_Staff.html', {'player':player, 'fan':fan, 'news1':news[0],'news2':news[1]})

def history(request):
	user = request.session['user']
	history = Purchases.objects.all().filter(user_id = user)
	return render(request,'History.html',{'user':user,'history':history})

def merch(request):
	merch = Merchandise.objects.all()
	user = request.session['user']
	staff = request.session['staff']
	return render(request,'Merchandise.html', { 'merch':merch, 'user':user, 'staff':staff})

def item(request,id):
	user = request.session['user']
	item = Merchandise.objects.all().filter(id=id).first()
	next_id = 1
	if(Cart.objects.all()):
		next_id = Cart.objects.last().id + 1
	if Cart.objects.all().filter(item=item.item_name).first() is None:
		Cart.objects.create(id=next_id,user_id=user,item = item.item_name, price = item.price, amount = 1)
	total = 0
	for e in Cart.objects.all().filter(user_id=int(user)):
		total += e.price*e.amount
	form = CreditCardForm()
	cart = Cart.objects.all().filter(user_id=int(user))
	return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form })

def add(request,id):
	user = request.session['user']
	for e in Cart.objects.all():
				if e.user_id==user and e.id == id:
					e.amount += 1
					e.save()
	cart = Cart.objects.all().filter(user_id=int(user))
	return HttpResponseRedirect('buyA')

def addnews(request):
	if request.method == 'POST':
		form = AddNews(request.POST, request.FILES)
		if form.is_valid():
			Newsform = form.cleaned_data
			news_title = Newsform['news_title']
			news_main = Newsform['news_main']
			news_image = Newsform['news_image']
			news_date = Newsform['news_date']
			news_number = Newsform['news_number']
			if news_number < 0 :
				form = AddNews()
				message = "Invalid number"
				return render(request, 'Add-News.html', {'form': form, 'message':message})
			next_id = 1
			if(News.objects.all()):
				next_id = News.objects.last().id + 1
			News.objects.create(id=next_id,news_title=news_title,news_main=news_main,news_image=news_image,news_date=news_date,news_number=news_number)
			return HttpResponseRedirect('news')
		form = AddNews()
		return render(request, 'Add-News.html', {'form': form})
	form = AddNews()
	return render(request,'Add-News.html',{'form':form})

def addmenleague(request):
	if request.method == 'POST':
		form = AddMenLeague(request.POST, request.FILES)
		if form.is_valid():
			Leagueform = form.cleaned_data
			team_name = Leagueform['team_name']
			points = Leagueform['points']
			rank = Leagueform['rank']
			
			if points < 0 or rank<0 :
				form = AddMenLeague()
				message = "Invalid number"
				return render(request, 'Add-League.html', {'form': form, 'message':message})
			next_id = 1
			if(LeaguesMen.objects.all()):
				next_id = LeaguesMen.objects.last().id + 1
			LeaguesMen.objects.create(id=next_id,team_name=team_name,points=points,rank=rank)
			return HttpResponseRedirect('leagues')
		form = AddMenLeague()
		return render(request, 'Add-League.html', {'form': form})
	form = AddMenLeague()
	return render(request,'Add-League.html',{'form':form})

def editmenleague(request,id):
	if request.method == 'POST':
		form = AddMenLeague(request.POST, request.FILES)
		if form.is_valid():
			Leagueform = form.cleaned_data
			team_name = Leagueform['team_name']
			points = Leagueform['points']
			rank = Leagueform['rank']
			
			if points < 0 or rank<0 :
				form = AddMenLeague()
				message = "Invalid number"
				return render(request, 'Edit-League.html', {'form': form, 'message':message})
			next_id = 1
			if(LeaguesMen.objects.all()):
				next_id = LeaguesMen.objects.last().id + 1
			for e in LeaguesMen.objects.all():
				if e.id==id:
					e.team_name = team_name
					e.points = points
					e.rank = rank
					e.save()
					return HttpResponseRedirect('leagues')
		form = AddMenLeague()
		return render(request, 'Edit-League.html', {'form': form})
	form = AddMenLeague()
	return render(request,'Edit-League.html',{'form':form})

def addwomenleague(request):
	if request.method == 'POST':
		form = AddWomenLeague(request.POST, request.FILES)
		if form.is_valid():
			Leagueform = form.cleaned_data
			team_name = Leagueform['team_name']
			points = Leagueform['points']
			rank = Leagueform['rank']
			
			if points < 0 or rank<0 :
				form = AddWomenLeague()
				message = "Invalid number"
				return render(request, 'Add-League.html', {'form': form, 'message':message})
			next_id = 1
			if(LeaguesWomen.objects.all()):
				next_id = LeaguesWomen.objects.last().id + 1
			LeaguesWomen.objects.create(id=next_id,team_name=team_name,points=points,rank=rank)
			return HttpResponseRedirect('leagues')
		form = AddWomenLeague()
		return render(request, 'Add-League.html', {'form': form})
	form = AddWomenLeague()
	return render(request,'Add-League.html',{'form':form})

def editwomenleague(request,id):
	if request.method == 'POST':
		form = AddWomenLeague(request.POST, request.FILES)
		if form.is_valid():
			Leagueform = form.cleaned_data
			team_name = Leagueform['team_name']
			points = Leagueform['points']
			rank = Leagueform['rank']
			
			if points < 0 or rank<0 :
				form = AddWomenLeague()
				message = "Invalid number"
				return render(request, 'Edit-League.html', {'form': form, 'message':message})
			next_id = 1
			if(LeaguesWomen.objects.all()):
				next_id = LeaguesWomen.objects.last().id + 1
			for e in LeaguesWomen.objects.all():
				if e.id==id:
					e.team_name = team_name
					e.points = points
					e.rank = rank
					e.save()
					return HttpResponseRedirect('leagues')
		form = AddWomenLeague()
		return render(request, 'Edit-League.html', {'form': form})
	form = AddWomenLeague()
	return render(request,'Edit-League.html',{'form':form})

def addmatch(request):
	if request.method == 'POST':
		form = AddMatch(request.POST, request.FILES)
		if form.is_valid():
			Matchform = form.cleaned_data
			team1 = Matchform['team1']
			team1_logo = Matchform['team1_logo']
			team2 = Matchform['team2']
			team2_logo = Matchform['team2_logo']
			date = Matchform['date']
			location = Matchform['location']
			score_team1 = Matchform['score_team1']
			score_team2 = Matchform['score_team2']
			priceA = Matchform['priceA']
			priceB = Matchform['priceB']
			priceC = Matchform['priceC']
			streaming_title = Matchform["streaming_title"]
			streaming_body = Matchform["streaming_body"]
			streaming_video = Matchform["streaming_video"]
			if priceA < 0 or priceB < 0 or priceC < 0:
				form = AddMatch()
				message = "Invalid Price"
				return render(request, 'Add-Match.html', {'form': form, 'message':message})
			next_id = 1
			if(Match.objects.all()):
				next_id = Match.objects.last().id + 1
			Match.objects.create(id=next_id,team1=team1,team1_logo=team1_logo,team2=team2,team2_logo=team2_logo,date=date,location=location,score_team1=score_team1,score_team2=score_team2,priceA=priceA,priceB=priceB,priceC=priceC,streaming_title=streaming_title,streaming_body=streaming_body,streaming_video=streaming_video)
			return HttpResponseRedirect('matches')
		form = AddMatch()
		return render(request, 'Add-Match.html', {'form': form})
	form = AddMatch()
	return render(request,'Add-Match.html',{'form':form})


def deletematch(request,id,type):
	Match.objects.all().filter(id=id).first().delete()
	if type == 1:
		return HttpResponseRedirect('matches')
	return HttpResponseRedirect('past_matches')

def delete_expense(request,id):
	Expenses.objects.all().filter(id=id).first().delete()
	return HttpResponseRedirect('expenses')

def edit_expense(request,id):
	if request.method == 'POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			Expenseform = form.cleaned_data
			department_expense =Expenseform['department_expense']
			department_name =Expenseform['department_name']
			expense_name =Expenseform['expense_name']
			expense_date =Expenseform['expense_date']
			for e in Expenses.objects.all():
				if e.id==id:
					e.department_expense = department_expense
					e.department_name = department_name
					e.expense_name = expense_name
					e.expense_date = expense_date
					e.save()
					return HttpResponseRedirect('expenses')
		form = ExpenseForm()
		return render(request, 'Edit-Expenses.html', {'form': form})
	form = ExpenseForm()
	return render(request,'Edit-Expenses.html',{'form':form})

def editmatch(request,id,type):
	if request.method == 'POST':
		form = AddMatch(request.POST, request.FILES)
		if form.is_valid():
			Matchform = form.cleaned_data
			team1 = Matchform['team1']
			team1_logo = Matchform['team1_logo']
			team2 = Matchform['team2']
			team2_logo = Matchform['team2_logo']
			date = Matchform['date']
			location = Matchform['location']
			score_team1 = Matchform['score_team1']
			score_team2 = Matchform['score_team2']
			priceA = Matchform['priceA']
			priceB = Matchform['priceB']
			priceC = Matchform['priceC']
			streaming_title = Matchform["streaming_title"]
			streaming_body = Matchform["streaming_body"]
			streaming_video = Matchform["streaming_video"]
			if priceA < 0 or priceB < 0 or priceC < 0:
				form = AddMatch()
				message = "Invalid Price"
				return render(request, 'Edit-Match.html', {'form': form, 'message':message})
			for e in Match.objects.all():
				if e.id==id:
					e.team1 = team1
					e.team1_logo = team1_logo
					e.team2 = team2
					e.team2_logo = team2_logo
					e.date = date
					e.location = location
					if score_team1 is not None:
						e.score_team1 = score_team1
					if score_team2 is not None:
						e.score_team2 = score_team2
					e.priceA = priceA
					e.priceB = priceB
					e.priceC = priceC
					e.streaming_title = streaming_title
					e.streaming_body = streaming_body
					e.streaming_video = streaming_video
					e.save()
					if type == 1:
						return HttpResponseRedirect('matches')
					return HttpResponseRedirect('past_matches')
		form = AddMatch()
		message = "incorrect video link"
		return render(request, 'Edit-Match.html', {'form': form,'message':message})
	form = AddMatch()
	return render(request,'Edit-Match.html',{'form':form})

def editnews(request,id):
	if request.method == 'POST':
		form = AddNews(request.POST, request.FILES)
		if form.is_valid():
			Newsform = form.cleaned_data
			news_title = Newsform['news_title']
			news_main = Newsform['news_main']
			news_image = Newsform['news_image']
			news_date = Newsform['news_date']
			news_number = Newsform['news_number']
			if news_number < 0 :
				form = AddNews()
				message = "Invalid number"
				return render(request, 'Add-News.html', {'form': form, 'message':message})
			for e in News.objects.all():
				if e.id==id:
					e.news_title = news_title
					e.news_main = news_main
					e.news_image = news_image
					e.news_date = news_date
					e.news_number = news_number
					e.save()
					
					return HttpResponseRedirect('news')
		form = AddNews()
		return render(request, 'Edit-News.html', {'form': form})
	form = AddNews()
	return render(request,'Edit-News.html',{'form':form})

def schedule(request):
	D={"01":"January", "02":"February","03":"March","04":"April","05":"May",
	"06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
	user = request.session['user']
	staff = request.session['staff']
	player = request.session['player']
	today=date.today()
	today = datetime.strptime(str(today), '%Y-%m-%d')
	today=str(today)
	month= today[5:7]
	year=today[0:4]
	month_year=today[0:7]
	days_of_month={"01":1, "02":-1,"03":1,"04":0,"05":1,"06":0,"07":1,"08":1,"09":0,"10":1,"11":0,"12":1}
	L=[]
	n=28
	if days_of_month[month]==1:
		n=31
	elif days_of_month[month]==0:
		n=30
	for i in range(1,n+1):
			if i<10:
				L.append(year+"-"+month+"-"+"0"+str(i))
			else:
				L.append(year+"-"+month+"-"+str(i))
	month=D[month]
	match = Match.objects.all().filter(date__range=["1800-01-01", "3000-01-01"])
	match_list=[]
	for item in match:
		item.date=str(item.date)
		match_list.append(item.date)
	return render(request,'Schedule.html',{ 'user':user, 'match':match,"Month":month,'n':n,'L':L, 'match_list':match_list, 'staff':staff, 'player':player })


def addmerch(request):
	if request.method == 'POST':
		form = AddMerchandise(request.POST, request.FILES)
		if form.is_valid():
			Matchform = form.cleaned_data
			item_name = Matchform['item_name']
			price = Matchform['price']
			item_image = Matchform['item_image']
			stock = Matchform['stock']
			if price < 0:
				form = AddMerchandise()
				message = "Invalid Price"
				return render(request, 'Add-Merch.html', {'form': form, 'message':message})
			next_id = 1
			if(Merchandise.objects.all()):
				next_id = Merchandise.objects.last().id + 1
			Merchandise.objects.create(id=next_id,item_name=item_name,price=price,item_image=item_image,stock=stock)
			return HttpResponseRedirect('merchandise')
		form = AddMerchandise()
		return render(request, 'Add-Merch.html', {'form': form})
	form = AddMerchandise()
	return render(request,'Add-Merch.html',{'form':form})

def deletemerch(request,id):
	Merchandise.objects.all().filter(id=id).first().delete()
	return HttpResponseRedirect('merchandise')

def editmerch(request,id):
	if request.method == 'POST':
		form = AddMerchandise(request.POST, request.FILES)
		if form.is_valid():
			Matchform = form.cleaned_data
			item_name = Matchform['item_name']
			price = Matchform['price']
			item_image = Matchform['item_image']
			if price < 0:
				form = AddMerchandise()
				message = "Invalid Price"
				return render(request, 'Edit-Merch.html', {'form': form, 'message':message})
			for e in Merchandise.objects.all():
				if e.id==id:
					e.item_name = item_name
					e.price = price
					e.item_image = item_image
					e.save()
					return HttpResponseRedirect('merchandise')
		form = AddMerchandise()
		return render(request, 'Edit-Merch.html', {'form': form})
	form = AddMerchandise()
	return render(request,'Edit-Merch.html',{'form':form})

def deletenews(request,id):
	News.objects.all().filter(id=id).first().delete()
	return HttpResponseRedirect('news')

def deletemenleague(request,id):
	LeaguesMen.objects.all().filter(id=id).first().delete()
	return HttpResponseRedirect('leagues')

def deletewomenleague(request,id):
	LeaguesWomen.objects.all().filter(id=id).first().delete()
	return HttpResponseRedirect('leagues')
	
def remove(request,id):
	user = request.session['user']
	for e in Cart.objects.all():
				if e.user_id==user and e.id == id and e.amount !=0:
					e.amount -= 1
					e.save()
	cart = Cart.objects.all().filter(user_id=int(user))
	return HttpResponseRedirect('buyA')

def buyA(request):
	user = request.session['user']
	if request.method =='POST':
		form=CreditCardForm(request.POST)
		if form.is_valid():
			PurchaseForm = form.cleaned_data
			name = PurchaseForm['name']
			card_number = PurchaseForm['card_number']
			experation_date = PurchaseForm['experation_date']
			CCV = PurchaseForm['CCV']
			for e in Cart.objects.all().filter(user_id=user):
				if 'Ticket' in e.item:
					match = Match.objects.get(id = int(e.item[-2]))
					zone = e.item[-1]
					if zone == 'A' and match.num_ticketsA < e.amount or zone == 'B' and match.num_ticketsB < e.amount or zone == 'C' and match.num_ticketsC < e.amount:
						cart = Cart.objects.all().filter(user_id=int(user))
						total = 0
						for e in Cart.objects.all().filter(user_id=int(user)):
							total += e.price*e.amount
						form = CreditCardForm()
						message = 'not enough available tickets'
						return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form, 'message':message })
					if zone == 'A':
						match.num_ticketsA -= e.amount
						match.save()
					if zone == 'B':
						match.num_ticketsB -= e.amount
						match.save()
					if zone == 'C':
						match.num_ticketsC -= e.amount
						match.save()
				elif Merchandise.objects.get(item_name=item).stock < e.amount:
					cart = Cart.objects.all().filter(user_id=int(user))
					total = 0
					for e in Cart.objects.all().filter(user_id=int(user)):
						total += e.price*e.amount
					form = CreditCardForm()
					message = 'not enough available stock'
					return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form, 'message':message })	
				next_id = 1
				if(Purchases.objects.all()):
					next_id = Purchases.objects.last().id + 1
				Purchases.objects.create(id=next_id,user_id=user,item = e.item, price = e.price, amount = e.amount, date = date.today())
				next_id = 1
				if(Revenue.objects.all()):
					next_id = Purchases.objects.last().id + 1
				Revenue.objects.create(id=next_id,department_name='Tickets',item_name = e.item, item_price = e.price, item_amount = e.amount, item_date = date.today())
			cart = Cart.objects.all().filter(user_id=int(user))
			total = 0
			for e in Cart.objects.all().filter(user_id=int(user)):
				total += e.price*e.amount
			form = CreditCardForm()
			message = 'Purchase completed succesfuly'
			return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form, 'message':message })
	cart = Cart.objects.all().filter(user_id=int(user))
	total = 0
	for e in Cart.objects.all().filter(user_id=int(user)):
		total += e.price*e.amount
	form = CreditCardForm()
	return render(request,'buy.html',{'cart':cart , 'total':total, 'form':form })

def buyM(request,id):
	user = request.session['user']
	merch = Merchandise.objects.get(id=id)
	next_id = 1
	if(Cart.objects.all()):
		next_id = Cart.objects.last().id + 1
	Cart.objects.all().filter(item=merch.item_name).filter(user_id=user).delete()
	Cart.objects.create(id=next_id,user_id=user,item = merch.item_name, price = merch.price, amount = 1)
	return HttpResponseRedirect('buyA')

def news(request):
	news = News.objects.order_by('news_date').all()
	user = request.session['user']
	staff = request.session['staff']
	player = request.session['player']
	fan = request.session['fan']
	return render(request,'News.html',{ 'user':user, 'news':news, 'staff': staff, 'player':player, 'fan':fan})

def make_table(department, month):
	df1 = pd.DataFrame(Expenses.objects.all().values()) 
	df2 = pd.DataFrame(Revenue.objects.all().values())
	df1 = df1[df1["department_name"] == department] 
	df2 = df2[df2["department_name"] == department]
	df1 = df1[["expense_date","department_expense","expense_name"]]
	df1 = df1[df1["expense_date"].str.contains(month)]
	df1.rename(columns={"expense_name":"Expense Name", "department_expense":"Expense Amount","expense_date": "Expense Date"},inplace=True)
	total0 = int(df1["Expense Amount"].astype(int).sum(axis=0))
	df2_temp = df2[["item_name", "item_date","item_price"]]
	df2_temp = df2_temp[df2_temp["item_date"].str.contains(month)]
	total1 = int(df2_temp["item_price"].astype(int).sum(axis=0))
	df2 = df2_temp.reset_index(drop=True)
	df2.rename(columns={"item_name":"Item Name", "item_price":"Item Price","item_date": "Item Date"},inplace=True)
	df = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True)],axis=1)
	df.to_csv("report.csv",index=False)
	totalRevenue = total1
	totalExpenses = total0
	return {"OverallExpenses": totalExpenses,"OverallRevenue": totalRevenue}


def stream_detail(request,pk):
	stream = Match.objects.get(pk=pk)
	context = {
	'stream': stream,
	}
	return  render(request, 'stream_detail.html', context)		


def report(request):
	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			reportForm = form.cleaned_data
			month = reportForm['Month']
			name = reportForm['Name']
			department = reportForm['Department']
			email = reportForm['Email']
			doc = SimpleDocTemplate(month + " report for " + department + ".pdf",pagesize=(1000,1000),
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
			Story=[]
			styles=getSampleStyleSheet()
			styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontSize=20))
			ptext = month + " Report for " + department
			Story.append(Paragraph(ptext, styles["Center"]))
			Story.append(Spacer(60, 60))
			tz_BEY = pytz.timezone('Asia/Beirut') 
			datetime_BEY = datetime.now(tz_BEY)
			Date = date(day=datetime_BEY.day, month=datetime_BEY.month, year=datetime_BEY.year).strftime('%A %d %B %Y')
			styles=getSampleStyleSheet()
			styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY,fontSize=16))
			ptext = '%s' % Date
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext = 'Department of %s' % department
			Story.append(Paragraph(ptext, styles["Justify"]))         
			Story.append(Spacer(40, 40))
			ptext = 'This report comprises of the revenues and expenses for the department of %s:' % department
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(50, 50))
			info = make_table(department,month)
			totalExpenses = info["OverallExpenses"]
			totalRevenue = info["OverallRevenue"]
			with open('report.csv', "r") as csvfile:
				data = list(csv.reader(csvfile))
			all_cells = [(0, 0), (-1, -1)]
			header = [(0, 0), (-1, 0)]
			column0 = [(0, 0), (0, -1)]
			column1 = [(1, 0), (1, -1)]
			column2 = [(2, 0), (2, -1)]
			column3 = [(3, 0), (3, -1)]
			column4 = [(4, 0), (4, -1)]
			column5 = [(5, 0), (5, -1)]
			column6 = [(6, 0), (6, -1)]
			column7 = [(7, 0), (7, -1)]
			column8 = [(8, 0), (8, -1)]
			column9 = [(9, 0), (9, -1)]
			column10 = [(10, 0), (10, -1)]
			table_style = TableStyle([
				('VALIGN', all_cells[0], all_cells[1], 'TOP'),
				('LINEBELOW', header[0], header[1], 1, colors.black),
				('INNERGRID', (0,0), (-1,-1), 1, colors.black),
				('ALIGN', column0[0], column0[1], 'CENTER'),
				('ALIGN', column1[0], column1[1], 'CENTER'),
				('ALIGN', column2[0], column2[1], 'CENTER'),
				('ALIGN', column3[0], column3[1], 'CENTER'),
				('ALIGN', column4[0], column4[1], 'CENTER'),
				('ALIGN', column5[0], column5[1], 'CENTER'),
				('ALIGN', column6[0], column6[1], 'CENTER'),
				('ALIGN', column7[0], column7[1], 'CENTER'),
				('ALIGN', column8[0], column8[1], 'CENTER'),
				('ALIGN', column9[0], column9[1], 'CENTER'),
				('ALIGN', column10[0], column10[1], 'CENTER'),
				('fontSize', column0[0], column0[1], 14),
				('fontSize', column1[0], column1[1], 14),
				('fontSize', column2[0], column2[1], 14),
				('fontSize', column3[0], column3[1], 14),
				('fontSize', column4[0], column4[1], 14),
				('fontSize', column5[0], column5[1], 14),
				('fontSize', column6[0], column6[1], 14),
				('fontSize', column7[0], column7[1], 14),
				('fontSize', column8[0], column8[1], 14),
				('fontSize', column9[0], column9[1], 14),
				('fontSize', column10[0], column10[1], 14),
			])

			colWidths = [
				3.5 * cm,  # Column 0
				3.5 * cm,  # Column 1
				3.5 * cm,  # Column 2
				3.5 * cm,  # Column 3
				3.5 * cm,  # Column 4
				3.5 * cm,  # Column 5
				3.5 * cm,  # Column 6
				3.5 * cm,  # Column 7
				3.5 * cm,  # Column 8
				3.5 * cm,  # Column 9
				3.5 * cm,  # Column 10
			]
			t = Table(data, colWidths=colWidths)
			t.setStyle(table_style)
			Story.append(t)
			Story.append(Spacer(40, 40))
			ptext =  'Overall Revenue made: ' + str(totalRevenue)
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'Overall Expenses cost: ' + str(totalExpenses)
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'Calculated difference (profit): ' + str(totalRevenue - totalExpenses)
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'This report was issued by %s' % name
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			ptext =  'Email: %s' % email
			Story.append(Paragraph(ptext, styles["Justify"]))
			Story.append(Spacer(40, 40))
			doc.build(Story)
			next_id = 1
			if(Report.objects.all()):
				next_id = Report.objects.last().id + 1
			Report.objects.create(id=next_id,Month=month,Name=name,Department=department,Email = email)
			return FileResponse(open(month + " report for " + department + ".pdf", 'rb'), content_type='application/pdf',as_attachment=True)
	form = ReportForm()
	S = Report.objects.all()
	return render(request, 'Report.html', {'form': form,'S':S})

def record_expense(request):
	if request.method == 'POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			expenseForm = form.cleaned_data
			department_expense = expenseForm['department_expense']
			department_name = expenseForm['department_name']
			expense_name = expenseForm['expense_name']
			expense_date = expenseForm['expense_date']
			next_id = 1
			if(Expenses.objects.all()):
				next_id = Expenses.objects.last().id + 1
			Expenses.objects.create(id=next_id,department_expense=department_expense,department_name=department_name,expense_name=expense_name,expense_date=expense_date)
			form = ExpenseForm()
			message = "Reported expense successfully"
			return render(request, 'Record-Expenses.html', { 'form': form, "message": message })
	form = ExpenseForm()
	return render(request, 'Record-Expenses.html', {'form': form})

def matches(request):
	user = request.session['user']
	staff = request.session['staff']
	today=date.today()
	today = datetime.strptime(str(today), '%Y-%m-%d')
	match = Match.objects.all().filter(date__range=[today, "3000-01-01"])
	return render(request,'Matches.html',{ 'user':user, 'match':match, 'staff':staff })

def expenses(request):
	staff = request.session['staff']
	expenses = Expenses.objects.all()
	return render(request,'Expenses.html',{ 'staff':staff ,"expenses":expenses})

def past_matches(request):
	user = request.session['user']
	staff = request.session['staff']
	today=date.today()
	today = datetime.strptime(str(today), '%Y-%m-%d')
	#match = Match.objects.all().filter(date=today)
	match = Match.objects.all().filter(date__range=["1800-01-01", today])
	return render(request,'Past-Matches.html',{ 'user':user, 'match':match, 'staff':staff })

def ticket(request,id):
	print(id)
	user = request.session['user']
	staff = request.session['staff']
	if request.method == 'POST':
		form = GetPrice(request.POST)
		if form.is_valid():
			price = request.POST.get('price')
			zone = request.POST.get('zone')
			if price is not None:
				next_id = 1
				if(Cart.objects.all()):
					next_id = Cart.objects.last().id + 1
				
				Cart.objects.all().filter(item='Tickets'+ str(id) + zone).filter(user_id=user).delete()
				Cart.objects.create(id=next_id,user_id=user,item = 'Tickets'+ str(id) + zone, price = price, amount = 1)
				cart = Cart.objects.all().filter(user_id=user)
				return HttpResponseRedirect('buyA')
				return render(request,'buy.html',{'cart':cart , 'total':price,	"staff":staff})
	request.session['buying'] = True
	match = Match.objects.get(id = id)
	form = GetPrice()
	return render(request,'Tickets.html',{'form':form, 'user':user,"staff":staff, 'match':match})

def player_login(request):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Playerform = form.cleaned_data
			username = Playerform['username']
			password = Playerform['password']
			for e in Player.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.id
					request.session['player'] = True
					player = request.session['player']
					return HttpResponseRedirect('home_main')
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Player-Login.html', {'form': form, 'message':message})
	form = FindForm()
	S = Player.objects.all()
	return render(request, 'Player-Login.html', {'form': form,'S':S})

def player_signup(request):
	if request.method == 'POST':
		form = CreatePlayerForm(request.POST)
		print("test")
		if form.is_valid():
			print("test1")
			Playerform = form.cleaned_data
			name = Playerform['name']
			username = Playerform['username']
			password = Playerform['password']
			confirm_password = Playerform['confirm_password']
			email = Playerform['email']
			gender = Playerform['gender']
			position = Playerform['position']
			photo = Playerform['photo']
			next_id = 1
			if(Player.objects.all()):
				next_id = Player.objects.last().id + 1
			Player.objects.create(id=next_id,name=name,username=username,password=password,confirm_password=confirm_password,email=email,gender=gender,position=position,photo=photo)
			for e in Player.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.id
					request.session['player'] = True
					player = request.session['player']
					return HttpResponseRedirect('home_main')
	form = CreatePlayerForm()
	S = Player.objects.all()
	return render(request, 'Player-Signup.html', {'form': form,'S':S})

def reset_password_player(request):
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			resetForm = form.cleaned_data
			email = resetForm['email']
			new_password = resetForm['new_password']
			confirm_new_password = resetForm['confirm_new_password']
			for e in Player.objects.all():
				if e.email==email:
					e.password = new_password
					e.confirm_password = confirm_new_password
					e.save()
					message = 'Password reset succesfuly'
					form = ResetForm()
					return render(request, 'Reset-Password-Player.html', {'form': form, 'message':message, 'player':player})

	form = ResetForm()
	return render(request, 'Reset-Password-Player.html', {'form': form})

def fan_login(request):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			username = Fanform['username']
			password = Fanform['password']
			for e in Fan.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.id
					request.session['fan'] = True
					fan = request.session['fan']
					return HttpResponseRedirect('home_main')
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Fan-Login.html', {'form': form, 'message':message})
	form = FindForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Login.html', {'form': form,'S':S})

def fan_ticket_login(request,id):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			username = Fanform['username']
			password = Fanform['password']
			for e in Fan.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.id
					request.session['fan'] = True
					if request.session['buying'] is not None:
						return HttpResponseRedirect('ticket('+str(id)+')')
					fan = request.session['fan']
					return render(request, 'HOME.html', { 'user': A.username, 'fan':fan })
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Fan-Login.html', {'form': form, 'message':message})
	form = FindForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Login.html', {'form': form,'S':S})

def fan_signup(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			Fanform = form.cleaned_data
			name = Fanform['name']
			username = Fanform['username']
			password = Fanform['password']
			confirm_password = Fanform['confirm_password']
			email = Fanform['email']
			next_id = 1
			if(Fan.objects.all()):
				next_id = Player.objects.last().id + 1
			Fan.objects.create(id=next_id,name=name,username=username,password=password,confirm_password=confirm_password,email=email)
			for e in Fan.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.id
					request.session['fan'] = True
					fan = request.session['fan']
					return HttpResponseRedirect('home_main')
	form = CreateForm()
	S = Fan.objects.all()
	return render(request, 'Fan-Signup.html', {'form': form,'S':S})

def reset_password_fan(request):
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			resetForm = form.cleaned_data
			email = resetForm['email']
			new_password = resetForm['new_password']
			confirm_new_password = resetForm['confirm_new_password']
			for e in Fan.objects.all():
				if e.email==email:
					e.password = new_password
					e.confirm_password = confirm_new_password
					e.save()
					message = 'Password reset succesfuly'
					form = ResetForm()
					return render(request, 'Reset-Password-Fan.html', {'form': form, 'message':message})

	form = ResetForm()
	return render(request, 'Reset-Password-Fan.html', {'form': form})

def staff_login(request):
	if request.method == 'POST':
		form = FindForm(request.POST)
		if form.is_valid():
			Staffform = form.cleaned_data
			username = Staffform['username']
			password = Staffform['password']
			for e in Staff.objects.all():
				if e.username==username and e.password==password:
					A=e
					request.session['user'] = A.id
					request.session['staff'] = True
					return HttpResponseRedirect('home_staff')
		form = FindForm()
		message = "Incorrect User Name or Password"
		return render(request, 'Staff-Login.html', {'form': form,'message':message})
	form = FindForm()
	S = Staff.objects.all()
	return render(request, 'Staff-Login.html', {'form': form,'S':S})

def reset_password_staff(request):
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			resetForm = form.cleaned_data
			email = resetForm['email']
			new_password = resetForm['new_password']
			confirm_new_password = resetForm['confirm_new_password']
			for e in Staff.objects.all():
				if e.email==email:
					e.password = new_password
					e.confirm_password = confirm_new_password
					e.save()
					message = 'Password reset succesfuly'
					form = ResetForm()
					return render(request, 'Reset-Password-Staff.html', {'form': form, 'message':message})

	form = ResetForm()
	return render(request, 'Reset-Password-Staff.html', {'form': form})

def forgot_password_player(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Player.objects.all():
				if e.email==email:
					A=e
					message_to_send = 'Hello ' + A.username + ',\n\n Please use the link below to reset your email. \n\n http://localhost:8000/reset_password_player'
					send_mail(
    						'Reset Password',
    						message_to_send,
    						'obazarbachi@gmail.com',
    						['obazarbachi@gmail.com'],
    						fail_silently=False,
					)
					message = "email sent to: " + A.email
					form = ForgotForm()
					return render(request, 'Forgot-Password-Player.html', {'form': form, 'message':message})
		form = ForgotForm()
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Player.html', {'form': form,'message':message})
	form = ForgotForm()
	return render(request, 'Forgot-Password-Player.html', {'form': form})

def forgot_password_fan(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Fan.objects.all():
				if e.email==email:
					A=e
					message_to_send = 'Hello ' + A.username + ',\n\n Please use the link below to reset your email. \n\n http://localhost:8000/reset_password_fan'
					send_mail(
    						'Reset Password',
    						message_to_send,
    						'obazarbachi@gmail.com',
    						['obazarbachi@gmail.com'],
    						fail_silently=False,
					)
					message = "email sent to: " + A.email
					form = ForgotForm()
					return render(request, 'Forgot-Password-Fan.html', {'form': form, 'message':message})
		form = ForgotForm()
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Fan.html', {'form': form,'message':message})
	form = ForgotForm()
	return render(request, 'Forgot-Password-Fan.html', {'form': form})

def forgot_password_staff(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			Forgotform = form.cleaned_data
			email = Forgotform['email']
			for e in Staff.objects.all():
				if e.email==email:
					A=e
					message_to_send = 'Hello ' + A.username + ',\n\n Please use the link below to reset your email. \n\n http://localhost:8000/reset_password_staff'
					send_mail(
    						'Reset Password',
    						message_to_send,
    						'obazarbachi@gmail.com',
    						['obazarbachi@gmail.com'],
    						fail_silently=False,
					)
					message = "email sent to: " + A.email
					form = ForgotForm()
					return render(request, 'Forgot-Password-Staff.html', {'form': form, 'message':message})
		form = ForgotForm()
		message = "Email address not  found"
		return render(request, 'Forgot-Password-Staff.html', {'form': form,'message':message})
	form = ForgotForm()
	return render(request, 'Forgot-Password-Staff.html', {'form': form})
		