import tkinter as tk
import time

class Cronometro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Cronômetro")

        self.label_tempo = tk.Label(self.janela, text="00:00:00", font=("Helvetica", 48))
        self.label_tempo.pack(pady=20)

        self.botao_iniciar = tk.Button(self.janela, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack(pady=10)

        self.botao_parar = tk.Button(self.janela, text="Parar", state=tk.DISABLED, command=self.parar_cronometro)
        self.botao_parar.pack(pady=10)

        #nao tem botao pra reiniciar

        self.tempo_inicial = 0
        self.tempo_decorrido = 0
        self.executando = False

    def iniciar_cronometro(self):
        if not self.executando:
            self.tempo_inicial = time.time() - self.tempo_decorrido
            self.executando = True
            self.atualizar_cronometro()

            self.botao_iniciar.config(state=tk.DISABLED)
            self.botao_parar.config(state=tk.NORMAL)

    def parar_cronometro(self):
        if self.executando:
            self.janela.after_cancel(self.atualizacao)
            self.tempo_decorrido = time.time() - self.tempo_inicial
            self.executando = False

            self.botao_iniciar.config(state=tk.NORMAL)
            self.botao_parar.config(state=tk.DISABLED)

    def atualizar_cronometro(self):
        if self.executando:
            tempo_atual = time.time() - self.tempo_inicial
            tempo_formatado = self.formatar_tempo(tempo_atual)
            self.label_tempo.config(text=tempo_formatado)
            self.atualizacao = self.janela.after(1000, self.atualizar_cronometro)

    #nao tem funcao pra reiniciar o cronometro

    def formatar_tempo(self, tempo):
        minutos = int(tempo // 60)
        segundos = int(tempo % 60)
        horas = int(minutos // 60)
        minutos %= 60

        return f"{horas:02d}:{minutos:02d}:{segundos:02d}" #nao tem decisegundos nem centisegundos

    def iniciar(self):
        self.janela.mainloop()

cronometro = Cronometro()
cronometro.iniciar()
