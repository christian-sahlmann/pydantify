import logging
from typing import Set, Type
from pyang.error import Position
from pathlib import Path
from typing_extensions import Self

logger = logging.getLogger('pydantify')


class YANGSourcesTracker:
    _relevant_files: Set[str] = set()

    @classmethod
    def track_from_pos(cls: Type[Self], pos: Position):
        path = str(Path(pos.ref).absolute())
        cls._relevant_files.add(path)

    @classmethod
    def copy_yang_files(cls: Type[Self], input_root: Path, output_dir: Path):
        """Copy only the relevant YANG model files to the output directory."""
        import shutil

        for f in cls._relevant_files:
            delta: Path = Path(f).relative_to(input_root)
            out = shutil.copy2(f, output_dir.joinpath(delta))
            logger.debug(f'Copied file "{f}" -> "{out}"')
