def logger(f):
    import functools
    @functools.wraps(f)
    def wrapper(*args):
        result = f(*args)
        with open("./log.txt", "a") as file:
            file.write(("-" * 20) + "\n")
            file.write("Rubles: " + str(args[0]) + "\n")
            file.write("Currency: " + str(args[2]) + "\n")
            file.write("Result: " + str(result) + "\n")
        return result
    return wrapper


def get_currencies():
    response = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))
    currencies = {}
    for line in response.findall('Valute'):
        currencies.update({line.find('CharCode').text: line.find('Value').text})
    return currencies


def get_currency_value(currencies: dict, currencty_char):
    return float(currencies[currencty_char].replace(",", "."))


@logger
def rubles_to_currency(rubles, currencies, currency_char):
    return rubles / get_currency_value(currencies, currency_char)


if __name__ == "__main__":
    print("Available currencies:")
    currencies = get_currencies()
    currency_chars = list(get_currencies().keys())

    for (i, j) in enumerate(currency_chars):
        print(i + 1, j, sep=": ")

    while True:
        try:
            currency_char = currency_chars[abs(int(input("set: "))) - 1]
        except IndexError:
            print("No such currency")
            continue
        except TypeError:
            print("Are you okay?")
            continue
        break

        while True:
        try:
            rubles = abs(int(input("Rubles: ")))
        except TypeError:
            print("Are you okay?")
            continue
        break
    print(rubles, "RUB =", rubles_to_currency(rubles, currencies, currency_char), currency_char)
