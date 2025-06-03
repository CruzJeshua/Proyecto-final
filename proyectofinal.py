import tkinter as tk
from tkinter import ttk, messagebox

medicos, enfermeros, pacientes, camas = [], [], [], []
areas = ["Pediatria", "Cirugia", "Oncologia", "Cardiologia"]

class Medico:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

class Enfermero:
    def __init__(self, nombre, id_cama):
        self.nombre = nombre
        self.id_cama = id_cama

class Paciente:
    def __init__(self, nombre, apellido, idp, sintoma):
        self.nombre = nombre
        self.apellido = apellido
        self.idp = idp
        self.sintoma = sintoma

class Cama:
    def __init__(self, id_cama):
        self.id_cama = id_cama
        self.ocupada = False

def agregar_medico():
    nombre = m_nombre.get().strip()
    area = m_area.get().strip()
    if nombre == "" or area == "":
        messagebox.showwarning("Error", "Debe ingresar nombre y área para el médico")
        return
    medicos.append(Medico(nombre, area))
    actualizar_lista()
    m_nombre.delete(0, tk.END)
    m_area.set('')

def agregar_enfermero():
    nombre = e_nombre.get().strip()
    id_cama_val = e_cama.get().strip()
    if nombre == "" or id_cama_val == "":
        messagebox.showwarning("Error", "Debe ingresar nombre y ID de cama para el enfermero")
        return
    cama_encontrada = None
    for c in camas:
        if c.id_cama == id_cama_val:
            cama_encontrada = c
            break
    if cama_encontrada is None:
        messagebox.showerror("Error", f"No existe la cama con ID '{id_cama_val}'")
        return
    if cama_encontrada.ocupada:
        messagebox.showerror("Error", f"La cama con ID '{id_cama_val}' está ocupada")
        return
    enfermeros.append(Enfermero(nombre, id_cama_val))
    cama_encontrada.ocupada = True
    actualizar_lista()
    e_nombre.delete(0, tk.END)
    e_cama.delete(0, tk.END)

def agregar_paciente():
    nombre = p_nombre.get().strip()
    apellido = p_apellido.get().strip()
    idp = p_id.get().strip()
    sintoma = p_sintoma.get().strip()
    if nombre == "" or apellido == "" or idp == "" or sintoma == "":
        messagebox.showwarning("Error", "Debe completar todos los campos del paciente")
        return
    pacientes.append(Paciente(nombre, apellido, idp, sintoma))
    actualizar_lista()
    p_nombre.delete(0, tk.END)
    p_apellido.delete(0, tk.END)
    p_id.delete(0, tk.END)
    p_sintoma.delete(0, tk.END)

def agregar_cama():
    id_cama_val = c_id.get().strip()
    if id_cama_val == "":
        messagebox.showwarning("Error", "Debe ingresar el ID de la cama")
        return
    for c in camas:
        if c.id_cama == id_cama_val:
            messagebox.showerror("Error", "Ya existe una cama con ese ID")
            return
    camas.append(Cama(id_cama_val))
    actualizar_lista()
    c_id.delete(0, tk.END)

def actualizar_lista():
    lista.delete(0, tk.END)
    for m in medicos:
        lista.insert(tk.END, f"Médico: {m.nombre} - Área: {m.area}")
    for e in enfermeros:
        lista.insert(tk.END, f"Enfermero: {e.nombre} - Cama ID: {e.id_cama}")
    for p in pacientes:
        lista.insert(tk.END, f"Paciente: {p.nombre} {p.apellido} - ID:{p.idp} - Síntoma: {p.sintoma}")
    for c in camas:
        lista.insert(tk.END, f"Cama ID: {c.id_cama} - {'Ocupada' if c.ocupada else 'Libre'}")

app = tk.Tk()
app.title("Gestión Hospitalaria Simple")

frm_medico = tk.LabelFrame(app, text="Agregar Médico")
frm_medico.pack(padx=5, pady=3, fill="x")
tk.Label(frm_medico, text="Nombre").grid(row=0, column=0)
m_nombre = tk.Entry(frm_medico); m_nombre.grid(row=0, column=1)
tk.Label(frm_medico, text="Área").grid(row=0, column=2)
m_area = ttk.Combobox(frm_medico, values=areas); m_area.grid(row=0, column=3)
tk.Button(frm_medico, text="Agregar", command=agregar_medico).grid(row=0, column=4)

frm_enfermero = tk.LabelFrame(app, text="Agregar Enfermero")
frm_enfermero.pack(padx=5, pady=3, fill="x")
tk.Label(frm_enfermero, text="Nombre").grid(row=0, column=0)
e_nombre = tk.Entry(frm_enfermero); e_nombre.grid(row=0, column=1)
tk.Label(frm_enfermero, text="ID de Cama").grid(row=0, column=2)
e_cama = tk.Entry(frm_enfermero); e_cama.grid(row=0, column=3)
tk.Button(frm_enfermero, text="Agregar", command=agregar_enfermero).grid(row=0, column=4)

frm_paciente = tk.LabelFrame(app, text="Agregar Paciente")
frm_paciente.pack(padx=5, pady=3, fill="x")
tk.Label(frm_paciente, text="Nombre").grid(row=0, column=0)
p_nombre = tk.Entry(frm_paciente); p_nombre.grid(row=0, column=1)
tk.Label(frm_paciente, text="Apellido").grid(row=0, column=2)
p_apellido = tk.Entry(frm_paciente); p_apellido.grid(row=0, column=3)
tk.Label(frm_paciente, text="ID").grid(row=0, column=4)
p_id = tk.Entry(frm_paciente); p_id.grid(row=0, column=5)
tk.Label(frm_paciente, text="Síntoma").grid(row=0, column=6)
p_sintoma = tk.Entry(frm_paciente); p_sintoma.grid(row=0, column=7)
tk.Button(frm_paciente, text="Agregar", command=agregar_paciente).grid(row=0, column=8)

frm_cama = tk.LabelFrame(app, text="Agregar Cama")
frm_cama.pack(padx=5, pady=3, fill="x")
tk.Label(frm_cama, text="ID de Cama").grid(row=0, column=0)
c_id = tk.Entry(frm_cama); c_id.grid(row=0, column=1)
tk.Button(frm_cama, text="Agregar Cama", command=agregar_cama).grid(row=0, column=2)

lista = tk.Listbox(app, width=100)
lista.pack(padx=5, pady=5)

app.mainloop()