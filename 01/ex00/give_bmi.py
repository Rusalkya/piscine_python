"""BMI calculator"""

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("height and weight must be lists")
        
        if len(height) != len(weight):
            raise ValueError(f"height and weight lists must have the same size: {len(height)} vs {len(weight)}")
        
        result = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or isinstance(h, bool):
                raise TypeError(f"height elements must be int or float, got {type(h).__name__}")
            if not isinstance(w, (int, float)) or isinstance(w, bool):
                raise TypeError(f"weight elements must be int or float, got {type(w).__name__}")
            if h <= 0 or w <= 0:
                raise ValueError(f"height and weight must be positive values")
            
            bmi = w / h ** 2
            result.append(bmi)
        
        return result
    
    except (TypeError, ValueError) as e:
        print(f"Error in give_bmi: {e}")
        raise


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError(f"limit must be an integer, got {type(limit).__name__}")
        
        result = []
        for value in bmi:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"bmi elements must be int or float, got {type(value).__name__}")
            
            res = value > limit
            result.append(res)
        
        return result
    
    except TypeError as e:
        print(f"Error in apply_limit: {e}")
        raise


if __name__ == "__main__":
    pass
