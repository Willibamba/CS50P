from um import count

# Unit test
def test_count():
    assert count("Um,") == 1
    assert count("um, thanks, um... Mum?") == 2
    assert count("album") == 0