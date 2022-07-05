import PySimpleGUI as sg
layout = [[sg.Text("Welcome too GameQuizShow!")], [sg.Button("New GameQuiz")], [sg.Button("Load GameQuiz")]]
win = sg.Window("GameQuizShow!", layout)
while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        break
win.close()