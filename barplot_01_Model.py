# Modell:

# import der notwendigen Pakete:
import os
import pandas as pd


class Burned_Area_Model:
    def __init__(self, csv_file, noneed_regions):
        # Existiert die angegebene Datei?
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"Die Datei {csv_file} wurde nicht gefunden.")

        # CSV-Datei laden und feststellen, ob Laden erfolgreich war:
        try:
            self.data = pd.read_csv(csv_file)
        except Exception as e:
            raise IOError(f"Fehler beim Laden der Datei {csv_file}: {e}")

        # Überprüfung, ob die notwendigen Spalten in der Datei vorhanden sind:
        required_columns = {'Entity', 'Year', 'Annual share of the total land area burnt by wildfires'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Die CSV-Datei muss die Spalten {required_columns} enthalten.")

        # Alle Entities in 'area_list' definieren
        self.area_list = self.data['Entity'].unique()

        # Unbrauchbare Entities aus 'area_list' entfernen
        self.noneed_regions = noneed_regions
        self.regions_countries = [entity for entity in self.area_list if entity not in self.noneed_regions]

    def get_data(self):
        """Gibt die vollständigen Daten zurück."""
        return self.data

    def get_regions_countries(self):
        """Gibt die bereinigten Regionen und Länder zurück."""

        return self.regions_countries


# Beispiel für die Verwendung der Modellklasse
if __name__ == "__main__":
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

    # Instanziieren des Modells und Laden der Daten
    wildf_data = Burned_Area_Model("share-of-the-total-land-area-burnt-by-wildfires-each-year.csv",
                                   noneed_regions)

    # Zugriff auf die Daten und bereinigten Regionen
    all_data = wildf_data.get_data()
    valid_regions = wildf_data.get_regions_countries()

    print("Alle Daten geladen.")
    print("Bereinigte Regionen und Länder:", valid_regions, len(valid_regions))
