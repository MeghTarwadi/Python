#empty set

mt=set()
s1={'Yash',1,2,3,4,5,'Megh',2.5,1,2}
# print(s1)
s2={5,4,1,2,3,2.6,'Yash','yash',5}
# print(s2)

print(s1.union(s2))
# s1=s1.union(s2)
# print(s1)

print(s1.intersection(s2))
# s1=s1.union(s2)
# print(s1)

s3=s1.intersection(s2)

print(s1-s3)
