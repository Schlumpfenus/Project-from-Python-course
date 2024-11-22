# View:

# import der notwendigen Pakete:
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Burned_Area_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Anteil der verbrannten an der gesamten Landfläche nach Regionen/ Ländern")

        # Setzen der Mindestgröße des Fensters (B, H):
        self.root.minsize(1400, 800)

        # Icon für das Fenster hinzufügen:
        self.root.iconphoto(False, tk.PhotoImage(
            file='pngtree-cartoon-fire-flame-flat-icon-vector-element-png-image_6117040.png'))

        # Hauptfenster
        self.widget_frame = tk.Frame(self.root, width=300)
        self.plot_frame = tk.Frame(self.root, width=500)

        self.widget_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Frame für Auswahlzeilen:
        self.selections_frame = tk.Frame(self.widget_frame)
        self.selections_frame.pack(pady=5, fill=tk.X, expand=False)

        # Frame für die Buttons unten:
        self.button_frame = tk.Frame(self.widget_frame)
        self.button_frame.pack(pady=20, fill='x', expand=False)

        self.setup_widgets()
        self.setup_plot_area()

    def setup_widgets(self):
        # Titel:
        title_label = tk.Label(self.selections_frame, text="Auswahl Regionen/ Länder (bis zu 4)", font=("Arial", 11))
        title_label.pack(pady=10)

        # Button Auswahlzeilen hinzufügen:
        self.add_button = tk.Button(self.selections_frame, text="Land/ Region hinzufügen",
                                    command=self.add_selection_row)
        self.add_button.pack(pady=5)

        # Button um Plot zu erzeugen, oder zu löschen:
        self.plot_button = tk.Button(self.button_frame, text="Plot erzeugen", command=self.controller.plot_data,
                                     state=tk.DISABLED)
        self.plot_button.pack(fill='x', pady=5)

        # Button um den Plot zurückzusetzen:
        self.clear_button = tk.Button(self.button_frame, text="Plot löschen", command=self.clear_plot,
                                      state=tk.DISABLED)
        self.clear_button.pack(fill='x', pady=5)

        # Button Auswahlzeilen entfernen:
        self.remove_button = tk.Button(self.button_frame, text="Auswahl entfernen", command=self.remove_selection_rows,
                                       state=tk.DISABLED)
        self.remove_button.pack(fill='x', pady=5)

        # Button, um Plot zu speichern:
        self.save_button = tk.Button(self.button_frame, text="Plot speichern", command=self.save_plot,
                                     state=tk.DISABLED)
        self.save_button.pack(fill='x', pady=5)

        # Button um Anwendung zu beenden:
        self.exit_button = tk.Button(self.button_frame, text="Beenden", command=self.root.quit)
        self.exit_button.pack(fill='x', pady=5)

        # Liste, um Auswahlzeilen zu speichern:
        self.search_vars = []
        self.region_entries = []

        # Hinzufügen der ersten Auswahlzeile:
        self.add_selection_row()


    def update_dropdown(self, search_var, dropdown):
        """Filtern des Dropdowns aufgrund des Inhalts der Liste search_vars"""
        # Dropdownwerte auf Basis des Suchbegriffs aktualisieren:
        search_term = search_var.get().lower()
        valid_regions = self.controller.get_valid_regions()
        filtered_regions = [region for region in valid_regions if search_term in region.lower()]

        # Aktualisieren der Werte für das Dropdown:
        dropdown['values'] = filtered_regions
        current_value = dropdown.get()

        # Auswahl entfernen, wenn der aktuelle Wert nicht in der gefilterten Liste ist:
        if current_value not in filtered_regions:
            dropdown.set('')

    def add_selection_row(self):
        if len(self.region_entries) >= 4:
            messagebox.showwarning("Limit erreicht", "Es können maximal 4 Regionen hinzugefügt werden.")
            return

        # Neue Auswahlzeile erstellen:
        row_frame = tk.Frame(self.selections_frame)
        row_frame.pack(fill=tk.X, pady=5)

        # Hinzufügen eines Suchfeldes je Zeile:
        search_var = tk.StringVar()
        self.search_vars.append(search_var)

        # Beschriftung:
        label = tk.Label(row_frame, text="Land/ Region:")             # old ggf not needed
        label.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)


        # Dropdown-Eintrag:
        valid_regions = self.controller.get_valid_regions()
        entry = ttk.Combobox(row_frame, values=valid_regions, state="readonly")
        entry.bind("<<ComboboxSelected>>", lambda event: self.toggle_buttons())
        search_var.trace_add('write', lambda *args: self.update_dropdown(search_var, entry))
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)

        # Suchfeld:
        search_box = ttk.Entry(row_frame, textvariable=search_var)
        search_box.pack(side=tk.RIGHT, padx=5, fill=tk.X, expand=True)


        # Neue Zeile zur Liste hinzufügen
        self.region_entries.append((row_frame, label, entry))
        self.toggle_buttons()

    def remove_selection_rows(self):
        """Entfernen aller Auswahlzeilen, außer der ersten."""
        if len(self.region_entries) > 1:                                # bei Fehler, hier gucken
            row_frame, label, entry = self.region_entries.pop()
            row_frame.destroy()
            self.toggle_buttons()

            # Informieren, dass das Limit zurückgesetzt wurde
            messagebox.showinfo("Limit zurückgesetzt",
                                "Das Limit für die Anzahl der Regionen wurde zurückgesetzt. "
                                "Sie können neue Regionen hinzufügen.")

    def setup_plot_area(self):
        # Platzhalter für das Diagramm
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.ax.set_title("Leerer Plot")
        self.canvas.draw()

    def clear_plot(self):
        # Löschen des Diagramms
        self.ax.clear()
        self.ax.set_title("Leerer Plot")
        self.canvas.draw()
        self.save_button.config(state=tk.DISABLED)

    def get_selected_regions(self):
        """Rückgabe einer Liste der ausgewählten Regionen"""
        return [entry.get() for _, _, entry in self.region_entries if entry.get()]

    def update_plot(self, data):
        """Diagramm mit den ausgewählten Daten aktualisieren."""
        self.ax.clear()
        self.ax.set_title("Plot für die ausgewählten Regionen (Jahre 2012 bis YTD, Angaben in Prozent)")

        regions = list(data.keys())
        n_regions = len(regions)

        # flexible Breite der Balken:
        bar_width = 0.8 / n_regions

        # x-Positionen initialisieren
        x_positions = np.arange(len(data[regions[0]]['Year']))

        # jeden Bereich in einem separaten Balken zeichnen:
        for idx, (region, year_data) in enumerate(data.items()):
            years = year_data['Year']
            values = year_data['Annual share of the total land area burnt by wildfires']

            # x-Position für jeden Bereich versetzen
            offset = bar_width * idx
            self.ax.bar(x_positions + offset, values, bar_width, label=region)

        self.ax.set_xticks(x_positions + bar_width * (n_regions-1) / 2)
        self.ax.set_xticklabels(years, rotation=45, ha="right")
        self.ax.legend()

        self.fig.tight_layout()
        self.canvas.draw()

        # Aktivieren des Buttons "Plot speichern" und "Plot löschen":
        self.save_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)

    def toggle_buttons(self):
        """Buttons aktiv oder inaktiv, je nach Benutzerinteraktion."""
        selected_regions = self.get_selected_regions()
        self.plot_button.config(state=tk.NORMAL if selected_regions else tk.DISABLED)
        self.remove_button.config(state=tk.NORMAL if len(self.region_entries) > 1 else tk.DISABLED)

    def save_plot(self):
        # Aktuellen Plot als .png-Datei speichern:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.fig.savefig(file_path)
            messagebox.showinfo("Gespeichert", f"Plot wurde unter {file_path} gespeichert.")



