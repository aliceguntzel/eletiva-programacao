import tkinter as tk
import random
import time

class SimuladorTempoReacao:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Simulador de Tempo de Reação")

        self.label_instrucao = tk.Label(self.janela, text="Clique no botão quando a cor mudar") #mudar de qual cor para qual??
        self.label_instrucao.pack(pady=10)

        self.frame_cor = tk.Frame(self.janela, width=200, height=200, bg="red")
        self.frame_cor.pack(pady=10)

        self.botao_inicio = tk.Button(self.janela, text="Iniciar", command=self.iniciar_simulacao)
        self.botao_inicio.pack(pady=10)

    def iniciar_simulacao(self):
        self.botao_inicio.config(state=tk.DISABLED)

        cor_aleatoria = random.choice(["red", "green", "blue"]) #troca de vermelho pra vermelho?? ai nao da pra saber quando muda
        self.frame_cor.config(bg=cor_aleatoria)

        self.janela.after(random.randint(1000, 5000), self.iniciar_tempo_reacao)

    def iniciar_tempo_reacao(self):
        self.frame_cor.config(bg="red")
        self.frame_cor.bind("<Button-1>", self.registrar_tempo_reacao)
        self.tempo_inicial = time.time()

    def registrar_tempo_reacao(self, event):
        tempo_reacao = time.time() - self.tempo_inicial
        self.mostrar_resultado(tempo_reacao)

    def mostrar_resultado(self, tempo_reacao):
        self.label_instrucao.config(text=f"Tempo de Reação: {tempo_reacao:.3f} segundos")
        self.botao_inicio.config(state=tk.NORMAL)

    def iniciar(self):
        self.janela.mainloop()

simulador = SimuladorTempoReacao()
simulador.iniciar()
