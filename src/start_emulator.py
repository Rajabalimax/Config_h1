from xml.etree import ElementTree as ET
from pathlib import Path

from emulator import Emulator
from emulator_gui import EmulatorGUI


ROOT_PATH = str(Path(__file__).resolve().parents[1])


def load_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()

    config = {
        'hostname': root.find('hostname').text,
        'fs_path': root.find('fs_path').text,
        'log_file_path': root.find('log_file_path').text,
        'start_script_path': root.find('start_script_path').text
    }
    return config


def start_emulator():
    #config = load_config('settings/config.xml')
    config = load_config(r'C:\Users\Rajabali\OneDrive\Рабочий стол\MIREA\Конфиг\1\1.1\OS-lang-emulator-master\settings\config.xml')


    emulator = Emulator(config)
    gui = EmulatorGUI(emulator)
    gui.start()


if __name__ == "__main__":
    start_emulator()
