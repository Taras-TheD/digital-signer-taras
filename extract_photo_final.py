from pdf2image import convert_from_path
from PIL import Image
import os

# 📂 Пути
pdf_path = r"C:\Users\Admin\OneDrive\Documenti\CV\encrypted_cv_with_qr.pdf"
output_dir = r"C:\Users\Admin\OneDrive\Documenti\CV\CVs"
output_file = os.path.join(output_dir, "taras_photo_extracted.png")
poppler_path = r"C:\Poppler\Release-24.07.0-0\poppler-24.07.0\Library\bin"

# 🖼 Конвертация PDF в изображение
pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
img = pages[0].convert("RGB")

# 📏 Корректные координаты области фото
left = 105
top = 1966
right = 628
bottom = 2382

# ✂️ Вырезаем фрагмент
cropped = img.crop((left, top, right, bottom))

# 💾 Сохраняем PNG
os.makedirs(output_dir, exist_ok=True)
cropped.save(output_file)

print(f"\n✅ Фото успешно извлечено:\n{output_file}")
