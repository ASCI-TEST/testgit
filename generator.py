#!/usr/bin/python3


manuallist=[1,2,3,4,5]
autolist=[x for x in range(10)]
print('manualist is',manuallist)
print('autolist is',autolist)

# generator

#manuallist=(1,2,3,4,5)
#print('first item is ',next(manuallist))
#print('next item is ',next(manuallist))

# generators are shorthand for iterators. you can build with () instead of []
g=(x for x in range(10))
print('first item is ',next(g))
print(next(g))
print("ok. here's the rest as a list")
print(list(g))

def infinite_gen():
        n=0
        while True:
                yield n
                n=n+1
print("Creating infinite generator: ",end="")
h=infinite_gen()
print(next(h))
print(next(h))
print(next(h))

for i in [ ['firstword','second'],['firstof2','secondof2']]:
	print('i is',i)
for i in ( ['firstword','second'],['firstof2','secondof2']):
	print('i is',i)



"""
print('manualist is',manuallist)
print('autolist is',autolist)
"""

