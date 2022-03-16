import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [  [sg.Text('Run this b on login')],
            [sg.Text('Did it run'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]
window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()