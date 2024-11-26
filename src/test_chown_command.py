import pytest

from emulator import Emulator


@pytest.mark.parametrize(
    "filepath, current_directory, expected",
    [
        (
            "/home/user/documents/file1.txt", "/home/bin", "Last 10 lines of file:\nHello, this is file 1.\n"
        ),
        (
            "file2.txt", "/home/user/documents", "Last 10 lines of file:\nThis is file 2.\n"
        )
    ]
)
def test_tail_command(filepath: str, current_directory: str, expected: str, emulator: Emulator) -> None:
    emulator.current_directory = current_directory
    result = emulator.tail(filepath)

    assert result == expected
