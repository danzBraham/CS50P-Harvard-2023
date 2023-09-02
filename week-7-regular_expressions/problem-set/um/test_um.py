from um import count


# Test counting a single occurrence of "um"
def test_count_single_um():
    assert count("um") == 1


# Test counting a single occurrence of "um?"
def test_count_single_um_question_mark():
    assert count("um?") == 1


# Test counting a single occurrence of "Um" (capitalized)
def test_count_single_um_capitalized():
    assert count("Um, thanks for the album") == 1


# Test counting multiple occurrences of "um"
def test_count_multiple_um():
    assert count("Um, thanks, um.....") == 2


# Test counting a single occurrence of "UM" (all caps)
def test_count_single_um_all_caps():
    assert count("UM") == 1


# Test counting a single occurrence of "um" within a sentence
def test_count_single_um_within_sentence():
    assert count("Um, I'm not sure about that.") == 1


# Test counting a triple occurrence of "um" within a sentence
def test_count_triple_um_within_sentence():
    assert count("I think um.. um... um....") == 3
