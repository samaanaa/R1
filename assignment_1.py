
aString=input("If you use SI to input your weith and hight please write yes else no")
a=format(aString)
print(a)
if a!=yes:

wString=input("enter your weith in kg")
hString=input("enter your hight in cm")
w=float(wString)
h=float(hString)

bmi=w/h**2
if bmi<18.5:
    print("underweith")
elif 18.5<bmi<25:
    print(Normal)
elif 25<bmi<30:
    print("Overwieth")
else:print("Obesity")


