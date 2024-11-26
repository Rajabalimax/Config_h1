import pytest
import sys
import os

from emulator import Emulator


@pytest.mark.parametrize(
    "path, current_directory, expected",
    [
        (
            "/home/user", "/", "/home/user"
        ),
        (
            "documents", "/home/user", "/home/user/documents"
        ),
        (
            "..", "/home/bin", "/home"
        )
    ]
)
def test_ls_command(path: str, current_directory: str, expected: str, emulator: Emulator) -> None:
    emulator.current_directory = current_directory
    emulator.cd(path)

    assert emulator.current_directory == expected
