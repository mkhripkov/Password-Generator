import secrets # Using secrets to generate the password rather than random is more secure
import PySimpleGUI as sg

# GUI 
sg.theme('DarkPurple4')

layout = [
    [sg.Text('Enter Desired Password Length:')],
    [sg.Input(key = '-INPUT-', size=5)],
    [sg.Button('Generate', key='-BUTTON1-')],
    [sg.Text('Password:'), sg.Multiline(size = 35, no_scrollbar=True, disabled=True, key='-PASSWORD-')]    
    ]

window = sg.Window('Python Password Generator', layout, size=(300, 100), resizable=True)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED: # Closes window when X button is clicked
        break 
    
    if event == '-BUTTON1-':
        try:
            # Password Generation
            possible_characters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()?'
            password_length = int(values['-INPUT-'])
            password = ''
            for x in range(password_length):
                password += secrets.choice(possible_characters) # secrets randomly selects a character and adds it to the password string
            window['-PASSWORD-'].update(password)
        except ValueError:
            window['-PASSWORD-'].update('Invalid Input')
    
window.close()