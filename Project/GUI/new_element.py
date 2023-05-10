import sys
sys.path.append('../models')
sys.path.append('../Project')
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.filedialog as fd
from sqlalchemy.orm import Session
from Project.models.dimension import Dimension
from Project.models.element import ElementId


class NewElementDialog:
    def __init__(self, parent=None):
        self.parent = parent
        self.dialog = ttk.Toplevel(parent)

        self.dialog.geometry("1024x720")

        # Create the form widgets

        title_label = ttk.Label(self.dialog, text='Data about the new element', font='Cambria 20 bold')

        type_label = ttk.Label(self.dialog, text='Type:', font='Cambria 11')

        # Dropdown box with type of element
        self.type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(self.dialog, textvariable=self.type_var)
        self.type_combobox['values'] = ['Wall', 'KB', 'TT beam', 'Steel I beam']

        # Bind the show_steel_fields function to the <<ComboboxSelected>> event
        self.type_combobox.bind("<<ComboboxSelected>>", self.show_steel_fields)

        # Width of element
        width_label = ttk.Label(self.dialog, text='Width:', font='Cambria 11')
        width_frame = ttk.Frame(self.dialog)
        self.width_input = ttk.Entry(width_frame)
        self.width_input_label = ttk.Label(width_frame, text='mm', font='Cambria 11')

        # Length of element
        length_label = ttk.Label(self.dialog, text='Length:', font='Cambria 11')
        length_frame = ttk.Frame(self.dialog)
        self.length_input = ttk.Entry(length_frame)
        self.length_input_label = ttk.Label(length_frame, text='mm', font='Cambria 11')

        # Height of element
        height_label = ttk.Label(self.dialog, text='Height:', font='Cambria 11')
        height_frame = ttk.Frame(self.dialog)
        self.height_input = ttk.Entry(height_frame)
        self.height_input_label = ttk.Label(height_frame, text='mm', font='Cambria 11')

        # Concrete type of element
        self.concrete_type_label = ttk.Label(self.dialog, text='Concrete type:', font='Cambria 11')
        self.concrete_type_input = ttk.Entry(self.dialog)

        # Steel type of element
        self.steel_type_label = ttk.Label(self.dialog, text='Steel type:', font='Cambria 11')
        self.steel_type_input = ttk.Entry(self.dialog, state='disabled')

        # Load capacity of element
        load_capacity_label = ttk.Label(self.dialog, text='Length:', font='Cambria 11')
        load_capacity_frame = ttk.Frame(self.dialog)
        self.load_capacity_input = ttk.Entry(load_capacity_frame)
        self.load_capacity_input_label = ttk.Label(load_capacity_frame, text='mm', font='Cambria 11')

        # Optional file attachment
        file_label = tk.Label(self.dialog, text='Select a file:', font='Cambria 11')
        self.file_path = tk.StringVar()
        self.file_path.set('No file selected')
        file_button = tk.Button(self.dialog, text='Browse...', command=self.browse_file)
        attach_button = tk.Button(self.dialog, text='Attach file...', command=self.attach_file)

        # Button to proceed
        style = ttk.Style()
        style.configure('Submit.TButton', font='Cambria 10')
        submit_button = ttk.Button(self.dialog, text='Submit', command=self.create_element, style='Submit.TButton')

        # Add the widgets to the layout
        title_label.pack(side='top', anchor='nw', padx=10, pady=5)
        type_label.pack(side='top', anchor='nw', padx=10, pady=5)
        self.type_combobox.pack(side='top', anchor='nw', padx=10, pady=5)

        width_label.pack(side='top', anchor='nw', padx=10, pady=5)
        width_frame.pack(side='top', anchor='nw', padx=10, pady=5)
        self.width_input.pack(side='left', anchor='w', pady=5)
        self.width_input_label.pack(side='left', anchor='w', padx=5, pady=5)

        length_label.pack(side='top', anchor='nw', padx=10, pady=5)
        length_frame.pack(side='top', anchor='nw', padx=10, pady=5)
        self.length_input.pack(side='left', anchor='nw', pady=5)
        self.length_input_label.pack(side='left', anchor='nw', padx=5, pady=5)

        height_label.pack(side='top', anchor='nw', padx=10, pady=5)
        height_frame.pack(side='top', anchor='nw', padx=10, pady=5)
        self.height_input.pack(side='left', anchor='nw', pady=5)
        self.height_input_label.pack(side='left', anchor='nw', padx=5, pady=5)

        self.concrete_type_label.pack(side='top', anchor='nw', padx=10, pady=5)
        self.concrete_type_input.pack(side='top', anchor='nw', padx=10, pady=5)

        self.steel_type_label.pack_forget()
        self.steel_type_input.pack_forget()

        file_label.pack(side='top', anchor='nw', padx=10, pady=5)
        file_button.pack(side='top', anchor='nw', padx=10, pady=5)
        attach_button.pack(side='left', anchor='nw', padx=10, pady=5)

        submit_button.pack(side='bottom', anchor='sw', padx=10, pady=10)

    def show_steel_fields(self, event=None):
        type = self.type_combobox.get()
        if "Steel" in type:
            self.steel_type_label.pack(side='top', anchor='nw', padx=10, pady=5)
            self.steel_type_input.pack(side='top', anchor='nw', padx=10, pady=5)
            self.concrete_type_label.pack_forget()
            self.concrete_type_input.pack_forget()
        elif "Steel" not in type:
            self.steel_type_label.pack_forget()
            self.steel_type_input.pack_forget()
            self.concrete_type_label.pack(side='top', anchor='nw', padx=10, pady=5)
            self.concrete_type_input.pack(side='top', anchor='nw', padx=10, pady=5)

    def browse_file(self):
        file_path = fd.askopenfilename()
        self.file_path.set(file_path)

    def attach_file(self):
        file_path = fd.askopenfilename()
        self.file_path.set(file_path)

    def create_element(self):
        # Create a session
        session = Session()

        # Get the input values from the form
        type = self.type_combobox.get()
        width = float(self.width_input.get())
        length = float(self.length_input.get())
        height = float(self.height_input.get())

        # Create a new Dimension object
        dimension = Dimension(width=width, length=length, height=height)

        # Create a new ElementId object
        element = ElementId(type=type, dimension=width)

        try:
            # Add the new object to the session
            session.add(element, dimension)

            # Commit the transaction
            session.commit()

            # Change the style of the button if submitted correctly
            style = ttk.Style()
            style.configure('Submit.TButton', foreground='green')

        except Exception as e:
            print(f"Error: {e}")
            session.rollback()

        else:
            # Close the dialog
            self.dialog.destroy()
