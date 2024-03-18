import tkinter as tk
import pyautogui
import threading

class GameAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Automation")
        
        self.start_button = tk.Button(root, text="Start Automation", command=self.start_automation)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop Automation", command=self.stop_automation, state="disabled")
        self.stop_button.pack(pady=5)
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)
        
        self.running = False
    
    def start_automation(self):
        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.status_label.config(text="Automation running...")
        
        threading.Thread(target=self.run_automation).start()
    
    def stop_automation(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_label.config(text="Automation stopped.")
    
    def run_automation(self):
        while self.running:
            # Aqui você pode adicionar a lógica da automação usando o PyAutoGUI
            # Por exemplo, clique em coordenadas específicas na tela
            pyautogui.click(100, 100)
            # ou envie pressionamentos de tecla
            pyautogui.press('space')
            # ou qualquer outra ação necessária para automatizar o jogo
            
            # Coloque um pequeno atraso para evitar sobrecarregar o sistema
            pyautogui.sleep(1)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = GameAutomationApp(root)
    root.mainloop()
