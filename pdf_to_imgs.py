import fitz
doc = fitz.open("/Users/edvard/Desktop/КП Smart Heat Engineering 1.pdf")
# We just want the whole assortment. 
# Pages are 0-indexed. Let's render all pages to PNGs
for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=150)
    pix.save(f"page_{i+1}.png")
print("Saved pages as PNGs")
