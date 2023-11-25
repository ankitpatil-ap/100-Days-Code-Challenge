import logging
values = [10, 2,4,5,3,22]

for value in values:
    try:
        print(int("Hello"))
    except ValueError as e:
        print(str(e))
    except ZeroDivisionError as e:
        pass
    except Exception as e:
        logging.exception(e)