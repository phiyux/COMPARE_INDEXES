import tkinter as tk
import tkinter.filedialog as filedialog

def select_file(file_var):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_var.set(file_path)

def compare_files():
    file1_path = file1_var.get()
    file2_path = file2_var.get()
    output_file_path = "anomalies.txt"  # Chemin de sortie par défaut

    # Vérifier si les fichiers ont été sélectionnés
    if file1_path == "" or file2_path == "":
        print("Veuillez sélectionner les deux fichiers à comparer.")
        return

    # Ouvrir les fichiers en mode lecture
    with open(file1_path, 'r', encoding='utf-8-sig') as file1, open(file2_path, 'r', encoding='utf-8-sig') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    # Obtenir les en-têtes des colonnes
    header1 = file1_lines[0].strip().split('\t')
    header2 = file2_lines[0].strip().split('\t')

    # Comparer les lignes des fichiers
    diff_lines = []
    for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines)):
        if line1 != line2:
            diff_lines.append(f"Différence à la ligne {i+1}:\n")
            diff_lines.append(f"INDEXES_DEV: {line1.strip()}\n")
            diff_lines.append(f"INDEXES_RECT: {line2.strip()}\n")

            # Trouver les colonnes avec des différences
            values1 = line1.strip().split('\t')
            values2 = line2.strip().split('\t')
            diff_columns = [header1[j] for j in range(len(values1)) if values1[j] != values2[j]]
            diff_lines.append(f"Colonnes avec des différences : {', '.join(diff_columns)}\n")


            diff_lines.append('\n')

    # Écrire les différences dans un fichier de sortie
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(diff_lines)

    print("Comparaison terminée. Les différences ont été enregistrées dans le fichier 'anomalies.txt'.")

# Create a new instance of Tkinter
window = tk.Tk()

# Set the window title
window.title("Comparaisons Indexes")

# Set the window dimensions
window.geometry("400x300")

# Variables pour stocker les chemins d'accès aux fichiers
file1_var = tk.StringVar()
file2_var = tk.StringVar()

# Fonction pour sélectionner le fichier INDEXES_DEV.txt
def select_file1():
    select_file(file1_var)

# Fonction pour sélectionner le fichier INDEXES_RECT.txt
def select_file2():
    select_file(file2_var)

# Boutons pour sélectionner les fichiers
button1 = tk.Button(window, text="Sélectionner INDEXES_DEV.txt", command=select_file1)
button1.pack(pady=10)

button2 = tk.Button(window, text="Sélectionner INDEXES_RECT.txt", command=select_file2)
button2.pack(pady=10)

# Bouton pour comparer les fichiers
compare_button = tk.Button(window, text="Comparer les fichiers", command=compare_files)
compare_button.pack(pady=10)

# Start the main event loop
window.mainloop()
