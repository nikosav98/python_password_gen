import PySimpleGUI as sg
import random
import string

sg.theme('DarkGrey13')

layout = [
    [sg.Text('Password generator')],
    [sg.Text("Choose strength: "),
     sg.Radio('Weak', "RADIO1", enable_events=True, key='-STREN WEAK-'),
     sg.Radio('Medium', "RADIO1", enable_events=False, key='-STREN MEDIUM-'),
     sg.Radio('Strong', "RADIO1", enable_events=False, key='-STREN STRONG-')],
    [sg.Text("Choose Amount of passwords: "), sg.InputText('5', key='-AMOUNT-', size=(5, 1))],
    [sg.Text("Output to file?"), sg.Radio('No', "RADIO2", default=True, key='-NO_FILE-'), 
     sg.Radio('Yes', "RADIO2", key='-YES_FILE-')],
    [sg.Output(size=(50, 10), key='-OUTPUT-')],
    [sg.Exit(key="-CANCEL-"), sg.Button("Generate", key="-GEN-"), sg.Button("Clear", key="-CLEAR-")]
]
window = sg.Window('Password generator', layout)

#Open file
f = open("passwords.txt", "w")

def generatePassword(passlen, amount, file, ptf):

        for i in range(amount):
            if(passlen == 6):
                characters = string.ascii_letters + string.digits 
            if(passlen > 6):
                characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(passlen))

            print(password)
            if ptf == True:
                print(password, file=file)

def generateSeed():
        if values['-SEED-'] != '0':
            seed = values['-SEED-']
        else:
            seed = None
        return seed

while True:
    event, values = window.read()
    if event == '-GEN-':

        window['-OUTPUT-'].update('') 
        amount = values['-AMOUNT-']
        printToFile = values['-YES_FILE-']
        if amount.isdigit():  
            amount = int(amount)
            if values['-STREN WEAK-']:
                generatePassword(6, amount, f, printToFile)

            elif values['-STREN MEDIUM-']:  
                generatePassword(12, amount, f, printToFile)

            elif values['-STREN STRONG-']:  
                generatePassword(16, amount, f, printToFile)
                    
        else:
            sg.popup_error("Please enter a valid integer for amount.")

    if event == '-CLEAR-':
        window['-OUTPUT-'].update('')
    if event == '-CANCEL-':
        break

f.close()
window.close()






