from string_reversal import reverse_string

def test_calculate_age():
    # Given
    text = "Hello World!"

    # When
    reversed = reverse_string(text)

    # Then 
    assert reversed == "!dlroW olleH"
