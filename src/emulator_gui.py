import tkinter as tk
from tkinter import scrolledtext

from emulator import Emulator

__all__ = [
    "EmulatorGUI"
]


class EmulatorGUI:
    _emulator: Emulator
    _window: tk.Tk
    _text_area: scrolledtext.ScrolledText
    _input_area: tk.Entry

    def __init__(self, emulator):
        self.emulator = emulator
        self._window = tk.Tk()
        self._window.title(f"{self.emulator.hostname} Emulator")

        self._text_area = scrolledtext.ScrolledText(
            self._window,
            wrap=tk.WORD,
            bg="black",
            fg="white"
        )
        self._text_area.pack(expand=True, fill='both')

        self._input_area = tk.Entry(self._window, bg="black", fg="white")
        self._input_area.pack(fill='x')
        self._input_area.bind("<Return>", self.run_command)
        self._input_area.focus_set()

    def run_command(self, args):
        command = self._input_area.get()
        self._input_area.delete(0, tk.END)

        full_path = self.emulator.current_directory  # Здесь нужно использовать полный путь
        output = self.emulator.execute_command(command)  # Выполнение команды и вывод с путем к текущей директории

        if output is not None:
            self._text_area.insert(tk.END, f"{self.emulator.hostname}:{full_path}$ {command}\n{output}\n")
        else:
            self._text_area.insert(tk.END, f"{self.emulator.hostname}:{full_path}$ {command}\n")

        self._text_area.yview(tk.END)
        self._input_area.focus_set()

    def start(self):
        self._window.mainloop()
