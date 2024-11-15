import pandas as pd
from deep_translator import GoogleTranslator
import os
from tqdm import tqdm

# Menentukan folder data dan results
data_folder = 'data'
results_folder = 'results'

# Membuat folder results jika belum ada
os.makedirs(results_folder, exist_ok=True)

# Tentukan path file
file_path = os.path.join(data_folder, 'other.csv')

# Load the file
data = pd.read_csv(file_path)

# Menambahkan animasi loading menggunakan tqdm
tqdm.pandas(desc="Menerjemahkan teks...")

# Translate 'en' column to Indonesian dengan progres bar
data['id'] = data['en'].progress_apply(lambda x: GoogleTranslator(source='en', target='id').translate(x) if pd.notna(x) else x)

# Tentukan path untuk hasil terjemahan
translated_file_path = os.path.join(results_folder, 'results.csv')

# Save the translated file
data.to_csv(translated_file_path, index=False)

print("Terjemahan selesai dan file disimpan di:", translated_file_path)
