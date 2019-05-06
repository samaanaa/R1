
aString=input("If you use metric units to input your weith and hight please write 1 if you use imperial unics please write 2")
a=int(aString)
print(a)

if a==1:

   wString=input("enter your weith in kg")
   hString=input("enter your hight in m")
   w=float(wString)
   h=float(hString)
   bmi=w/(h**2)
elif a==2:
    wString = input("enter your weith in lb")
    hString = input("enter your hight in in")
    w = float(wString)
    h = float(hString)
    bmi = (w / h ** 2) * 703


if bmi<18.5:
    print("underweith")
elif 18.5<bmi<25:
    print("Normal")
elif 25<bmi<30:
    print("Overwieth")
else:
    print("Obesity")



