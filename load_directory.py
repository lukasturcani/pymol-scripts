from pymol import cmd
from glob import iglob
import os


@cmd.extend
def _load_directory(path, extension):
    """
    Load all files with `extension` in `path`.

    """

    glob = os.path.join(path, f'*.{extension}')
    for filename in sorted(iglob(glob)):
        cmd.load(filename)
