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
    

def valid_list(string: str, target: list):
    '''引数の文字列が指定したリスト内にあるかどうかを判定
    return: bool
    '''
    if string in target:
        return True
    else:
        print('※入力した情報が間違っています')
        return False
    