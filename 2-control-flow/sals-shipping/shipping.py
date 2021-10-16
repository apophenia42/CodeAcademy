#Sals-Shipping
#Apophenia42


weight = 41.5
cost = 0.0

#Ground shipping
if weight <= 2.0:
  cost = 20 + (weight * 1.5)
elif weight > 2.0 and weight <= 6.0:
    cost = 20 + (weight * 3.0)
elif weight > 6.0 and weight <= 10.0:
    cost = 20 + (weight * 4.0)
elif weight > 10.0:
    cost = 20 + (weight * 4.75)
    
#Ground shipping print
cost = round(cost, 2)
cost = format(cost, '.2f')
print("Ground shipping cost: $", cost)

#Premium shipping print
print("Premium shipping cost: $", format(125, '.2f'))

#Drone shipping
if weight <= 2.0:
  cost = weight * 4.5
elif weight > 2.0 and weight <= 6.0:
    cost = weight * 9.0
elif weight > 6.0 and weight <= 10.0:
    cost = weight * 12
elif weight > 10.0:
    cost = weight * 14.25 
    
    
#Drone shipping print
cost = round(cost, 2)
cost = format(cost, '.2f')
print("Drone shipping cost: $", cost)


