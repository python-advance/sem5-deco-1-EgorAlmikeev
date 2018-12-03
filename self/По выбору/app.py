# задание по выбору номер 3

def logger(func):
    import datetime
    with open("log.txt", "a") as file:
        file.write("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " : " + func.__name__ + "\n")
    return func
