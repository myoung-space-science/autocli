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
    for line in lines:
        try:
            name, annotation = line.split(':')
            if name.strip() in parameters:
                import pdb; pdb.set_trace()
                # From here: index all names provided in the docstring, then use
                # that information to extract parameter descriptions.
        except ValueError:
            pass
    for parameter in parameters.values():
        if parameter.default is signature.empty:
            name = f'{parameter.name}'
        else:
            name = f'--{parameter.name}'
        parser.add_argument(
            name,
            type=get_type(parameter)
        )
    args = parser.parse_args()
    this(**vars(args))


type_map = {
    'int': int,
    'str': str,
    'float': float,
}


def get_type(parameter: inspect.Parameter) -> type:
    """Get the type of a parameter."""
    type_string = parameter.annotation.__qualname__
    return type_map[type_string]