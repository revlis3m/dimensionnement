import tkinter as tk
from tkinter import ttk

class UMTSDimensioningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dimensionnement du Réseau UMTS")
        self.root.geometry("900x350")

        # Partie où on rentre les données
        frame_input = ttk.Frame(root, padding="20")
        frame_input.grid(row=0, column=0, sticky=tk.W)

        ttk.Label(frame_input, text="Population:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.population_entry = ttk.Entry(frame_input)
        self.population_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame_input, text="Taux de Pénétration (%):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.penetration_rate_entry = ttk.Entry(frame_input)
        self.penetration_rate_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame_input, text="Erlangs par Abonné:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.erlangs_per_subscriber_entry = ttk.Entry(frame_input)
        self.erlangs_per_subscriber_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame_input, text="Nombre de Fréquences:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.frequency_count_entry = ttk.Entry(frame_input)
        self.frequency_count_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame_input, text="Facteur de Réutilisation:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.reuse_factor_entry = ttk.Entry(frame_input)
        self.reuse_factor_entry.grid(row=4, column=1, pady=5)

        ttk.Label(frame_input, text="Taux de Blocage (%):").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.block_rate_entry = ttk.Entry(frame_input)
        self.block_rate_entry.grid(row=5, column=1, pady=5)

        ttk.Button(frame_input, text="Calculer", command=self.calculate).grid(row=6, column=0, columnspan=2, pady=10)

        # Partie pour afficher les résultats
        frame_output = ttk.Frame(root, padding="20")
        frame_output.grid(row=0, column=1, sticky=tk.W)

        self.result_label = tk.Label(frame_output, text="Les différents résultats:", justify=tk.LEFT, font=("Helvetica", 14), pady=5)
        self.result_label.grid(row=0, column=0, sticky=tk.W, pady=5)

    def calculate(self):
        try:
            population = int(self.population_entry.get())
            penetration_rate = float(self.penetration_rate_entry.get()) / 100
            erlangs_per_subscriber = float(self.erlangs_per_subscriber_entry.get())
            frequency_count = int(self.frequency_count_entry.get())
            reuse_factor = int(self.reuse_factor_entry.get())
            block_rate = float(self.block_rate_entry.get()) / 100

            # Calculs
            subscribers = population * penetration_rate
            peak_traffic = subscribers * erlangs_per_subscriber
            carriers_per_cell = frequency_count / reuse_factor
            traffic_per_cell = carriers_per_cell * 8 - 3
            cell_capacity = traffic_per_cell * 0.406  
            number_of_cells = peak_traffic / cell_capacity
            number_of_sites = number_of_cells / 3
            oversized_traffic = peak_traffic * 1.2
            oversized_cells = oversized_traffic / cell_capacity
            oversized_sites = oversized_cells / 3

            # Affichage des résultats
            results = (
                f"Trafic total à l'heure de pointe: {peak_traffic:.3f} Erlangs\n\n"
                f"Nombre de cellules nécessaires: {number_of_cells:.3f}\n\n"
                f"Nombre de sites correspondants: {number_of_sites:.3f}\n\n"
                f"Trafic total avec surdimensionnement: {oversized_traffic:.3f} Erlangs\n\n"
                f"Nombre de cellules nécessaires (surdimensionnement): {oversized_cells:.3f}\n\n"
                f"Nombre de sites correspondants (surdimensionnement): {oversized_sites:.3f}"
            )
            self.result_label.config(text=results)
        except ValueError:
            self.result_label.config(text="Erreur: Veuillez entrer des valeurs numériques valides.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UMTSDimensioningApp(root)
    root.mainloop()
