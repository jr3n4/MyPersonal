import tkinter as tk
import pyautogui
from PIL import ImageGrab

# Função para atualizar as informações de coordenadas e cor
def atualizar_informacoes():
    # Captura as coordenadas do mouse
    x, y = pyautogui.position()

    # Captura a tela inteira
    imagem = ImageGrab.grab()

    # Obtém a cor do pixel nas coordenadas do mouse
    cor_pixel = imagem.getpixel((x, y))

    # Atualiza os rótulos de coordenadas e cor
    lbl_coordenadas.config(text=f"Coordenadas do mouse (x, y): {x}, {y}")
    lbl_cor.config(text=f"Cor do pixel (RGB): {cor_pixel}")

    # Atualiza a interface a cada 100 milissegundos (0.1 segundo)
    root.after(100, atualizar_informacoes)

# Configurações da janela principal
root = tk.Tk()
root.title("Captura de Coordenadas e Cor do Pixel")
root.geometry("400x150")

# Rótulos para exibir as informações
lbl_coordenadas = tk.Label(root, text="Coordenadas do mouse (x, y): ")
lbl_coordenadas.pack()

lbl_cor = tk.Label(root, text="Cor do pixel (RGB): ")
lbl_cor.pack()

# Botão para fechar o programa
btn_fechar = tk.Button(root, text="Fechar", command=root.destroy)
btn_fechar.pack()

# Inicia a atualização das informações em tempo real
atualizar_informacoes()

# Inicia o loop principal da interface gráfica
root.mainloop()
