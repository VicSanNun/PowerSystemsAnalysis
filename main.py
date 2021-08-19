from tkinter import *

window = Tk()

window.title("PSA - Power System Analysis")

text = Label(window, text="Escolha Qual Função Executar")
text.grid(column=0, row=0, padx=70, pady=30)

#button = Button(window, text="Representação de Fase", command=pegar_cotacoes)
buttonPhase = Button(window, text="Representação de Fase")
buttonPhase.grid(column=0, row=1, padx=10, pady=20)

buttonSim = Button(window, text="Componentes Simétricas")
buttonSim.grid(column=0, row=2, padx=10, pady=20)

buttonClarke = Button(window, text="Transformação de Clarke")
buttonClarke.grid(column=0, row=3, padx=10, pady=20)

buttonSolve = Button(window, text="Resolver Sistema de Potência")
buttonSolve.grid(column=0, row=4, padx=10, pady=20)

window.mainloop()