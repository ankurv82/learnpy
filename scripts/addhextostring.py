#!/bin/python
var1 = 'HelloWorld'

print var1
print "----------------"  

##f= open("av1.txt","w+")

i=0
str=""
while i < len(var1):
    str+='0x'+var1[i]+var1[i+1]
    i += 2

print str
