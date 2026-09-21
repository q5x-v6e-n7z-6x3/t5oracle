from t5oracle import generate_code


def test_generate_code_returns_string():
    code = generate_code()
    assert isinstance(code, str)


def test_generate_code_has_correct_format():
    code = generate_code()

    parts = code.split("_")

    assert len(parts) == 4
    assert all(len(part) == 3 for part in parts)


def test_generate_code_uses_valid_characters():
    code = generate_code()

    cleaned = code.replace("_", "")

    assert cleaned.isalnum()
    assert cleaned == cleaned.lower()