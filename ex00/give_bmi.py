def valid_input(height: list, weight: list) -> bool:
    """Check is input is int or float"""
    for h in height:
        if not isinstance(h, (int, float)) or h <= 0:
            return False
    for w in weight:
        if not isinstance(w, (int, float)) or w <= 0:
            return False
    return True


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """Calculate BMI values based on given height and weight"""
    try:
        if len(height) != len(weight):
            raise AssertionError("Input len don't match")
        if not valid_input(height, weight):
            raise AssertionError("Input must be valid")
        bmi_values = []
        for h, w in zip(height, weight):
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except Exception as error:
        print("An error ocurred:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if BMI is above limit"""
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be int")
        result = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("BMI value must be int or float")
            result.append(value > limit)
        return result
    except Exception as error:
        print("An error occurred:", error)
        return []
