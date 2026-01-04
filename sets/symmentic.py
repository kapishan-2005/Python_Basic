#symmetric difference of sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = s1.symmetric_difference(s2) #using symmetric_difference() method
print(s3) #print set after symmetric difference

s4 = s1 ^ s2 #using ^ operator
print(s4) #print set after symmetric difference

