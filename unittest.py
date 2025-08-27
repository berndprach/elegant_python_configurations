from main import Configuration, this_function_needs_a_configuration


def test_this_function_needs_a_configuration():
    c = Configuration(batch_size=512)
    target = "Using SGD with c.learning_rate=0.1 and c.batch_size=512."

    result = this_function_needs_a_configuration(c)

    assert result == target


if __name__ == '__main__':
    test_this_function_needs_a_configuration()
    print("All tests passed!")