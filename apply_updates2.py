import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# R290 Commercial models update
old_r290 = """<select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"BNL-050ТС3", "p":"$13 486", "s":"17.56–50 кВт", "d":"1155×990×1880", "a":"500 м²"}'>Площадь 500 м²</option>
                </select>"""

new_r290 = """<select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"BNL-050ТС3", "p":"$13 486", "s":"17.56–50 кВт", "d":"1155×990×1880", "a":"500 м²"}'>Площадь 500 м² (BNL-050TC3)</option>
                  <option style="color:#000" value='{"m":"BNL-080ТС3", "p":"$19 430", "s":"до 80 кВт", "d":"-", "a":"800 м²"}'>Площадь 800 м² (BNL-080TC3)</option>
                </select>"""

html = html.replace(old_r290, new_r290)

# Replace all wa.me buttons text
# wa.me/XXXXXXXXXX -> wa.me/996999699620
html = re.sub(r'https?://wa\.me/\d+\??', 'https://wa.me/996999699620?', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated R290 and WA links.")
