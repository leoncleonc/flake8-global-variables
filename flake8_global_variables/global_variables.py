import sys
import ast
from visitor import Visitor
from typing import Any, Type, Tuple, Generator


if sys.version_info < (3, 8):  # pragma: no cover (<PY38)
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
