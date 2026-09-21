import secrets
import string


def generate_code():
    characters = string.ascii_lowercase + string.digits

    groups = []

    for _ in range(4):
        group = "".join(secrets.choice(characters) for _ in range(3))
        groups.append(group)

    return "_".join(groups)