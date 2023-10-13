i=10
str1 , str2 = 'MEGH is in IT','YASH is in business'
print(  str1,   str1[ 0 : 100],   str1[5 : 10],      str1[i:i+3]      ,sep='\n')

string1 = "{2}{0}{1}".format('a ','b ','c ')
print(string1)


k = 'NOTHING is ordinary'
print(k.upper())
print(k.capitalize())
print(len(k))
print(k.title())

t=k.split()
print(t)

k1="---".join(t)
print(k1)