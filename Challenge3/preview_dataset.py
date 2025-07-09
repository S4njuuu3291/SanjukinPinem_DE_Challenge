import json
import random
import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

folder_gambar = 'Labeled_Dataset\\'
file_coco = 'Labeled_Dataset\\_annotations.coco.json'

with open(file_coco, 'r') as f:
    coco = json.load(f)

images = coco['images']
img_info = random.choice(images)
img_id = img_info['id']
img_file = img_info['file_name']

annotations = [ann for ann in coco['annotations'] if ann['image_id'] == img_id]
cat_id_to_name = {cat['id']: cat['name'] for cat in coco['categories']}

random.seed(42)
cat_colors = {}
for cat_id in cat_id_to_name.keys():
    cat_colors[cat_id] = tuple(random.choices(range(50, 256), k=3))

img_path = os.path.join(folder_gambar, img_file)
img = Image.open(img_path).convert('RGB')
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()

for ann in annotations:
    x, y, w, h = ann['bbox']
    category = cat_id_to_name[ann['category_id']]
    color = cat_colors[ann['category_id']]

    draw.rectangle([x, y, x + w, y + h], outline=color, width=4)
    bbox = font.getbbox(category)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = x
    text_y = max(0, y - text_height - 2) 
    rect_bg = (text_x, text_y, text_x + text_width, text_y + text_height)
    draw.rectangle(rect_bg, fill=color)
    draw.text((text_x+1, text_y+1), category, font=font, fill="black")
    draw.text((text_x, text_y), category, font=font, fill="white")

plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.title(f"Gambar: {img_file} - {len(annotations)} bbox")
plt.axis('off')
plt.show()