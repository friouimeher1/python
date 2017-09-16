#

#

#


def alive_day(name,age):

	day_alive=('%s alive %d day'%(name,age*365))
	return day_alive

age=input('Give me your Age \n')

age =int(age)

name=input('Give me Name\n')

print(alive_day(name,age))

