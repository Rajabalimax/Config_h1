import pytest

from start_emulator import load_config, ROOT_PATH
from emulator import Emulator


@pytest.fixture()
def emulator() -> Emulator:
    config = load_config('settings/config.xml')
    return Emulator(config)
