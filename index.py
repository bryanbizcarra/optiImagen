import os
from PIL import Image

# Directorios
input_folder = 'Imagenes para comprimir'
output_folder = 'Imagenes comprimidas'
output_list_file = 'imagenes_comprimidas.txt'

# Crear carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Extensiones de imagen válidas
image_extensions = ('.jpg', '.jpeg', '.png', '.webp')

# Calidad WebP
webp_quality = 80

# Lista para guardar los nombres de imágenes comprimidas
comprimidas = []

# Procesar imágenes
for filename in os.listdir(input_folder):
    if filename.lower().endswith(image_extensions):
        input_path = os.path.join(input_folder, filename)

        # Normalizar nombre
        name_without_ext = os.path.splitext(filename)[0]
        normalized_name = name_without_ext.lower().replace(" ", "_")
        output_filename = normalized_name + '.webp'
        output_path = os.path.join(output_folder, output_filename)

        # Evitar duplicados
        if os.path.exists(output_path):
            print(f"🔁 Ya existe: {output_filename} — se omite.")
            continue

        try:
            img = Image.open(input_path)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.save(output_path, 'WEBP', quality=webp_quality, optimize=True)
            comprimidas.append(output_filename)
            print(f"✅ {filename} → {output_filename}")
        except Exception as e:
            print(f"❌ Error al procesar {filename}: {e}")

# Guardar nombres en archivo .txt
with open(output_list_file, 'w', encoding='utf-8') as f:
    for nombre in comprimidas:
        f.write(nombre + '\n')

print(f"\n📝 Lista de imágenes guardada en: {output_list_file}")
print("🚀 Proceso completo.")
