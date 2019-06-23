counter1=0
counter2=5
while(counter1 < counter2):
  star=""
  n = counter2
  while(n>counter1):
     star=star+ "*"
     n-=1  
  print(star)
  counter1+=1