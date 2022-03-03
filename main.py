num=int(input("Enter the four digits number:"))

rem1=num%10
var1=num//10

rem2=var1%10
var2=var1//10

rem3=var2%10
var3=var2//10

reverse_num=(rem1*1000)+(rem2*100)+(rem3*10)+(var3)
print(reverse_num)

