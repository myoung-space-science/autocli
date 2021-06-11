import argparse
import inspect
from typing import *


def run(this: Callable):
    """Provide a CLI to a callable."""
    lines = this.__doc__.split('\n')
    parser = argparse.ArgumentParser(
        description=lines[0].strip(),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    signature = inspect.signature(this)
    parameters = signature.parameters
    descriptions = parse_descriptions(parameters, lines)
    for parameter in parameters.values():
        if parameter.default is signature.empty:
            name = f'{parameter.name}'
        else:
            name = f'--{parameter.name}'
        parser.add_argument(
            name,
            help=descriptions[parameter.name],
            type=get_type(parameter)
        )
    args = parser.parse_args()
    this(**vars(args))


def parse_descriptions(
    parameters: Iterable[inspect.Parameter],
    doclines: Iterable[str],
) -> Dict[str, str]:
    """Parse parameter descriptions from the docstring"""
    return {name: '<no description available>' for name in parameters}


type_map = {
    'int': int,
    'str': str,
    'float': float,
}


def get_type(parameter: inspect.Parameter) -> type:
    """Get the type of a parameter."""
    type_string = parameter.annotation.__qualname__
    return type_map[type_string]