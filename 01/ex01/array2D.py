def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be int")

    if len(family) == 0:
        raise ValueError("family cannot be empty")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")

    row_size = len(family[0])

    if not all(len(row) == row_size for row in family):
        raise ValueError("all rows must have the same size")

    print(f"My shape is : ({len(family)}, {row_size})")

    fami = family[start:end]

    if len(fami) > 0:
        new_shape = (len(fami), len(fami[0]))
    else:
        new_shape = (0, 0)

    print(f"My new shape is : {new_shape}")

    return fami
