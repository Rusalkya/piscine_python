"""BMI calculator."""


def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    """Return BMI list from height and weight."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")

    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")

    result = []

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or isinstance(h, bool):
            raise TypeError("height must contain int or float only")
        if not isinstance(w, (int, float)) or isinstance(w, bool):
            raise TypeError("weight must contain int or float only")

        if h <= 0 or w <= 0:
            raise ValueError("height and weight must be positive")

        result.append(w / (h ** 2))

    return result


def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """Return True if BMI is above limit."""
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")

    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("limit must be an integer")

    result = []

    for value in bmi:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("bmi must contain int or float only")

        result.append(value > limit)

    return result


if __name__ == "__main__":
    pass
