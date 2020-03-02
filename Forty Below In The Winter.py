x = input()
if x[len(x) - 1] == 'C':
   c = x[0:len(x) - 1]
   c1 = float(c)
   f = (c1 * 9) / 5 + 32
   print(str(f) + 'F')
elif x[len(x) - 1] == 'F':
   f = x[0:len(x) - 1]
   f1 = float(f)
   c = ((f1-32) * 5) / 9
   print(str(c) + 'C')
