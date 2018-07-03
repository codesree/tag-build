from django.test import TestCase

# Create your tests here.

var1 = None
var2 = 'PROCEED'

if var1 is not None:
    print("var1",type(var1))
elif var2 is not None:
    print("var2",type(var2))

