a = float(input())
b = float(input())
c = float(input())

highest = 0

if(a >= b and a >= c):
	highest = a
elif(a >= b and a >= c):
	highest = b
else:
	highest = c

print(f"Highest : ", highest)
percentage = ((a+b+c)/300)*100
percentage = round(percentage)
print(f"Percentage : {percentage}")