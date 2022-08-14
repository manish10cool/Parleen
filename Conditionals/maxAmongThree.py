a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
	print(f"Max among {a}, {b}, {c} : {a}")
elif b >=a and b >=c:
	print(f"Max among {a}, {b}, {c} : {b}")
else:
	print(f"Max among {a}, {b}, {c} : {c}")



