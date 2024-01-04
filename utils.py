from caseconverter import snakecase


def to_snakecase(original: dict) -> dict:
    """
    Changes the keys of a dictionary to snake_case.
    """
    new = {snakecase(key): value for key, value in original.items()}
    for key, value in new.items():
        if isinstance(value, dict):
            new[key] = to_snakecase(value)
    return new


def update_dictionary(original: dict, new: dict) -> dict:
    """
    Recursively merges the new dictionary into the original dictionary overwriting existing values.
    """
    for key, value in new.items():
        if key in original and isinstance(original[key], dict) and isinstance(value, dict):
            update_dictionary(original[key], value)
            continue

        original[key] = value
    return original
