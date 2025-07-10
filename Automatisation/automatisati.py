import time
import os
import joblib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd

CSV_PATH = r"C:\Users\sanba\Desktop\Me\cmc\PROJET\PFE\MISE EN CIRCULATION\file_path .csv"
LOG_FILE = "last_row.txt"
EXPORT_PATH = "nouveau_data.csv"
MODEL_DIR = r"C:\Users\sanba\Desktop\Me\cmc\PROJET\PFE\MODEL"

class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, path='.', recursive=False)
        self.observer.start()
        print("🔍 Watching for changes...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(CSV_PATH):
            print("📄 File modified: checking for new rows...")
            self.check_new_rows()

    def check_new_rows(self):
        df = pd.read_csv(CSV_PATH)
        current_row_count = len(df)

        if not os.path.exists(LOG_FILE):
            last_row = 0
        else:
            with open(LOG_FILE, "r") as f:
                last_row = int(f.read())

        if current_row_count > last_row:
            print(" Detected new rows!")
            new_data = df.iloc[last_row:]
            print(" New Data:")
            print(new_data)

            # Nettoyage des dates
            new_data["DATE VISITE"] = pd.to_datetime(
                new_data["DATE VISITE"], format="%d/%m/%Y %H:%M", dayfirst=True
            ).dt.date

            new_data["MIS EN CIRCULATION"] = pd.to_datetime(
                new_data["MIS EN CIRCULATION"], format='mixed', dayfirst=True, errors='coerce'
            ).dt.date

            # Nettoyage des colonnes numériques
            cols_to_convert = ["FORCE_AV_G", "FORCE_AV_D", "FORCE_AR_G", "FORCE_AR_D", "POIDS", "EFFICACITE"]
            for col in cols_to_convert:
                new_data[col] = pd.to_numeric(new_data[col], errors="coerce")
            new_data[cols_to_convert] = new_data[cols_to_convert].astype("Int64")

            # Fonction de prédiction
            def predict_outlier(row):
                MARQUE = row.get('MARQUE')
                POIDS = row.get('POIDS')
                if pd.isnull(MARQUE) or pd.isnull(POIDS):
                    return 'Missing data'

                model_path = os.path.join(MODEL_DIR, f'isolation_forest_{MARQUE}.pkl')
                if os.path.exists(model_path):
                    try:
                        model = joblib.load(model_path)
                        pred = model.predict(pd.DataFrame({'Weight_Avg': [POIDS]}))[0]
                        return 'Outlier' if pred == -1 else 'Normal'
                    except Exception as e:
                        return f'Error: {str(e)}'
                else:
                    return 'Model not found'

            # Application de la prédiction
            new_data['status'] = new_data.apply(predict_outlier, axis=1)

            # Export des données
            new_data.to_csv(EXPORT_PATH, index=False)
            print(f"✅ Données transformées exportées vers {EXPORT_PATH}")

            with open(LOG_FILE, "w") as f:
                f.write(str(current_row_count))
        else:
            print("ℹ️ No new rows.")

if __name__ == "__main__":
    w = Watcher(CSV_PATH)
    w.run()
