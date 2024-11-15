import pandas as pd
from googletrans import Translator

# Load the file
file_path = 'theme.csv'
data = pd.read_csv(file_path)

# Initialize translator
translator = Translator()

# Translate 'en' column to Indonesian
data['id'] = data['en'].apply(lambda x: translator.translate(x, src='en', dest='id').text if pd.notna(x) else x)

# Save the translated file
translated_file_path = 'results.csv'
data.to_csv(translated_file_path, index=False)
