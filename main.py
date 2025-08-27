from dataclasses import dataclass

import parsing


@parsing.with_short_flags(dataset_name="-d", epochs="-e")
@dataclass
class Configuration:
    dataset_name: str = "CIFAR-10"
    epochs: int = 24
    use_test_set: bool = False

    @classmethod
    def from_command_line(cls):
        args = parsing.create_parser(cls).parse_args()
        return cls(**vars(args))


def this_function_needs_a_configuration(c: Configuration):
    """ Placeholder function e.g. for a training script. """
    partition = "test" if c.use_test_set else "validation"
    return f"Training on {c.dataset_name} for {c.epochs} epochs. Evaluating on {partition} data."


def main():
    print("\nConfiguration.from_command_line():")
    my_config = Configuration.from_command_line()
    result = this_function_needs_a_configuration(my_config)
    print(result)

    print("\nConfiguration(epochs=1):")
    my_other_config = Configuration(epochs=1)
    result = this_function_needs_a_configuration(my_other_config)
    print(result)


if __name__ == "__main__":
    main()