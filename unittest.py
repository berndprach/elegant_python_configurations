from main import Configuration, this_function_needs_a_configuration


def test_this_function_needs_a_configuration():
    c = Configuration(epochs=100)
    target = "Training on CIFAR-10 for 100 epochs. Evaluating on validation data."

    result = this_function_needs_a_configuration(c)

    assert result == target, result


if __name__ == '__main__':
    test_this_function_needs_a_configuration()
    print("All tests passed!")