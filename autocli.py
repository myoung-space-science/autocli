import argparse
import inspect
from typing import *


class DocString:
    """A class to hold information about a given docstring."""
    def __init__(self, docstring: str) -> None:
        self.raw = docstring
        self._lines = docstring.split('\n')
        self._sections = None

    @property
    def summary(self) -> str:
        """The docstring summary."""
        return self._lines[0].strip()

    @property
    def sections(self) -> Dict[str, List[str]]:
        """The parsed sections of the docstring."""
        if self._sections is None:
            self._sections = self._get_sections()
        return self._sections

    def _get_sections(self) -> Dict[str, List[str]]:
        """The parsed sections of the docstring."""
        breaks = self._get_section_breaks()
        indices = [b[0] for b in breaks]
        headings = [b[1] for b in breaks]
        sections = {}
        for i, heading in enumerate(headings):
            head = indices[i]
            stop = indices[i+1] - 1 if head != indices[-1] else None
            start = head + 1
            sections[heading] = self._lines[start:stop]
        return sections

    def _get_section_breaks(self) -> list:
        """Get a list of section breaks."""
        return [
            (i, self._lines[i - 1].strip())
            for i, line in enumerate(self._lines)
            if set(list(line.strip())) == {'-'}
        ]


def run(this: Callable, **kwargs):
    """Provide a CLI to a callable."""
    docstring = DocString(inspect.getdoc(this))
    parser = argparse.ArgumentParser(
        description=docstring.summary,
        formatter_class=argparse.RawTextHelpFormatter,
        **kwargs
    )
    signature = inspect.signature(this)
    parameters = signature.parameters
    descriptions = parse_descriptions(parameters, docstring)
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
    docstring: DocString,
) -> Dict[str, str]:
    """Parse parameter descriptions from the docstring"""
    if 'Parameters' not in docstring.sections:
        return {name: '<no description available>' for name in parameters}
    descriptions = {}
    given = docstring.sections['Parameters']
    names = []
    for i, line in enumerate(given):
        name = line.split(':')[0].strip()
        if name in parameters:
            names.append((i, name))
    for i, (start, name) in enumerate(names):
        try:
            stop = names[i+1][0]
        except IndexError:
            stop = None
        text = '\n'.join(s.strip() for s in given[start+1:stop])
        descriptions[name] = text.rstrip('\n')
    return descriptions


type_map = {
    'int': int,
    'str': str,
    'float': float,
}


def get_type(parameter: inspect.Parameter) -> type:
    """Get the type of a parameter."""
    type_string = parameter.annotation.__qualname__
    return type_map[type_string]