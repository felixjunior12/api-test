def to_camel_case(s: str) -> str:
    parts = s.replace('-', ' ').replace('_', ' ').split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])