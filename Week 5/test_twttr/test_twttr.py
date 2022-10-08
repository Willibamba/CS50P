from twttr import shorten


def test_shorten():
    assert shorten("lowercase") == "lwrcs"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("All4one") == "ll4n"
    assert shorten("This is sentence!") == "Ths s sntnc!"