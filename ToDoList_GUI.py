import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To Do")
input_box = sg.InputText(tooltip = "Enter a To Do Item")
add_button = sg.Button("Add")

window = sg.Window("My ToDo App", layout=[[label], [input_box, add_button]])
window.read()
window.close()