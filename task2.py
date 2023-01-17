h = [0]
for i in range (1, 1000):
  for j in ranhge (1,1000):
    z = i*j
    if str(z) == str(z)[::-1]:
      if z > h[0]:
        h.append(z)
        #print(z)
h.sort()
print(h[-1])
