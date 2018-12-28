# задание по выбору номер 3

def logger(func):
    import datetime
    import functools
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now()
        func(*args, **kwargs)
        time = datetime.datetime.now() - time
    
        with open("log.txt", "a") as file:
            file.write(str(func.__name__) + ": " + str(time) "\n")
            
    return wrapper
