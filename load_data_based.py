from time import sleep
from progress.spinner import MoonSpinner
import requests

loaded_data = None  # Declare loaded_data in the global scope


def bar_chargement():
    with MoonSpinner('Processing…') as bar:
        while True:
            sleep(0.03)
            bar.next()
            global loaded_data  # Use the global keyword to modify the global variable
            loaded_data = load_ygo_db()
            if loaded_data is not None:
                break



