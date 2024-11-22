#  Controller:

# import der notwendigen Pakete
from barplot_01_Model import Burned_Area_Model
from barplot_02_View import Burned_Area_View
import tkinter as tk
from tkinter import messagebox


# import pandas as pd


class Burned_Area_Controller:
    def __init__(self, root, csv_file, noneed_regions):
        # Modell instanziieren
        self.model = Burned_Area_Model(csv_file, noneed_regions)

        # View instanziieren und mit dem Controller initialisieren
        self.view = Burned_Area_View(root, self)

    def get_valid_regions(self):
        """Rückgabe einer bereinigten Regionen- und Länderliste."""
        return self.model.get_regions_countries()

    def plot_data(self):
        """Ausführen des Plots für ausgewählte Regionen ."""
        selected_regions = self.view.get_selected_regions()
        if not selected_regions:
            messagebox.showinfo("Keine Auswahl", "Bitte wählen Sie mindestens eine Region aus.")
            return

        data = self.model.get_data()
        plot_data = {}

        for region in selected_regions:
            region_data = data[data['Entity'] == region]
            plot_data[region] = {
                'Year': region_data['Year'],
                'Annual share of the total land area burnt by wildfires': region_data[
                    'Annual share of the total land area burnt by wildfires']
            }

        self.view.update_plot(plot_data)


if __name__ == "__main__":
    root = tk.Tk()

    # Definieren der unbrauchbaren Entities
    noneed_regions = ['Africa (FAO)', 'Americas (FAO)', 'Asia (FAO)', 'Belgium-Luxembourg (FAO)', 'Caribbean (FAO)',
                      'Central America (FAO)', 'Central Asia (FAO)', 'China (FAO)', 'Eastern Africa (FAO)',
                      'Eastern Asia (FAO)', 'Eastern Europe (FAO)', 'Ethiopia (former)', 'Europe (FAO)',
                      'European Union (27)', 'European Union (27) (FAO)', 'High-income countries',
                      'Land Locked Developing Countries (FAO)', 'Least Developed Countries (FAO)',
                      'Low Income Food Deficit Countries (FAO)', 'Low-income countries',
                      'Lower-middle-income countries',
                      'Micronesia (FAO)', 'Middle Africa (FAO)', 'Net Food Importing Developing Countries (FAO)',
                      'Northern Africa (FAO)', 'Northern America (FAO)', 'Northern Europe (FAO)', 'Oceania (FAO)',
                      'Small Island Developing States (FAO)', 'South America (FAO)', 'South-eastern Asia (FAO)',
                      'Southern Africa (FAO)', 'Southern Asia (FAO)', 'Southern Europe (FAO)', 'Serbia and Montenegro',
                      'Sudan (former)', 'USSR', 'Upper-middle-income countries', 'Western Africa (FAO)',
                      'Western Asia (FAO)', 'Western Europe (FAO)', 'Western Sahara', 'Yugoslavia', 'Czechoslovakia']

    # Controller mit der CSV-Datei und den unbrauchbaren Regionen starten
    controller = Burned_Area_Controller(root, 'share-of-the-total-land-area-burnt-by-wildfires-each-year.csv',
                                        noneed_regions)

    root.mainloop()
