from datetime import datetime


def date_today():
	
	today=datetime.now().strftime('%Y')
	today=int(today)
	return today

def FRIOUI(frist_name):
	age=int(1991-date_today())
	return "l'age %s est %d"%(frist_name,age)


print(FRIOUI('meher'))

current_day=datetime.now().strftime('%A')

current_date=datetime.now().strftime('%Y/%m/%d %H:%M')

print('{} : date equal {}'.format(current_day,current_date))