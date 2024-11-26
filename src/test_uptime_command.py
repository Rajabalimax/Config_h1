import platform
import pytest

from emulator import Emulator

@pytest.mark.parametrize(
    "expected",
    [
        (f"System uptime: {platform.uname().system}\n"
         f"Node: {platform.uname().node}\n"
         f"Release: {platform.uname().release}\n"
         f"Version: {platform.uname().version}\n"
         f"Machine: {platform.uname().machine}")
    ]
)
def test_uptime_command(expected: str, emulator: Emulator) -> None:
    result = emulator.uptime()
    assert result == expected
