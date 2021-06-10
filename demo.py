import autocli


def main(
    int_arg: int,
    str_arg: str,
    float_kwarg: float=1.0,
) -> None:
    """Print the user values.
    
    Positional Parameters
    ---------------------
    int_arg : int

    an integer positional argument

    str_arg : str

    a string positional argument

    Keyword Parameters
    ------------------
    float_kwarg : float

    a float keyword argument

    Return
    ------
    None
    """
    print(f"{int_arg=}")
    print(f"{str_arg=}")
    print(f"{float_kwarg=}")


if __name__ == "__main__":
    autocli.run(main)
