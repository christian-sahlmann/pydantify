from yang2pydantic.generator import ModelGenerator  # TODO: Get relative import to work. (╯°□°）╯︵ ┻━┻
from io import TextIOWrapper
from pyang.plugin import PyangPlugin, register_plugin
from pyang.statements import ModSubmodStatement
from pyang.context import Context
from typing import Dict


def pyang_plugin_init():
    register_plugin(Yang2Pydantic())


class Yang2Pydantic(PyangPlugin):
    def __init__(self):
        """Init plugin instance."""
        super().__init__(name="yang2pydantic")

    def add_output_format(self, fmts: Dict[str, PyangPlugin]):
        """Register self as primary pydantic output generator."""
        fmts['pydantic'] = self
        self.multiple_modules = True
        self.handle_comments = True

    def emit(self, ctx: Context, modules: ModSubmodStatement, fd: TextIOWrapper):
        """Convert yang model."""
        ModelGenerator.generate(ctx=ctx, modules=modules, fd=fd)