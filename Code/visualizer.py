# interface based on Tkinter
# Mann der Baeume ausreist, incl Progressbar
import tkinter as tk

root = tk.Tk()
root.title("Bubble sort visualizer")
root.geometry("1200x600")

canvas = tk.Canvas(root, bg="black", height=250, width=300)

canvas.pack(fill='both', expand=True)
root.mainloop()


