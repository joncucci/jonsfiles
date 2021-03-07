
routes = []
sticks = 21\


#while sticks > 21:
    



for a in range(1,4):
   for b in range(1,4):
       for c in range(1,4):
           for d in range(1,4):
               for e in range(1,4):
                   for f in range(1,4):
                       for g in range(1,4):
                           new_route = [a,b,c,d,e,f,g]
                           routes.append(new_route)

print(routes)