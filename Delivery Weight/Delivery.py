def cost_ogs(weight):
  if weight <= 2:
   cost = weight * 1.5 + 20
   return cost
  elif (weight > 2) and (weight <= 6):
   cost = weight * 3 + 20
   return cost
  elif (weight > 6) and (weight <= 10):
    cost = weight * 4 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
    return cost

def cost_od(weight):
  if weight <= 2:
   cost = weight * 4.5
   return cost
  elif (weight > 2) and (weight <= 6):
   cost = weight * 9 
   return cost
  elif (weight > 6) and (weight <= 10):
    cost = weight * 12 
    return cost
  else:
    cost = weight * 14.25 
    return cost

premium = 125

def cheapest(weight):
  if cost_ogs(weight) < premium and  cost_ogs(weight) < cost_od(weight):
    return "Plain Ground Shipping is your cheapest option! It costs: $" + str(cost_ogs(weight))
  
  elif cost_od(weight) < premium and cost_od(weight) < cost_ogs(weight):
    return "Drone Shipping is your cheapest option! It costs: $" + str(cost_od(weight))

  else:
    return "Premium Ground Shipping is your cheapest option! It costs: $" + str(premium)

print(cheapest(4.8))

print(cheapest(41.5))