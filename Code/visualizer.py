# interface based on Tkinter
# Mann der Baeume ausreist, incl Progressbar
import tkinter as tk


def window_runner(root):
    canvas = tk.Canvas(root, bg="black", height=250, width=300)
    canvas.pack(fill='both', expand=True)

    length_label = tk.Label(canvas, text="array length").grid(row=0)

    length_input = tk.Entry(canvas, bd=5).grid(row=0, column=1)

    enter_button = tk.Button(canvas, text="Enter", command=get_length_input(length_input)).grid(row=1)

    root.mainloop()


def get_length_input(length_input):
    # Todo: Implement validity check for entry value (int)
    if length_input is not None:
        user_input = int(length_input.get())
        print(user_input)


class Visualizer:

    def __init__(self, title, geometry):
        root = tk.Tk()
        root.title(title)
        root.geometry(geometry)
        window_runner(root)
