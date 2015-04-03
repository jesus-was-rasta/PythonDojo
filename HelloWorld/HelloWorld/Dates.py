#Exercise: days until my birthday
#Learnt: datetime

#importing class datetime
import datetime

#today
currentDate = datetime.date.today()

#formatting dates
#print (currentDate.strftime('%d %m %Y'))    # 03 04 2015
#print (currentDate.strftime('%A %d %B %Y')) #Friday 03 April 2015

birthDateString = input ("What is your birth date (dd-mm-yyyy)?")
birthDate = datetime.datetime.strptime(birthday, "%d-%m-%Y").date()
#nextBirthday = ?