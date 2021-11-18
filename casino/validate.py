def valid_integer(string: str, max: int, min: int = 1):
    '''引数の文字列が指定した範囲内の整数か判定
    return: bool
    '''
    if string.isdigit():
        if min <= int(string) <= max:
            return True
        else:
            return False
    else:
        return False