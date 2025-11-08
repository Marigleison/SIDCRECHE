import tkinter as tk
from tkinter.ttk import Label
from PIL import Image, ImageTk
import tkintermapview
import pygame

LOCALIDADES = {
    'ALERTA': {
        'nome': 'UniFBV-Wyden',
        'coordenadas': (-8.1069, -34.9151),
        'endereco': 'R. Jean Emile Favre, 422 - Imbiribeira'
    },
    'CRECHE1': {
        'nome': 'Centro de Progressão Nossa Senhora das Graças',
        'coordenadas': (-8.0979, -34.9311),
        'endereco': 'Av. Cap. Gregório de Caldas, 302 - Areias'
    },
    "CRECHE2": {
        'nome': '',
        'coordenadas': (),
        'endereco': ''
    }
}

class ESPAlerta:
    def __init__(self):
        self.janela = None

    def fechar(self, event=None):
        pygame.mixer.music.stop()
        if self.janela:
            self.janela.destroy()
            self.janela = None

    def abrir_mapa(self, local):
        dados = LOCALIDADES.get(local, LOCALIDADES['ALERTA'])
        lat, lon = dados['coordenadas']

        mapa_janela = tk.Toplevel()
        mapa_janela.title("Mapa do Alerta")
        mapa_janela.attributes('-fullscreen', True)
        mapa_janela.configure(bg='#111')
        mapa_janela.iconbitmap('favicon.ico')
        mapa_janela.state("zoomed")

        pygame.mixer.music.stop()

        tk.Label(
            mapa_janela,
            text="Localização do Alerta 🔥",
            font=('Arial', 24, 'bold'),
            fg='red',
            bg='#111'
        ).pack(pady=20)

        mapa = tkintermapview.TkinterMapView(mapa_janela, corner_radius=0)
        mapa.pack(fill="both", expand=True)

        mapa.set_position(lat, lon)
        mapa.set_zoom(17)
        mapa.set_marker(
            lat, lon,
            text=f"{dados['nome']}\n{dados['endereco']}",
            font=('Arial', 11, 'bold')
        )

        tk.Button(
            mapa_janela,
            text="Fechar Mapa",
            command=mapa_janela.destroy,
            font=('Arial', 12, 'bold'),
            bg='red', fg='white',
            activebackground='#550000',
            relief='flat',
            padx=10, pady=5
        ).pack(pady=15)

        mapa_janela.mainloop()

    def piscar_texto(self, label):
        atual = label.cget("fg")
        nova_cor = "black" if atual == "red" else "red"
        label.config(fg=nova_cor)
        label.after(500, lambda: self.piscar_texto(label))

    def start(self, local):
        if self.janela:
            return

        self.janela = tk.Tk()
        self.janela.title('🚨 Alerta do ESP32')
        self.janela.configure(bg='black')
        self.janela.iconbitmap('favicon.ico')
        self.janela.attributes('-fullscreen', True)
        self.janela.focus_force()

        warn = Image.open('warning.png').resize((250, 250))
        warntk = ImageTk.PhotoImage(warn)
        Label.image = warntk

        texto_alerta = tk.Label(
            self.janela,
            image=warntk,
            compound='top',
            text='⚠️ ALERTA DE INCÊNDIO ⚠️',
            font=('Arial', 32, 'bold'),
            fg='red',
            bg='black'
        )
        texto_alerta.pack(pady=40)

        self.piscar_texto(texto_alerta)

        tk.Label(
            self.janela,
            text="Pressione [ESPAÇO] para abrir o mapa",
            font=('Arial', 16),
            fg='white',
            bg='black'
        ).pack(pady=40)

        pygame.mixer.init()
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play(-1)

        self.janela.bind('<space>', lambda event: self.abrir_mapa(local))
        self.janela.bind('<Escape>', lambda event: self.fechar())

        self.janela.mainloop()
