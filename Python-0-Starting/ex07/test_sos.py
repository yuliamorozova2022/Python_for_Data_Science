from sos import validate_input, convert_to_morse


def test_validate_input():
    """Checks if function correctly validates input string"""
    assert validate_input('hello world')
    assert validate_input('')
    assert validate_input('abc')
    assert validate_input('2475    urbvjfbv')
    assert not validate_input('hello World!')
    assert not validate_input('not so bad, not bad at all&')


def test_convert_to_morse():
    """Checks correctness of converting text to morse code."""
    assert convert_to_morse('') == ''
    assert convert_to_morse('sos') == '... --- ...'
    assert convert_to_morse('SOS') == '... --- ...'
    assert convert_to_morse('so s') == '... --- / ...'
    assert convert_to_morse('Hello World') == (
        '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    )
    assert convert_to_morse('10 5') == '.---- ----- / .....'
