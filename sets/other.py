# s1={"one","two","three","four","five"}#create a set value
# s2={"one","three"}#create another set value

# #subset
# print(s1.issubset(s2))#check subset using issubset() method
# print(s2.issubset(s1))#check subset using issubset() method
# print(s1 < s2)#check subset using < operator
# print(s2 < s1)#check subset using < operator
# print(s2 <= s1)#check subset using <= operator

# #superset
# print(s1.issuperset(s2))#check superset using issuperset()
# print(s2.issuperset(s1))#check superset using issuperset() method
# print(s1 > s2)#check superset using > operator
# print(s2 > s1)#check superset using > operator
# print(s1 >= s2)#check superset using >= operator

#disjoint
s3={6,7,8}
s4={8,9,10}
print(s3.isdisjoint(s4))#check disjoint using isdisjoint() method