import tkinter as tk


class CustomEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def _on_focus_in(self, _):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def _on_focus_out(self, _):
        if not self.get().strip():
            self.put_placeholder()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Input integers and floats")
        self.geometry("300x100")

        self.entry = CustomEntry(self, placeholder="Ex: 1,45,57")
        self.entry.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.bind("<Button-1>", self.on_window_click)

    def on_window_click(self, event):
        widget = self.winfo_containing(event.x_root, event.y_root)
        if widget != self.entry:
            self.focus_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
