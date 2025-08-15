amount = eval(input("Enter amount to deposit: ")) 
print("Here is a breakdown, using PH denomination:") 
#1000
rk = amount / 1000 // 1 * 1000
k = rk / 1000
#500
rfh = (amount - rk) / 500 // 1 * 500
fh = rfh / 500
#200
rth = (amount - (rk + rfh)) / 200 // 1 * 200
th = rth / 200
#100
rh = (amount - (rk + rfh + rth)) / 100 // 1 * 100
h = rh / 100
#50
rft = (amount - (rk + rfh + rth + rh)) / 50 // 1 * 50
ft = rft / 50
#20
rtt = (amount - (rk + rfh + rth + rh + rft)) / 20 // 1 * 20
tt = rtt / 20
#10
rt = (amount - (rk + rfh + rth + rh + rft)) / 10 // 1 * 10
t = rt / 10
#5
rf = (amount - (rk + rfh +rth + rh + rft + rt)) / 5 // 1 * 5
f = rf / 5
#1
o = (amount - (rk + rfh +rth + rh + rft +rt + rf)) // 1


print("1000 -", k)
print("500 -", fh)
print("200 -", th)
print("100 -", h) 
print("50 -", ft) 
print("20 -", tt) 
print("10 -", t)
print("5 -", f) 
print("1 -", o) 
