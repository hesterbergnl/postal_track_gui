import tkinter as tk
from tkinter import ttk
from tracker import newItem, updateItems

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.frames = {}
        
        self.title("Postal tracker")
        self.geometry('1300x400')

        lblMain = tk.Label(self, text="Package 1").grid(column = 0, row = 1)

        lblCarrier = tk.Label(self, text="Carrier:").grid(sticky="w", column = 1, row = 0)

        lblTrackNum = tk.Label(self, text = "Tracking Number:")
        lblTrackNum.grid(sticky="w", column = 2, row = 0)

        lblOrigin = tk.Label(self, text = "Origin:")
        lblOrigin.grid(sticky="w", column = 3, row = 0)

        lblDescription = tk.Label(self, text = "Description:")
        lblDescription.grid(sticky="w", column = 4, row = 0)

        cmbCarrier = ttk.Combobox(self,
                                  values = ["USPS",
                                            "Fedex",
                                            "UPS"])

        cmbCarrier.grid(column = 1, row = 1)
        cmbCarrier.current(0)

        txtTrackNum = tk.Entry(self, width = 20)
        txtTrackNum.grid(column = 2, row = 1)

        txtOrigin = tk.Entry(self, width = 20)
        txtOrigin.grid(column = 3, row = 1)

        txtDescription = tk.Entry(self, width = 80)
        txtDescription.grid(column = 4, row = 1)

        def addClicked():
            newItem(cmbCarrier.get(), txtTrackNum.get(), txtOrigin.get(), txtDescription.get())

        btnAdd = tk.Button(self, text="Add", command=addClicked)
        btnAdd.grid(column = 5, row = 1)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
