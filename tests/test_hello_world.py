from hello_word import HelloWorld


def test_hello_world():
    message = "Hello World!"

    hello_word_utils = HelloWorld(message)

    assert message == hello_word_utils.log()
