import argparse


def main(
    int_arg: int,
    str_arg: str,
    float_kwarg: float=1.0,
) -> None:
    """Print the user values."""
    print(f"{int_arg=}")
    print(f"{str_arg=}")
    print(f"{float_kwarg=}")


if __name__ == '__main__':
    p = argparse.ArgumentParser(
        description=main.__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    p.add_argument(
        'int_arg',
        help=(
            "an integer positional argument that can be used to do a good thing"
            " and\ncount the best stuff"
        ),
        type=int,
    )
    p.add_argument(
        'str_arg',
        help="a string positional argument",
    )
    p.add_argument(
        '--float_kwarg',
        help="a float keyword argument",
        type=float,
        default=1.0,
    )
    args = p.parse_args()
    main(**vars(args))
