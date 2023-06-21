import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.jogador_atual = "X"
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")

        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self.janela, text=" ", width=10, height=5,
                                  command=lambda row=i, col=j: self.jogar(row, col))
                botao.grid(row=i, column=j)
                linha.append(botao)
            self.botoes.append(linha)

    def jogar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] != " ": #nao esta registrando as jogadas dos jogadores
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)

            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo("Fim do Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.janela.quit()
            elif self.verificar_empate():
                messagebox.showinfo("Fim do Jogo", "O jogo empatou!")
                self.janela.quit()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self, jogador):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] == jogador:
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] == jogador:
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador:
            return True
        return False

    def verificar_empate(self):
        return all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3))

    def iniciar(self):
        self.janela.mainloop()

jogo = JogoDaVelha()
jogo.iniciar()