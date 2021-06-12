import autocli
import matplotlib.pyplot as plt


def main(
    int_arg: int,
    str_arg: str,
    float_kwarg: float=1.0,
) -> None:
    """Print the user values.
    
    Parameters
    ----------
    int_arg : int
        an integer positional argument that can be used to do a good thing and
        count the best stuff
    str_arg : str
        a string positional argument
    float_kwarg : float
        a float keyword argument

    Returns
    -------
    None
    """
    print(f"{int_arg=}")
    print(f"{str_arg=}")
    print(f"{float_kwarg=}")


if __name__ == "__main__":
    autocli.run(main, prog='prog')
