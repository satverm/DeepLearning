import tkinter as tk
from tkinter import messagebox

class NeuronGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Single Neuron Representation")
        self.geometry("800x800")
        
        self.weight = tk.DoubleVar()
        self.bias = tk.DoubleVar()
        self.input_val = tk.DoubleVar()
        self.output_val = tk.StringVar()
        
        weight_label = tk.Label(self, text="Weight")
        weight_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        weight_slider = tk.Scale(self, from_=-1, to=1, resolution=0.01, orient="vertical", variable=self.weight,
                                 command=self.update_output)
        weight_slider.set(0)
        weight_slider.grid(row=1, column=1, padx=10, pady=5)
        
        bias_label = tk.Label(self, text="Bias")
        bias_label.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        bias_slider = tk.Scale(self, from_=-1, to=1, resolution=0.1, orient="horizontal", variable=self.bias,
                               command=self.update_output)
        bias_slider.set(0)
        bias_slider.grid(row=1, column=3, padx=10, pady=5)
        
        input_label = tk.Label(self, text="Input")
        input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        input_slider = tk.Scale(self, from_=-1, to=1, resolution=0.1, orient="vertical", variable=self.input_val,
                                command=self.update_output)
        input_slider.set(0)
        input_slider.grid(row=1, column=0, padx=10, pady=5)
        
        output_label = tk.Label(self, text="Output")
        output_label.grid(row=0, column=4, padx=10, pady=10, sticky="w")
        output_box = tk.Label(self, textvariable=self.output_val)
        output_box.grid(row=0, column=5, padx=10, pady=5)
        
        self.update_output(None)
    
    def update_output(self, _):
        weight = self.weight.get()
        bias = self.bias.get()
        input_val = self.input_val.get()
        
        output = weight * input_val + bias
        #self.output_val.set(f"Max: {max(output):.2f}\nMin: {min(output):.2f}\nCurrent: {output:.2f}")
        self.output_val.set(output)
if __name__ == "__main__":
    app = NeuronGUI()
    app.mainloop()
