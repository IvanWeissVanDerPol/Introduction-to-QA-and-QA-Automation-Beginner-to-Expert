import json
import os

# Ruta al archivo JSON en el directorio UTILS
json_path = 'C:/Users/WEISSIVA/Documents/FPUNA/Introduction-to-QA-and-QA-Automation-Beginner-to-Expert/UTILS/sugerencias.json'

# Leer el archivo JSON
with open(json_path, 'r', encoding='utf-8') as f:
    sugerencias = json.load(f)

# Base path to prepend to each file path
base_path = "C:/Users/WEISSIVA/Documents/FPUNA/Introduction-to-QA-and-QA-Automation-Beginner-to-Expert"

# Función para agregar contenido a un archivo
def agregar_contenido(file_path, contenido):
    with open(file_path, 'a', encoding='utf-8') as f:
        for item in contenido:
            if isinstance(item, dict):
                f.write(item['section'] + '\n')
                if isinstance(item['content'], list):
                    for sub_item in item['content']:
                        if 'sub_section' in sub_item:
                            f.write(sub_item['sub_section'] + '\n')
                            f.write(sub_item['content'] + '\n')
                        else:
                            f.write(sub_item['content'] + '\n')
                else:
                    f.write(item['content'] + '\n')
            else:
                f.write(item + '\n')
        f.write('\n')

# Iterar sobre los elementos del JSON y actualizar los archivos
for entry in sugerencias:
    file_path = entry["file_path"]
    content_to_add = entry["content_to_add"]
    
    # Construir la ruta completa del archivo
    full_path = os.path.join(base_path, file_path)
    
    # Agregar contenido al archivo
    agregar_contenido(full_path, content_to_add)

print("Archivos actualizados con sugerencias.")
