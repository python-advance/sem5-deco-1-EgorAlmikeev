def logger(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("./log.txt", 'a') as file:
            file.write("=" * 20)
            file.write("\n")
            file.write("args: " + str(args))
            file.write("\n")
            file.write("result: " + str(result))
            file.write("\n")
        return result
    return wrapper


@logger
def make_calcs(operation, arg1, arg2):
    result = None
    if operation == "+":
        result = arg1 + arg2
    elif operation == "-":
        result = arg1 - arg2
    elif operation == "*":
        result = arg1 * arg2
    elif operation == "/":
        result = arg1 / arg2

    return result


if __name__ == "__main__":
    print(make_calcs("+", 1, 2))
