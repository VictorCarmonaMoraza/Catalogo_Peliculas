import tkinter as tk


def main():
    root = tk.Tk()
    ##Agregamos un titulo a la ventana
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/pelicula.ico')
    root.resizable(1,0)

    root.mainloop()

if __name__ =='__main__':
    main()