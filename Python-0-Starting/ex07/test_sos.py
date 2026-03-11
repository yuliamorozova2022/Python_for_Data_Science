from sos import validate_input, convert_to_morse


def test_validate_input():
    """Checks if function correctly validates input string"""
    assert validate_input('hello world') == True
    assert validate_input('') == True
    assert validate_input('abc') == True
    assert validate_input('2475    urbvjfbv') == True
    assert validate_input('hello World!') == False
    assert validate_input('not so bad, not bad at all&') == False


def test_convert_to_morse():
    """Checks correctness of converting text to morse code."""
    assert convert_to_morse('') == ''
    assert convert_to_morse('sos') == '... --- ...'
    assert convert_to_morse('SOS') == '... --- ...'
    assert convert_to_morse('so s') == '... --- / ...'
    assert convert_to_morse('Hello World') == '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    assert convert_to_morse('10 5') == '.---- ----- / .....'

