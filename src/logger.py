from csv import writer
from datetime import datetime

__all__ = [
    "Logger"
]


class Logger:
    _hostname: str
    _log_file_path: str

    def __init__(self, hostname, log_file_path):
        self._hostname = hostname
        self._log_file_path = log_file_path

        with open(self._log_file_path, mode='w+'):  # truncating the file before new session
            pass

    def write(self, message):
        with open(self._log_file_path, mode='a', newline='') as log_file:
            csv_writer = writer(log_file)
            csv_writer.writerow([self._hostname, datetime.now(), message])
