#W5A1:  
def find_max(a,b):
    return a if a>b else b
a=int(input("Nhập vào số nguyên a: "))
b=int(input("Nhập vào số nguyên b: "))
print(max(a,b))

#W5A2:
c=0
def swap(a,b):
    return b,a
a=int(input("Nhập vào số nguyên a: "))
b=int(input("Nhập vào số nguyên b: "))
print(swap(a,b))

#W5A3:
import math
def is_prime(n):
    if n<2:
        return False
    if n>=2:
        for i in range (2, int(math.sqrt(n)+1)):
            if n%i ==0:
                return False
        return True
n=int(input("Nhập vào số tự nhiên n: "))
print(is_prime(n))

#W5A4:

def is_perfect_number(n):
    if n<=1:
        return False
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n
n=int(input("Nhập vào số nguyên n: "))
print(is_perfect_number(n))

#W5A5:
def find_first_index(lst,k ):
    for i in range(len(lst)):
        if lst[i] ==k:
            return i+1
    return -1
lst=list(map(int,input("Nhập vào chuỗi các số:").split()))
k=int(input("Nhập vào số k:"))
print(find_first_index(lst,k))

#W5A6:

def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result

while True:
    n=int(input("Nhập vào số nguyên dương n: "))
    if n<0:
        print("Vui lòng nhập lại với n nguyên dương")
    else:
        break
print(factorial(n))

#W5A7:
def may_tinh_bo_tui(num1, num2, operat):
    if operat == "+":
        return "{:.2f}".format(num1+num2)
    elif operat == "/":
        if num2 ==0:
            print("Lỗi phép chia cho không")
            return None
        return "{:.2f}".format(num1/num2)
    elif operat == "*":
        return "{:.2f}".format(num1*num2)
    elif operat == "-":
        return "{:.2f}".format(num1-num2)
    else:
        print("Toán tử không hợp lệ")
    return None
num1_str,operat,num2_str=input("Nhập vào phép toán: ").split()
num1 = float(num1_str)
num2=float(num2_str)
print(may_tinh_bo_tui(num1, num2,operat))


#W5A8:
def khoang_cach_haming(a,b):
    xor= a^b
    return bin(xor).count('1')
a,b=map(int, input("Nhập vào hai số a, b: ").split())
print(khoang_cach_haming(a,b))

#W5A9:
def tong_chu_so(n):
    return sum(int(i) for i in str(n))
while True:
    n=int(input("Nhập vào số nguyên dương: "))
    if n<=0:
        print("Vui lòng nhập vào số nguyên dương")
    else:
        break
print(tong_chu_so(n))

#W5A10:

def is_isomorphic(a,b):
    map_a_to_b={}
    map_b_to_a={}
    for char_a, char_b in zip(a,b):
        if char_a in map_a_to_b:
           if map_a_to_b[char_a] != char_b:
               return False
        else:
            if char_b in map_b_to_a:
                return False
            map_a_to_b[char_a] = char_b
            map_b_to_a[char_b] = char_a
    return True
           
while True:
    a,b=input("Nhập vào hai từ: ").split()
    if len(a)!=len(b):
        print("Vui lòng nhập hai từ có độ dài bằng nhau.")
    else:
        break
print(is_isomorphic(a,b))


