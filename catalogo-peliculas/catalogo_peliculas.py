import tkinter as tk
from client.gui_app import Frame


def main():
    root = tk.Tk()
    ##Agregamos un titulo a la ventana
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/pelicula.ico')
    root.resizable(0,0)


    app = Frame(root = root)
    ##frame =tk.Frame(root)
    ##frame.pack()
    ##frame.config(width=480, height=320, bg='green')'''
    #root.mainloop()

    app.mainloop()

if __name__ =='__main__':
    main()