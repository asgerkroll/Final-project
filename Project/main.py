import ttkbootstrap as ttk
from GUI.new_element import NewElementDialog


root = ttk.Window()
root.title('Element database')

style = ttk.Style(theme='sandstone')

# Create a new instance of the dialog
dialog = NewElementDialog(root)

# Display the dialog
root.wait_window(dialog.dialog)

root.mainloop()
