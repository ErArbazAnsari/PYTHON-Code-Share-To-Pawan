"""Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""
# print("Hello")
# print('Hello')
#
# #Assign String to a Variable
# a='arbaz'
# print(a)
#
# # Multiline Strings
# arbaz="""Hello world! my name is
# arbaz ansari. i am 17 years old. my age is 18. i am currently persuing b.tech
# cse."""
#
# print(arbaz)
#
#
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

a = "Hello, World!"
print(a[0:100])

arbaz='india'
for x in arbaz:
  print(x,end="")
a = "Hello, World!"
print("\n")
print(len(a))


# Check String
var0="India is the best country"
if "India" in var0:
    print("true, India is present in this paragraph.")

#Not in
var0="India is the best country"
if "India" not in var0:
    print("true, India is present in this paragraph.")

