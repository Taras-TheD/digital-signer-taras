from pdf2image import convert_from_path
from PIL import Image
import matplotlib.pyplot as plt

pdf_path = r"C:\Users\Admin\OneDrive\Documenti\CV\encrypted_cv_with_qr.pdf"
poppler_path = r"C:\Poppler\Release-24.07.0-0\poppler-24.07.0\Library\bin"

# 🖼 Конвертація першої сторінки
pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
img = pages[0].convert("RGB")

# 🧭 Вивід розміру
print(f"🔍 Розмір зображення (width, height): {img.size}")  # наприклад: (1654, 2339)

# 📸 Показ у вікні
plt.figure(figsize=(8,11))
plt.imshow(img)
plt.axis("on")  # показ осей для зручності
plt.title("Наведи курсор, щоб оцінити розташування фото")
plt.show()
