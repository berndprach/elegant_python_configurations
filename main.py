from dataclasses import dataclass

from parsing import with_short_flags, create_parser


@with_short_flags(dataset_name="-d", epochs="-e")
@dataclass
class Configuration:
    dataset_name: str = "CIFAR-10"
    epochs: int = 24
    use_test_set: bool = False

    @classmethod
    def from_command_line_arguments(cls):
        parser = create_parser(cls)
        args = parser.parse_args()
        return cls(**vars(args))



def this_function_needs_a_configuration(c: Configuration):
    partition = "test" if c.use_test_set else "train"
    return f"Training on {c.dataset_name} ({partition}) for {c.epochs} epochs."


def main():
    my_config = Configuration.from_command_line_arguments()
    result = this_function_needs_a_configuration(my_config)
    print(result)


if __name__ == "__main__":
    main()