__all__ = (
    'seconds_to_str',
)


def f(n: int, postfix: str) -> str:
    if n < 10:
        return "0" + str(n) + postfix
    return str(n) + postfix


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds == 0:
        return '00s'
    _seconds = seconds % 60
    minutes = (seconds - _seconds) // 60
    _minutes = minutes % 60
    hours = (minutes - _minutes) // 60
    _hours = hours % 24
    days = (hours - _hours) // 24
    flag = False
    result = ""
    for n, postfix in [(days, "d"), (_hours, "h"), (_minutes, "m"), (_seconds, "s")]:
        if n != 0:
            flag = True
        if flag:
            result += f(n, postfix)
    return result
