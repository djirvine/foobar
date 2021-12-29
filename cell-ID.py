def answer2(x, y):
  z = x*(x+1)/2 + y*(y-1)/2 + (x-1)*(y-1)
  return str(z)

def answer(x, y):
  z = ((x+y-1)*(x+y-2))/2 + x
  return str(z);


for i in range(5):
    for j in range(5):
        print(answer2(i,j), answer(i,j))
