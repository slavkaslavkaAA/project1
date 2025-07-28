# Sal's Shipping 

#Ground Shipping Cost
weight = 4.8

if weight <= 2:
  cost = weight * 1.5 + 20 
  print("Your weight would be cost " + str(cost) + '$')
elif weight >= 2 and weight <= 6:
  cost = weight * 3.0 + 20
  print("Your weight would be cost " + str(cost) + '$')
elif weight >= 6 and weight <= 10:
  cost = weight * 4.0 + 20 
  print("Your weight would be cost " + str(cost) + '$')
elif weight >= 10:
  cost = weight * 4.75 + 20
  print("Your weight would be cost " + str(cost) + '$')
else: 
  print("Your weight is too high")

# Ground Shipping Premium Cost

groundShippingPremiumCost = 125 

print("Ground Shipping Premium Cost is " + str(groundShippingPremiumCost) + '$')


#Drone Shipping 

droneWeight = 41.5

if droneWeight <= 2:
  droneCost = droneWeight * 4.5 + 0
  print("Your droneShipping cost will be " + str(droneCost) + '$')
elif droneWeight >= 2 and droneWeight <= 6:
  droneCost = droneWeight * 9.0 + 0
  print("Your droneShipping cost will be " + str(droneCost) + '$')
elif droneWeight >= 6 and droneWeight <= 10:
  droneCost = droneWeight * 12.0 + 0
  print("Your droneShipping cost will be " + str(droneCost) + '$')
elif droneWeight >= 10:
  droneCost = droneWeight * 14.25 + 0
  print("Your droneShipping cost will be " + str(droneCost) + '$')
else:
  print("Your weight is too high")
