def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Function to calculate the bmi given the height and weight
    :param height: list of heights in centimeters
    :param weight: list of weights in kilograms
    :return list of bmi values
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("Height and weight must be the same length")
    bmi = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight must contain only int or float")
        if h == 0:
            raise ZeroDivisionError("Height can't be zero")
        bmi.append(w / (h * h))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Function that applies the given limit to the given bmi array.
    :param bmi: list of bmi values
    :param limit: maximum bmi value
    :return list of bools if bmi values exceed limit"""
    result = []
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list")
    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer")
    if len(bmi) == 0:
        return result
    for bmi_value in bmi:
        if not isinstance(bmi_value, (int, float)):
            raise TypeError("BMI list must contain only numbers")
        result.append(bmi_value > limit)
    return result
