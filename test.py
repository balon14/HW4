def test_punctuated():
    assert text_punctuated("Дмитрий") == \
        "Дмитрий"


def test_lang_detection():
    assert lang_detection("12332") == \
        "имя должно состоять из букв"
