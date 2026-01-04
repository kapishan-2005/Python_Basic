num = {"one", "two", "three"}#create a set value
num.add("four")#add element using add() method
print(num)#print set after adding element

num_odd = {1, 3, 5}
num_even = {2, 4, 6}
print(num_odd)
num_odd.update(num_even)#add multiple elements using update() method
print(num_odd)#print set after adding multiple elements
