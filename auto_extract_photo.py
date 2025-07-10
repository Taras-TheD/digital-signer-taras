from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import os

# 🗂 Пути к файлам
pdf_path = r"C:\Users\Admin\OneDrive\Documenti\CV\encrypted_cv_with_qr.pdf"
output_dir = r"C:\Users\Admin\OneDrive\Documenti\CV\CVs"
output_file = os.path.join(output_dir, "taras_photo_auto_extracted.png")
poppler_path = r"C:\Poppler\Release-24.07.0-0\poppler-24.07.0\Library\bin"

# 📄 Конвертация PDF → изображение
pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
img = pages[0].convert("RGB")
img_np = np.array(img)

# 📦 Получим размеры
height, width, _ = img_np.shape

# 🎯 Ограничим поиск правым верхним квадрантом
search_area = img_np[0:int(height * 0.5), int(width * 0.6):width]

# 🧠 Вычислим маску небелых пикселей
white_thresh = 240
non_white_mask = np.any(search_area < white_thresh, axis=2)

# 🧭 Найдём границы области фото
coords = np.argwhere(non_white_mask)
if coords.size == 0:
    raise ValueError("📭 Фото не найдено — верхняя правая область белая")

y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0) + 1

# ✂️ Вырезаем и сохраняем
crop_img = Image.fromarray(search_area[y0:y1, x0:x1])
os.makedirs(output_dir, exist_ok=True)
crop_img.save(output_file)

print(f"\n✅ Фото автоматически извлечено:\n{output_file}")
