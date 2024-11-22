# Programm ausführen:

import tkinter as tk
from barplot_03_Controller import Burned_Area_Controller


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

