import tkinter as tk

class NeuronGUI:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=1200)
        self.canvas.pack()

        # Neuron properties
        self.input = 0
        self.weight = 0
        self.bias = 0

        # Create GUI elements
        self.input_entry = tk.Entry(master)
        self.weight_entry = tk.Entry(master)
        self.bias_entry = tk.Entry(master)
        self.submit_button = tk.Button(master, text="Submit", command=self.update_neuron)

        # Place GUI elements on the canvas
        self.canvas.create_window(180, 50, window=self.input_entry)
        self.canvas.create_window(180, 90, window=self.weight_entry)
        self.canvas.create_window(180, 130, window=self.bias_entry)
        self.canvas.create_window(100, 190, window=self.submit_button)

    def update_neuron(self):
        # Get the values from the input fields
        self.input = float(self.input_entry.get())
        self.weight = float(self.weight_entry.get())
        self.bias = float(self.bias_entry.get())

        # Perform ReLU activation
        activation = max(0, self.input * self.weight + self.bias)

        # Clear the canvas and display the neuron
        self.canvas.delete("neuron")
        self.canvas.create_oval(500, 500, 200, 200, fill="lightblue", tags="neuron")
        self.canvas.create_text(500, 600, text=f"ReLU({self.input}*{self.weight} + {self.bias}) = {activation}", tags="neuron")

# Create the main window
root = tk.Tk()
root.title("Neuron GUI")

# Create an instance of the NeuronGUI class
neuron_gui = NeuronGUI(root)

# Run the tkinter event loop
root.mainloop()
