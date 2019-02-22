def search4vowels(phrase:str) -> set:
    """指定された単語内の母音を返す。"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str) -> set:
    """phrase内のlettersの集合を返す。"""
    return set(letters).intersection(set(phrase))
