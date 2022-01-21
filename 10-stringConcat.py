from pickletools import string1


x = 'string1'
y= 'string2'
z = 'string3'

print(len(''))
concatStr= x+' '+y+' '+' '+z  # it will concatenate two string

print(concatStr)
concatStrWithTemplateLiteral = f'{x} {y} {z}'

print(concatStrWithTemplateLiteral)
