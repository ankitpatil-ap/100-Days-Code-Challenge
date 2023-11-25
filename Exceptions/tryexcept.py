#print(10/0)
#print("Hello")
# File "c:\Users\ankit\OneDrive\Desktop\100 Days Code Challenge\100-Days-Code-Challenge\Exceptions\tryexcept.py", line 7, in <module>
#    print(10 / 0)
#          ~~~^~~
#ZeroDivisionError: division by zero
#As you can see the program will stop execution after an error and hello will never gonna print 
#so to handle such things we use exceptions

try:
    print(10 / 0)
except:
    pass

    #print("zero division error")

print("hello")
#hello
#zero division error
#hello