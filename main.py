from dataclasses import dataclass

import parsing
from parsing import with_short_flags, create_parser


@with_short_flags(dataset_name="-d", epochs="-e")
@dataclass
class Configuration:
    dataset_name: str = "CIFAR-10"
    epochs: int = 24
    use_test_set: bool = False


def this_function_needs_a_configuration(c: Configuration):
    """ Placeholder function e.g. for a training script. """
    partition = "test" if c.use_test_set else "validation"
    return f"Training on {c.dataset_name} for {c.epochs} epochs. Evaluating on {partition} data."


def main():
    my_config = parsing.from_command_line(Configuration)
    result = this_function_needs_a_configuration(my_config)
    print(result)


if __name__ == "__main__":
    main()