__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even_sum = sum(filter(lambda x: x % 2 == 0, arr))
    odd_sum = sum(filter(lambda x: x % 2 != 0, arr))
    if even_sum and odd_sum:
        return even_sum / odd_sum
    return 0
