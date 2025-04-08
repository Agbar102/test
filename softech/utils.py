def strtobool(value: str) -> bool:
    value = value.lower()
    if value in ('y', 'yes', 't', 'true', 'on', '1', 'TRUE', 'True'):
        return True
    elif value in ('n', 'no', 'f', 'false', 'off', '0', 'False', 'FALSE'):
        return False
    raise ValueError(f"Invalid truth value: {value}")