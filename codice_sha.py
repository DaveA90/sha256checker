import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os

def genera_checksum():
    """Genera il checksum del file selezionato usando certutil."""
    file_path = file_path_entry.get()
    algoritmo = algoritmo_var.get()

    if not os.path.exists(file_path):
        messagebox.showerror("Errore", "File non trovato. Inserisci un percorso valido.")
        return

    comando = ["certutil", "-hashfile", file_path, algoritmo]

    try:
        processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        stdout, stderr = processo.communicate()

        if stderr:
            messagebox.showerror("Errore", f"Errore durante l'esecuzione di certutil:\n{stderr.decode()}")
            output_text.delete("1.0", tk.END)
            return

        output = stdout.decode()
        linee = output.splitlines()
        hash_valore = None
        for linea in linee:
            if algoritmo.upper() in linea and "hash" in linea.lower():
                hash_valore = linee[linee.index(linea)+1].strip()
                break

        if hash_valore:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, f"Checksum {algoritmo.upper()} per:\n{file_path}\n\n")
            output_text.insert(tk.END, f"{hash_valore}\n")
        else:
            messagebox.showerror("Errore", "Impossibile estrarre l'hash dall'output di certutil.")
            output_text.delete("1.0", tk.END)

    except FileNotFoundError:
        messagebox.showerror("Errore", "Certutil non trovato nel sistema.")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore inatteso:\n{e}")

def seleziona_file():
    """Apre la finestra di dialogo per selezionare il file per il checksum."""
    file_path = filedialog.askopenfilename(title="Seleziona File per Checksum")
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def salva_checksum_file():
    """Salva il checksum in un file .sha1 o .sha256."""
    checksum_text = output_text.get("1.0", tk.END).strip()
    if not checksum_text:
        messagebox.showinfo("Info", "Nessun checksum da salvare. Genera prima un checksum.")
        return

    file_path = file_path_entry.get()
    algoritmo = algoritmo_var.get()
    if file_path:
        nome_file_base = os.path.splitext(os.path.basename(file_path))[0]
        estensione_checksum = algoritmo.lower()
        nome_file_salvataggio_suggerito = f"{nome_file_base}.{estensione_checksum}" # Estensione .sha1 o .sha256
    else:
        nome_file_salvataggio_suggerito = f"checksum.{algoritmo.lower()}"

    file_salvataggio = filedialog.asksaveasfilename(
        defaultextension=f".{algoritmo.lower()}", # Definisce l'estensione predefinita in base all'algoritmo
        filetypes=[(f"File {algoritmo.upper()}", f"*.{algoritmo.lower()}"), ("Tutti i file", "*.*")],
        initialfile=nome_file_salvataggio_suggerito,
        title="Salva file checksum"
    )

    if file_salvataggio:
        try:
            with open(file_salvataggio, "w") as f:
                if dettagli_var.get():
                    f.write(f"{algoritmo.upper()}:\n")
                    f.write(f"File: {os.path.basename(file_path)}\n")
                    f.write(checksum_text + "\n")
                else:
                    f.write(checksum_text)
            messagebox.showinfo("Successo", f"Checksum salvato con successo in:\n{file_salvataggio}")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il salvataggio del file:\n{e}")

def pulisci_output():
    """Pulisce l'area di testo dell'output."""
    output_text.delete("1.0", tk.END)

def seleziona_file_verifica():
    """Apre la finestra di dialogo per selezionare il file da verificare."""
    file_path_verifica = filedialog.askopenfilename(title="Seleziona File da Verificare")
    file_path_verifica_entry.delete(0, tk.END)
    file_path_verifica_entry.insert(0, file_path_verifica)

def seleziona_checksum_file_verifica():
    """Apre la finestra di dialogo per selezionare il file checksum per la verifica."""
    checksum_file_path = filedialog.askopenfilename(
        title="Seleziona File Checksum (.sha1 o .sha256)",
        filetypes=[("File Checksum", "*.sha1 *.sha256"), ("Tutti i file", "*.*")]
    )
    checksum_file_path_entry.delete(0, tk.END)
    checksum_file_path_entry.insert(0, checksum_file_path)

