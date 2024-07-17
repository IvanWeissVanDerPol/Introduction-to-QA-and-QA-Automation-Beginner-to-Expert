import os

# Ruta base de tu proyecto
base_path = "C:\\Users\\WEISSIVA\\Documents\\FPUNA\\Introduction-to-QA-and-QA-Automation-Beginner-to-Expert\\Introduccion_QA_Automatizacion"

# Archivo de salida
output_dir = "C:\\Users\\WEISSIVA\\Documents\\FPUNA\\Introduction-to-QA-and-QA-Automation-Beginner-to-Expert\\UTILS"
output_file = os.path.join(output_dir, "version_completa.md")

# Eliminar archivo mergeado anterior si existe
if os.path.exists(output_file):
    os.remove(output_file)

# Lista de subcarpetas para incluir en el merge (descomentar las que quieras incluir)
subfolders_to_include = [
    "01_Introduccion_QA",
    "02_Fundamentos_Python",
    "03_Pruebas_Automatizadas",
    "04_APIs_RESTful",
    "05_Selenium_Basico"
]

# Función para leer y escribir contenido de los archivos markdown
def merge_markdown_files(base_path, output_file, subfolders):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for subfolder in subfolders:
            subfolder_path = os.path.join(base_path, subfolder)
            if os.path.exists(subfolder_path):
                for root, dirs, files in os.walk(subfolder_path):
                    for file in files:
                        if file.endswith(".md"):
                            file_path = os.path.join(root, file)
                            relative_path = os.path.relpath(file_path, base_path)
                            outfile.write(f"\n## {relative_path}\n\n")
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                outfile.write(infile.read())
                                outfile.write("\n")

# Ejecutar la función
merge_markdown_files(base_path, output_file, subfolders_to_include)
