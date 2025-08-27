
import argparse
import dataclasses


def with_short_flags(**kwargs):
    def decorator(cls):
        setattr(cls, "__short_flags__", kwargs)
        return cls

    return decorator


def create_parser(cls) -> argparse.ArgumentParser:
    if not dataclasses.is_dataclass(cls):
        raise TypeError(f"{cls.__name__} must be a dataclass")

    parser = argparse.ArgumentParser()
    short_flags = getattr(cls, "__short_flags__", {})
    print(short_flags)

    for field in dataclasses.fields(cls):
        arg_name = f"--{field.name}".replace("_", "-")
        arg_type = field.type
        arg_default = field.default

        if field.name in short_flags:
            flags = [short_flags[field.name], arg_name]
        else:
            flags = [arg_name]

        if arg_type == bool:
            action = {True: "store_false", False: "store_true"}[arg_default]
            parser.add_argument(*flags, action=action)
        else:
            parser.add_argument(*flags, type=arg_type, default=arg_default)
    return parser