values = [10, 2,4,5,3,22]

for value in values:
    try:
        print(int("Hello"))
    except ValueError as e:
        print(str(e))

'''
invalid literal for int() with base 10: 'Hello'
invalid literal for int() with base 10: 'Hello'  
invalid literal for int() with base 10: 'Hello'  
invalid literal for int() with base 10: 'Hello'  
invalid literal for int() with base 10: 'Hello'  
invalid literal for int() with base 10: 'Hello' '''