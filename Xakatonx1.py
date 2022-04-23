
a = input(str("введите три слова:"))
b = input(str("введите три слова:"))
c = input(str("введите три слова:"))
d = (' ').join([a,  b,  c])
print(d)

if len(a + b + c) >= 20:
	if len(a) > len(b) and len(a) > len(c):
		print(a.upper())
	elif len(b) > len(a) and len(b) > len(c):
		d.upper()
		print(b.upper())
	else:
		print(c.upper())

elif len(a + b + c) <= 20 and d.isalpha():
	print('Число')
