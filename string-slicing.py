#SLICING = create a substring by extracting elements from another string
# indexing[] or slicing()
# [start:stop:step]

name = 'reicen cutie'
first_name = name[:6]
last_name = name[7:]
jeje_name = name[:6:2]
jeje_full = name[::2]
reversed_name = name[::-1]


print(first_name+" "+last_name)
print(jeje_name)
print(jeje_full)
print(reversed_name)

#SLICING

website1 = 'https://twitter.com'
website2 = 'https://facebook.com'
website3 = 'https://instagram.com'
webslice = slice(8,-4)

print(website1[webslice])
print(website2[webslice])
print(website3[webslice])