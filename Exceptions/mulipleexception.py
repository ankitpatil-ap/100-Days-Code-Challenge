import logging
values = [10, 2,4,5,3,"Hello",22]

for value in values:
    try:
        print(10/int(value))
    except (ValueError,ZeroDivisionError) as e:
        pass
    except AttributeError as e:
        print("Hello World")
        continue
    except Exception as e:
        logging.exception(e)
        
