import pytest

from emulator import Emulator


@pytest.mark.parametrize(
    "path, current_directory, expected",
    [
        (
            "/home/user", "/", "documents\tmusic\tpictures"
        ),
        (
            "/home/bin", "/home/bin", "program\tscript.sh"
        ),
        (
            "../", "/home/user/documents", "documents\tmusic\tpictures"
        )
    ]
)
def test_ls_command(path: str, current_directory: str, expected: str, emulator: Emulator) -> None:
    emulator.current_directory = current_directory
    result = emulator.ls(path)

    assert result == expected
