import tkinter as tk
from tkinter import ttk

class NeuronGUI:
    def __init__(self, master):
        self.master = master

        # Create sliders frame
        sliders_frame = tk.Frame(master)
        sliders_frame.pack(pady=20)

        # Create sliders
        self.input_slider = self.create_slider(sliders_frame, "Input:", self.update_input)
        self.weight_slider = self.create_slider(sliders_frame, "Weight:", self.update_weight)
        self.bias_slider = self.create_slider(sliders_frame, "Bias:", self.update_bias)

        # Create neuron frame
        neuron_frame = tk.Frame(master)
        neuron_frame.pack()

        # Create canvas for neuron visualization
        self.canvas = tk.Canvas(neuron_frame, width=500, height=300)
        self.canvas.pack()

    def create_slider(self, parent, label, command):
        slider_frame = tk.Frame(parent)
        slider_frame.pack()

        label = tk.Label(slider_frame, text=label)
        label.pack(side=tk.LEFT)

        slider = ttk.Scale(slider_frame, from_=-10, to=10, orient=tk.HORIZONTAL, command=command)
        slider.set(0)
        slider.pack(side=tk.LEFT)

        return slider

    def update_input(self, value):
        self.input = float(value)
        self.update_neuron()

    def update_weight(self, value):
        self.weight = float(value)
        self.update_neuron()

    def update_bias(self, value):
        self.bias = float(value)
        self.update_neuron()

    def update_neuron(self):
        # Perform ReLU activation
        activation = max(0, self.input * self.weight + self.bias)

        # Clear the canvas and display the neuron
        self.canvas.delete("neuron")

        # Draw input line
        self.canvas.create_line(50, 200, 150, 100, width=2, arrow=tk.LAST, tags="neuron")

        # Draw weight line
        self.canvas.create_line(150, 100, 250, 100, width=2, arrow=tk.LAST, tags="neuron")

        # Draw bias line
        self.canvas.create_line(250, 100, 350, 200, width=2, arrow=tk.LAST, tags="neuron")

        # Draw input node
        self.canvas.create_oval(45, 195, 55, 205, fill="white", tags="neuron")

        # Draw weight node
        self.canvas.create_oval(145, 95, 155, 105, fill="white", tags="neuron")

        # Draw bias node
        self.canvas.create_oval(345, 195, 355, 205, fill="white", tags="neuron")

        # Draw activation node
        self.canvas.create_oval(245, 95, 255, 105, fill="white", tags="neuron")

        # Draw activation text
        self.canvas.create_text(250, 85, text=f"ReLU({self.input}*{self.weight} + {self.bias}) = {activation}", tags="neuron")

# Create the main window
root = tk.Tk()
root.title("Neuron GUI")

# Create an instance of the NeuronGUI class
neuron_gui = NeuronGUI(root)

# Run the tkinter event loop
root.mainloop()