def verifica_integrita_file():
    """Verifica l'integrità del file confrontando il checksum calcolato con quello nel file."""
    file_path_verifica = file_path_verifica_entry.get()
    checksum_file_path = checksum_file_path_entry.get()

    if not os.path.exists(file_path_verifica):
        messagebox.showerror("Errore", "File da verificare non trovato.")
        return
    if not os.path.exists(checksum_file_path):
        messagebox.showerror("Errore", "File checksum non trovato.")
        return

    try:
        with open(checksum_file_path, "r") as f_checksum:
            checksum_file_content = f_checksum.read().strip()
            # Prova a estrarre l'hash se il file contiene dettagli aggiuntivi
            checksum_da_file = None
            for line in checksum_file_content.splitlines():
                line = line.strip()
                if len(line) == 64 or len(line) == 40: # Lunghezza tipica SHA256 o SHA1
                    checksum_da_file = line
                    break
            if not checksum_da_file:
                checksum_da_file = checksum_file_content # Altrimenti usa tutto il contenuto se non trova una riga hash chiara

        algoritmo_verifica = None
        if checksum_file_path.lower().endswith(".sha256"):
            algoritmo_verifica = "SHA256"
        elif checksum_file_path.lower().endswith(".sha1"):
            algoritmo_verifica = "SHA1"
        else:
            messagebox.showerror("Errore", "Impossibile determinare l'algoritmo dal file checksum. Usa .sha1 o .sha256.")
            return

        comando_verifica = ["certutil", "-hashfile", file_path_verifica, algoritmo_verifica]
        processo_verifica = subprocess.Popen(comando_verifica, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        stdout_verifica, stderr_verifica = processo_verifica.communicate()

        if stderr_verifica:
            messagebox.showerror("Errore", f"Errore durante il calcolo del checksum per la verifica:\n{stderr_verifica.decode()}")
            return

        output_verifica = stdout_verifica.decode()
        linee_verifica = output_verifica.splitlines()
        checksum_calcolato = None
        for linea in linee_verifica:
            if algoritmo_verifica.upper() in linea and "hash" in linea.lower():
                checksum_calcolato = linee_verifica[linee_verifica.index(linea)+1].strip()
                break

        if checksum_calcolato == checksum_da_file:
            risultato_verifica_label.config(text="Integrità File: Valida", fg="green")
        else:
            risultato_verifica_label.config(text="Integrità File: NON Valida", fg="red")

    except FileNotFoundError:
        messagebox.showerror("Errore", "Certutil non trovato nel sistema.")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la verifica dell'integrità:\n{e}")


# Configurazione finestra principale
root = tk.Tk()
root.title("Generatore e Verificatore Checksum di Sicurezza")
root.geometry("700x650") # Aumenta l'altezza per la nuova sezione

frame_principale = tk.Frame(root, padx=20, pady=20)
frame_principale.pack(fill=tk.BOTH, expand=True)

# --- Sezione Genera Checksum ---
genera_frame = tk.LabelFrame(frame_principale, text="Genera Checksum", padx=10, pady=10)
genera_frame.pack(fill=tk.X, pady=(0, 10))

# Seleziona File (Sezione Genera)
file_label = tk.Label(genera_frame, text="Seleziona File:")
file_label.grid(row=0, column=0, sticky=tk.W, pady=5)

file_path_entry = tk.Entry(genera_frame, width=50)
file_path_entry.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E, pady=5)

browse_button = tk.Button(genera_frame, text="Sfoglia", command=seleziona_file)
browse_button.grid(row=0, column=3, padx=5, pady=5)

# Algoritmo Checksum (Sezione Genera)
algoritmo_label = tk.Label(genera_frame, text="Algoritmo:")
algoritmo_label.grid(row=1, column=0, sticky=tk.W, pady=5)

algoritmo_var = tk.StringVar(value="SHA256")
sha1_radio = tk.Radiobutton(genera_frame, text="SHA-1", variable=algoritmo_var, value="SHA1")
sha256_radio = tk.Radiobutton(genera_frame, text="SHA-256", variable=algoritmo_var, value="SHA256")
sha1_radio.grid(row=1, column=1, sticky=tk.W, pady=5)
sha256_radio.grid(row=1, column=2, sticky=tk.W, pady=5)

