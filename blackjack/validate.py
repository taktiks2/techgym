def valid_decimal(string: str):
    if string.isdecimal():
        return True
    return False


def valid_alpha(string: str):
    if string.isalpha():
        return True
    return False


def valid_count(string: str, num: int):
    string_list: list = string
    if len(string_list) == num:
        return True
    return False


def valid_alnum(string: str):
    if string.isalnum():
        return True
    return False


def valid_multiple_10(num: int):
    if num % 10 == 0:
        return True
    return False


def main():
    pass


if __name__ == '__main__':
    main()