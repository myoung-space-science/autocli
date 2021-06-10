import autocli


def main(
    int_arg: int,
    str_arg: str,
    float_kwarg: float=1.0,
) -> None:
    """Print the user values."""
    print(f"{int_arg=}")
    print(f"{str_arg=}")
    print(f"{float_kwarg=}")


if __name__ == "__main__":
    autocli.run(main)
