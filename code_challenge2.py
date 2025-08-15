amount = eval(input("Enter amount to deposit: ")) 

#1000
p1000 = amount  // 1000
amount = amount % 1000
#500
p500 = amount // 500
amount = amount % 500
#200
p200 = amount // 200
amount = amount % 200
#100
p100 = amount // 100
amount = amount % 100
#50
p50 = amount // 50
amount = amount % 50
#20
p20 = amount // 20
amount = amount % 20
#10
p10 = amount // 10
amount = amount % 10
#5
p5 = amount // 5
amount = amount % 5
#1
p1 = amount // 1

print("Here is a breakdown, using PH denomination:") 
print("1000 -", p1000)
print("500 -", p500)
print("200 -", p200)
print("100 -", p100) 
print("50 -", p50) 
print("20 -", p20) 
print("10 -", p10)
print("5 -", p5) 
print("1 -", p1) 
