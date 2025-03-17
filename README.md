import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D

def obtener_puntos():
    try:
        P1 = np.array([float(entry_p1_x.get()), float(entry_p1_y.get()), float(entry_p1_z.get())])
        P2 = np.array([float(entry_p2_x.get()), float(entry_p2_y.get()), float(entry_p2_z.get())])
        P3 = np.array([float(entry_p3_x.get()), float(entry_p3_y.get()), float(entry_p3_z.get())])
        
        if verificar_puntos(P1, P2, P3):
            A, B, C, D = calcular_ecuacion_plano(P1, P2, P3)
            label_resultado.config(text=f"Ecuación del plano: {A}x + {B}y + {C}z + ({D}) = 0")
            graficar_plano(P1, P2, P3, A, B, C, D)
        else:
            label_resultado.config(text="No se puede graficar un plano con los puntos ingresados.")
            borrar_datos()
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

def verificar_puntos(P1, P2, P3):
    if np.array_equal(P1, P2) or np.array_equal(P1, P3) or np.array_equal(P2, P3):
        return False
    
    v1 = P2 - P1
    v2 = P3 - P1
    normal = np.cross(v1, v2)
    if np.all(normal == 0):
        return False
    
    return True

def calcular_ecuacion_plano(P1, P2, P3):
    v1 = P2 - P1
    v2 = P3 - P1
    normal = np.cross(v1, v2)
    A, B, C = normal
    D = -np.dot(normal, P1)
    return A, B, C, D

def graficar_plano(P1, P2, P3, A, B, C, D):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    gx, gy = np.meshgrid(np.linspace(-5, 10, 10), np.linspace(-5, 10, 10))
    gz = (-D - A*gx - B*gy) / C
    
    ax.plot_surface(gy, gx, gz, alpha=0.5, color='cyan')
    ax.scatter(*P1, color='red', s=100)
    ax.scatter(*P2, color='blue', s=100)
    ax.scatter(*P3, color='green', s=100)
    
    ax.text(*P1, f'({P1[0]}, {P1[1]}, {P1[2]})', color='black')
    ax.text(*P2, f'({P2[0]}, {P2[1]}, {P2[2]})', color='black')
    ax.text(*P3, f'({P3[0]}, {P3[1]}, {P3[2]})', color='black')
    
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    plt.show()

def borrar_datos():
    entry_p1_x.delete(0, tk.END)
    entry_p1_y.delete(0, tk.END)
    entry_p1_z.delete(0, tk.END)
    entry_p2_x.delete(0, tk.END)
    entry_p2_y.delete(0, tk.END)
    entry_p2_z.delete(0, tk.END)
    entry_p3_x.delete(0, tk.END)
    entry_p3_y.delete(0, tk.END)
    entry_p3_z.delete(0, tk.END)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Cálculo de Plano en 3D")

tk.Label(root, text="Ingrese los puntos:").grid(row=0, column=1)

tk.Label(root, text="P1 (x, y, z):").grid(row=1, column=0)
entry_p1_x = tk.Entry(root)
entry_p1_y = tk.Entry(root)
entry_p1_z = tk.Entry(root)
entry_p1_x.grid(row=1, column=1)
entry_p1_y.grid(row=1, column=2)
entry_p1_z.grid(row=1, column=3)

tk.Label(root, text="P2 (x, y, z):").grid(row=2, column=0)
entry_p2_x = tk.Entry(root)
entry_p2_y = tk.Entry(root)
entry_p2_z = tk.Entry(root)
entry_p2_x.grid(row=2, column=1)
entry_p2_y.grid(row=2, column=2)
entry_p2_z.grid(row=2, column=3)

tk.Label(root, text="P3 (x, y, z):").grid(row=3, column=0)
entry_p3_x = tk.Entry(root)
entry_p3_y = tk.Entry(root)
entry_p3_z = tk.Entry(root)
entry_p3_x.grid(row=3, column=1)
entry_p3_y.grid(row=3, column=2)
entry_p3_z.grid(row=3, column=3)

btn_calcular = tk.Button(root, text="Calcular Plano", command=obtener_puntos)
btn_calcular.grid(row=4, column=1, columnspan=3)

label_resultado = tk.Label(root, text="")
label_resultado.grid(row=5, column=1, columnspan=3)

root.mainloop()
