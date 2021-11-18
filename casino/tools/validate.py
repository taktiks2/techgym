def valid_integer(string: str, max: int, min: int = 1):
    '''引数の文字列が指定した範囲内の整数か判定
    return: bool
    '''
    if string.isdigit():
        if min <= int(string) <= max:
            return True
        else:
            print(f'※{min}から{max}の範囲で入力してください')
            return False
    else:
        print('※数字で入力してください')
        return False