int=int(input("Enter the value 1-infinte:"))
sum = 0
temp = int

while temp>0:
    digit= temp%10
    digit= digit**3
    sum= sum+ digit
    temp= temp// 10
if int==sum:
    print(int,"is an armstorm number")
else:
      print(int,"is anot an  armstorm number")
