SportClubManagement-EECE430-Group 10

Django SportsClub Management System
Steps to Run the Project 

Step 1 - Django Environment Preparation 
(please go to step 2 if you already have django)
 
Steps to install Django2.0.1 with Python3.6.4 on windows 64bits
C:\>pip3 install virtualenvwrapper-win
C:\>mkvirtualenv my_env		
Note that you can replace my_env with the environment you are working on

This will create an environment to run Django. You can run the following commands on the environment:
1.	workon: lists available virtual environment , because you can run many mkvirtualenv
2.	workon env_name:  to activate specific environment
3.	deactivate: to exit the virtual environment
4.	rmvirtualenv env_name: to remove specific environment

C:\>workon my_env
(my_env) C:\>pip3 install django

 
Step 2 - Clone the repository
 
(my_env) C:\>git clone https://github.com/Spring21-22Group10/SportsClubManagementApp/
(my_env) C:\>cd SportsClubManagementApp

 
Step 3 - Running the project

To run the project, you need to install some libraries:
pip install pandas
pip install reportlab
pip install django-embed-video
pip install datetime
pip install pytz
pip install csv
pip install pillow
pip install django-environ

if needed, the following are migrations steps:
(my_env) C:\> python manage.py migrate
(my_env) C:\> python manage.py makemigrations app1
(my_env) C:\> python manage.py migrate

finally:
(my_env) C:\>python manage.py runserver 0.0.0.0:8000 

Open any browser and type: Your_computer_ip_address:8000 Or localhost:8000 

Congrats! You have the project running on your computer

username and passwords needed:
to log in as staff:
username: omar
password: 1234

note: you can create accounts for fans and players.