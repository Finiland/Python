import datetime

Hourinput = int(input("Hours: "))
Minuteinput = int(input("Minutes: "))
maininputs = datetime.timedelta(hours=(Hourinput), minutes=(Minuteinput))
print(maininputs)
print("These next will be added into the value")
#qwe1 = int(input("Hours: ")) /// This line was just for the testing purposes.
Addminutes = int(input("Minutes: "))
Addseconds = int(input("Seconds: "))
addminutesandseconds = datetime.timedelta(minutes=(Addminutes), seconds=(Addseconds))
lastvalue = maininputs + addminutesandseconds
utctime = (datetime.timedelta(hours=2)) #Now it is going to minus 2 hours from Finnish time to get UTC 00:00 time (aka London time, GMT 0)
print(lastvalue - utctime,("This is in British time."))
print(lastvalue,("This is in Finnish time."))
