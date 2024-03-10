capital_city = {"Kenya": "Nairobi", "Uganda": "kampala", "Italy": "Rome", "England": "London"}
print(capital_city.keys())

capital_city["japan"]= "Tokyo"
print("updated Dictionary: ", capital_city)
print(capital_city["England"])
del capital_city["Uganda"]

#dictionary Membership Test

squares ={1: 1 , 3: 9 ,5 : 25 , 7 : 49 , 9 : 81}
print(5 in squares) #prints true
print(7 in squares) #prints true
 
 # membership test for key only not value
print(49 in squares) #prints false

squares = {1: 1 , 3: 9 ,5 : 25 , 7 : 49 , 9 : 81}
for i in squares:
    print(squares[i])