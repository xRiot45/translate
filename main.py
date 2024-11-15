import pandas as pd
from googletrans import Translator
import os
from tqdm import tqdm

# Menentukan folder data dan results
data_folder = 'data'
results_folder = 'results'

# Membuat folder results jika belum ada
os.makedirs(results_folder, exist_ok=True)

# Tentukan path file yang akan di terjemahkan
file_path = os.path.join(data_folder, 'theme.csv')

# Load the file
data = pd.read_csv(file_path)

# Initialize translator
translator = Translator()

# Menambahkan animasi loading menggunakan tqdm
tqdm.pandas(desc="Translate text...")

# Translate 'en' column to Indonesian dengan progres bar
data['id'] = data['en'].progress_apply(lambda x: translator.translate(x, src='en', dest='id').text if pd.notna(x) else x)

# Tentukan path untuk hasil terjemahan dan nama file hasil terjemahan
translated_file_path = os.path.join(results_folder, 'results.csv')

# Save the translated file
data.to_csv(translated_file_path, index=False)

print("The translation is complete and the file is saved in:", translated_file_path)
