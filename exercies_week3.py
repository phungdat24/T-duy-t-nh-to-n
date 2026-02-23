#Chương trình nhập vào số nguyên n và in ra ngược lại số nguyên đó:
n=int(input("Nhập số nguyên n: "))
n=str(n)
a=n[::-1]
a=int(a)
print(a)


#Hoán đổi hai số không sử dụng biến tạm thời


a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
#sử dụng toán tử bit XOR
a=a^b
b=a^b
a=a^b
print("Giá trị sau khi hoán đổi: a=",a,"b=",b)


#Kiểm tra xem một số có phải là lũy thừa của 2 hay không
#Sử dụng các toán tử bitwise để xác định xem một số có phải là lũy thừa của 2 hay không.

n=int(input("Nhập số nguyên dương n: "))
if n>0 and (n & (n - 1)) == 0:
    print("True")
else:
    print("False")

#Kết quả phép chia làm tròn xuống:
import math
m=int(input("Nhập số nguyên dương m: "))
n=int(input("Nhập số nguyên dương n: "))
a=math.floor(m/n)
print(a)


#Kết quả phép chia làm tròn lên:
import math
m=int(input("Nhập số nguyên dương m: "))
n=int(input("Nhập số nguyên dương n: "))    
a=math.ceil(m/n)
print(a)


#Even and odd:
x=int(input("Nhập số nguyên dương x: "))
if x%2==0:
    print("Even")
else:
    print("Odd")


#Check negative number:
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if a < 0 and b < 0:
    print("Yes")
else:
    print("No")

#Longer string:
a = input("Nhập chuỗi thứ nhất: ")
b = input("Nhập chuỗi thứ hai: ")
if len(a) > len(b):
    print("True")
else:
    print("False")
    



#triangle
a,b,c = map(int, input("Nhập vào 3 cạnh của tam giác cách nhau bởi dấu cách: ").split())
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")



#Largest of four numbers
a, b, c, d = map(int, input("Nhập vào 4 số nguyên cách nha bởi dấu cách ").split())
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d
print(largest)

#Phân loại tam giác:
a, b, c = map(int, input("Nhập độ dài 3 cạnh của tam giác: ").split())
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")


#Kiểm tra năm nhuận
n=int(input("Nhập vào năm:"))
if (n%4==0 and n%100!=0) or (n%400==0):
    print("Yes")
else:
    print("No")




#Tính số tiền điện 
so=int(input("Nhập số kWh điện đã tiêu thụ: "))
if so <=50 and so >=0:
    print("Số tiền điện phải trả là: ", so*1500)
elif so <=100 and so >=51:
    print("Số tiền điện phải trả là: ", (50*1500)+(so-50)*2000)
else:
    print("Số tiền điện phải trả là: ", (50*1500)+(50*2000)+(so-100)*3000)

#Giải phương trình bậc nhất
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Nghiệm của phương trình là: x =", format(-b/a,".2f"))

# Xếp loại học lực:
diem = float(input("Nhập vào điểm trung bình của học sinh: "))
if diem >=8.0:
    print("Học sinh xếp loại Giỏi")
elif diem >=6.5:
    print("Học sinh xếp loại Khá")
elif diem >=5.0:
    print("Học sinh xếp loại Trung bình")
else:
    print("Học sinh xếp loại Yếu")

#Rounding:
n=float(input("Nhập vào một số thực: "))
a=int(n)
if n >0:
    if n - a >= 0.5:
        print(a + 1,a,a+1, sep=' ') 
    elif n-a==0:
        print(a,a,a, sep=' ')
    else:
        print(a+1,a,a, sep=' ')
else:
    if n - a <= -0.5:
        print(a ,a-1,a-1, sep=' ')
    elif n-a==0:
        print(a,a,a, sep=' ')
    else:
        print(a,a-1,a, sep=' ')


#Phân loại tam giác
a, b, c = map(int, input("Nhập độ dài 3 cạnh của tam giác: ").split())
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