# Bottone Genera Checksum (Sezione Genera)
genera_button = tk.Button(genera_frame, text="Genera Checksum", command=genera_checksum, width=15)
genera_button.grid(row=2, column=1, columnspan=2, pady=10)

# Output Checksum (Sezione Genera)
output_label = tk.Label(genera_frame, text="Checksum:")
output_label.grid(row=3, column=0, sticky=tk.W, pady=5)

output_text = tk.Text(genera_frame, height=8, width=60) # Altezza ridotta
output_text.grid(row=4, column=0, columnspan=4, sticky=tk.W+tk.E+tk.N+tk.S, pady=5)

scrollbar = tk.Scrollbar(genera_frame, command=output_text.yview)
scrollbar.grid(row=4, column=4, sticky='ns')
output_text.config(yscrollcommand=scrollbar.set)

# Opzioni di salvataggio (Sezione Genera)
dettagli_var = tk.BooleanVar()
dettagli_checkbox = tk.Checkbutton(genera_frame, text="Includi dettagli nel file (Algoritmo, Nome File)", variable=dettagli_var)
dettagli_checkbox.grid(row=5, column=0, columnspan=4, sticky=tk.W, pady=5)

# Bottoni Salva e Pulisci (Sezione Genera)
salva_button = tk.Button(genera_frame, text="Salva Checksum", command=salva_checksum_file, width=15)
salva_button.grid(row=6, column=1, pady=10)

pulisci_button = tk.Button(genera_frame, text="Pulisci Output", command=pulisci_output, width=15)
pulisci_button.grid(row=6, column=2, pady=10, padx=5)


# --- Sezione Verifica Integrità File ---
verifica_frame = tk.LabelFrame(frame_principale, text="Verifica Integrità File", padx=10, pady=10)
verifica_frame.pack(fill=tk.X, pady=(10, 0)) # Spazio sopra

# File da Verificare (Sezione Verifica)
file_verifica_label = tk.Label(verifica_frame, text="File da Verificare:")
file_verifica_label.grid(row=0, column=0, sticky=tk.W, pady=5)

file_path_verifica_entry = tk.Entry(verifica_frame, width=50)
file_path_verifica_entry.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E, pady=5)

browse_verifica_file_button = tk.Button(verifica_frame, text="Sfoglia", command=seleziona_file_verifica)
browse_verifica_file_button.grid(row=0, column=3, padx=5, pady=5)

# File Checksum (.sha1/.sha256) (Sezione Verifica)
checksum_file_label = tk.Label(verifica_frame, text="File Checksum:")
checksum_file_label.grid(row=1, column=0, sticky=tk.W, pady=5)

checksum_file_path_entry = tk.Entry(verifica_frame, width=50)
checksum_file_path_entry.grid(row=1, column=1, columnspan=2, sticky=tk.W+tk.E, pady=5)

browse_checksum_file_button = tk.Button(verifica_frame, text="Sfoglia", command=seleziona_checksum_file_verifica)
browse_checksum_file_button.grid(row=1, column=3, padx=5, pady=5)

# Bottone Verifica Integrità (Sezione Verifica)
verifica_button = tk.Button(verifica_frame, text="Verifica Integrità", command=verifica_integrita_file, width=15)
verifica_button.grid(row=2, column=1, columnspan=2, pady=10)

# Risultato Verifica (Sezione Verifica)
risultato_verifica_label = tk.Label(verifica_frame, text="Integrità File: In Attesa", fg="black")
risultato_verifica_label.grid(row=3, column=0, columnspan=4, pady=5)
risultato_verifica_label.config(font=("TkDefaultFont", 12, "bold")) # Rende il risultato più evidente


# Configurazione griglia per ridimensionamento corretto
frame_principale.columnconfigure(1, weight=1) # La colonna dell'entry si espande
genera_frame.columnconfigure(1, weight=1)
genera_frame.rowconfigure(4, weight=1)
verifica_frame.columnconfigure(1, weight=1)


root.mainloop()