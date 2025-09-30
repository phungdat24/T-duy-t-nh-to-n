
#W2A3:
a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
print(f"Tổng của {a} và {b} là: {a+b}")
print(f"Hiệu của {a} và {b} là: {a-b}")
print(f"Tích của {a} và {b} là: {a*b}")
c=a/b 
print(f"Thương của {a} và {b} là:", (round(float(c),2)))
print(f"Phần dư của {a} và {b} là: {a%b}")
print(f"Phần nguyên của {a} và {b} là: {a//b}")

#W2A4
a,b,c,d,e,f=(input("Nhập vào 6 số nguyên cách nhau bởi dấu cách: ")).split()
a,b,c,d,e,f=int(a),int(b),int(c),int(d),int(e),int(f)
k=((a+b+c)+(d+e)*2+f*3)/10
print("Điểm trung bình của bạn là: ", round(k,2))

#W2A5
a,b=input("Nhập vào 2 số nguyên cách nhau bởi dấu cách: ").split()
a,b=int(a),int(b)
print("Kết quả của phép toán a mũ b là: ", a**b)

#W2A6
a=input("Nhập vào chuỗi ký tự: " )
print("kí tự in hoa tương ứng: " ,a.upper())

#W2A7
A=((13**2)*3) +5
B=13**2*3 +5
print("Kết quả của biểu thức A là: ", A)
print("Kết quả của biểu thức B là: ", B)
#Hai biểu thức A và B khác nhau vì biểu thức A có dấu ngoặc nên sẽ ưu tiên tính trong ngoặc trước, còn biểu thức B thì không có dấu ngoặc nên sẽ thực hiện phép tính theo thứ tự từ trái sang phải. 


#W2A8
a=float(input("Nhập vào nhiệt độ Celcius: "))
print(f"Nhiệt độ Fahrenheit tương ứng là: {round((a*9/5)+32,2)} độ F")

#W2A9
a=float(input("Chiếc đồng hồ có giá trị là:"))
print(f"Tổng số tiền mà Đạt phải trả để mua được chiếc đồng hồ là: {round((a*1.4)+10,2)} USD")


#W2A11
a=int(input("Nhập vào số giờ: "))
b=int(input("Nhập vào số phút: "))
print(f"{a}h{b}p tương đương với {a*3600 + b*60}s")

#W2A12
n=int(input("Nhập vào độ dài khối Rubik: "))
print(f"Số lượng miếng dán riêng lẻ cần thiết để bọc khối Rubik là: {6*n**2}")

#W2A13
a=int(input("Nhập vào số nguyên dương a: "))
b=int(input("Nhập vào số nguyên dương b: "))
print(f"Chữ số hàng đơn vị của tổng a+b là: {(a+b)%10}")

#W2A14
a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
a=a+b
b=a-b
a=a-b
print(f"Giá trị mới của a là: {a}")
print(f"Giá trị mới của b là: {b}")

#Cách 2 của W2A14
a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
a,b=b,a
print(f"Giá trị mới của a là: {a}")
print(f"Giá trị mới của b là: {b}")


#W2A15
a=int(input("Nhập vào số nguyên dương n: "))
if a <= 0:
    print("Vui lòng nhập số nguyên dương")
else:
    print(f'Số sao thứ {a} là: {1+6*a*(a-1)}')


