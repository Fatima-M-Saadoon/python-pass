"""
Instructions:

1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:
    def reverse(self, *, to_be_reversed: str = None):
        raise NotImplemented('This method need to be implemented')
       
    class ReversedString(StringOperations)
       def reverse(string):
        string = "".join(reversed(string))
    return string
s = "butterfly"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))
