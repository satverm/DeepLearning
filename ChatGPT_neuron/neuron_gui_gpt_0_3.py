import tkinter as tk
from tkinter import ttk

class Neuron:
    def __init__(self, input=0, weight=0, bias=0, activation=0):
        self.input = input
        self.weight = weight
        self.bias = bias
        self.activation = activation

    def set_input(self, value):
        self.input = value

    def set_weight(self, value):
        self.weight = value

    def set_bias(self, value):
        self.bias = value

    def calculate_activation(self):
        pass
        # the line below creates problem
        #self.activation = max(0, self.input * self.weight + self.bias)


class NeuronGUI:
    def __init__(self, master, neuron):
        self.master = master
        self.neuron = neuron

        # Create sliders frame
        sliders_frame = tk.Frame(master)
        sliders_frame.pack(pady=20)

        # Create sliders
        self.input_slider = self.create_slider(sliders_frame, "Input:", self.neuron.set_input)
        self.weight_slider = self.create_slider(sliders_frame, "Weight:", self.neuron.set_weight)
        self.bias_slider = self.create_slider(sliders_frame, "Bias:", self.neuron.set_bias)

        # Create neuron frame
        neuron_frame = tk.Frame(master)
        neuron_frame.pack()

        # Create canvas for neuron visualization
        self.canvas = tk.Canvas(neuron_frame, width=500, height=300)
        self.canvas.pack()

        # Draw initial neuron
        self.update_neuron()

    def create_slider(self, parent, label, command):
        slider_frame = tk.Frame(parent)
        slider_frame.pack()

        label = tk.Label(slider_frame, text=label)
        label.pack(side=tk.LEFT)

        slider = ttk.Scale(slider_frame, from_=-10, to=10, orient=tk.HORIZONTAL, command=command)
        slider.set(0)
        slider.pack(side=tk.LEFT)

        return slider

    def update_neuron(self):
        self.neuron.calculate_activation()

        # Clear the canvas and display the neuron
        self.canvas.delete("neuron")

        # Draw input node
        self.canvas.create_oval(80, 50, 120, 90, fill="lightgray", tags="neuron")

        # Draw weight node
        self.canvas.create_oval(220, 50, 260, 90, fill="lightgray", tags="neuron")

        # Draw bias node
        self.canvas.create_oval(350, 180, 390, 220, fill="lightgray", tags="neuron")

        # Draw activation node
        self.canvas.create_oval(250, 180, 290, 220, fill="lightgray", tags="neuron")

        # Draw activation inner circle
        if self.neuron.activation > 0:
            self.canvas.create_oval(255, 185, 285, 215, fill="green", tags="neuron")

        # Draw input arrow
        self.canvas.create_line(100, 70, 220, 70, arrow=tk.LAST, tags="neuron")

        # Draw weight arrow
        self.canvas.create_line(260, 70, 350, 200, arrow=tk.LAST, tags="neuron")

        # Draw bias arrow
        self.canvas.create_line(370, 200, 290, 200, arrow=tk.LAST, tags="neuron")

        # Draw input text
        self.canvas.create_text(100, 90, text="Input", tags="neuron")

        # Draw weight text
        self.canvas.create_text(260, 90, text="Weight", tags="neuron")

        # Draw bias text
        self.canvas.create_text(370, 220, text="Bias", tags="neuron")

        # Update the sliders based on the neuron's properties
        self.input_slider.set(self.neuron.input)
        self.weight_slider.set(self.neuron.weight)
        self.bias_slider.set(self.neuron.bias)


# Create a Neuron instance
neuron1 = Neuron()

# Create the root window
root = tk.Tk()
root.title("Neuron Visualization")

# Create the NeuronGUI object
neuron_gui = NeuronGUI(root, neuron1)

# Start the Tkinter event loop
root.mainloop()
