student_id = {101 , 102 ,103 ,105, 104 , 112 ,134}
print('student_ID:' , student_id)

student_id = {101 , 101 , 105, 102 ,103 ,105, 104 , 112 ,134}
print('student_ID:' , student_id)

#using add () method
numbers = {11,12,13,14,14,23}
print('initial Set:', numbers)
numbers.add(115)
print('updated Set:', numbers )

#update set() method

companies = {'bmw' , 'Tesla', 'V8'}
car_companies = {'Bravian', 'Tes', 'Toyota'}
companies.update(car_companies)
print(companies)

#remove set()
companies.discard('Tes')
print('latest:',companies)

#mathematical operations using set()
#union of two sets
A =  { 1 ,3 , 5}
B =  { 0 ,2 , 4}
print('union using |:', A | B)
print( A.union (B))

A =  { 1 ,3 , 5}
B =  { 0 ,2 , 4}
print('intersection using &:', A & B)

A =  { 1 ,3 , 5}
B =  { 0 ,2 , 4}
print('diffrence using |:', A - B)

