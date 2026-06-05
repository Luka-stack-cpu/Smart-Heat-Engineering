import os
import re

files_to_update = ['index.html', 'faq.html', 'services.html', 'callback.html']

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Global replacements
    html = html.replace('1000+ объектов', '300+ объектов')
    html = html.replace('Гарантия 5 лет', 'Гарантия 2 года')
    html = html.replace('Гарантия и поддержка', 'Гарантия 2 года')
    html = html.replace('Гарантия и сервис', 'Гарантия 2 года')
    html = html.replace('до −30°C', 'до −25°C')
    html = html.replace('Бойлеры', 'Водонагреватели с тепловым насосом')
    html = html.replace('2–3 дня', '1–3 дня')
    html = html.replace('13 дней', '1–2 дня')

    # FAQ Specifics
    if 'faq.html' in file_path or 'index.html' in file_path:
        html = html.replace(
            'В Кыргызстане газ есть не везде. Если газа нет — насос однозначно выгоднее электрического котла. Если газ есть — считайте по тарифам, но насос ещё и охлаждает летом',
            'Мы с газом не работаем. Если газа нет или вы хотите независимости от подорожаний — насос однозначно выгоднее электрического котла. Плюс насос ещё и охлаждает летом, а котёл — нет'
        )
        html = html.replace(
            'Квартира с бойлером — 1 день. Дом 120 м² с тёплым полом — 1–3 дня. Большой коммерческий объект — до недели. Всё зависит от сложности',
            'Квартира с бойлером — 1 день. Дом 120 м² с тёплым полом — 1–3 дня. Коммерческий объект — 1–2 дня. Всё зависит от сложности'
        )
        # Also maybe 2-3 in the old FAQ
        html = html.replace(
            'Дом 120 м² с тёплым полом — 2–3 дня',
            'Дом 120 м² с тёплым полом — 1–3 дня'
        )

    # 3. Index.html specifics
    if file_path == 'index.html':
        # Services changes
        # Remove Gas/Koty
        html = re.sub(r'<div class="srv-card[^>]*>.*?Водяное отопление.*?</div>\s*</div>', '', html, flags=re.DOTALL)
        # Remove Water/Sewage
        html = re.sub(r'<div class="srv-card[^>]*>.*?Водопровод и канализация.*?</div>\s*</div>', '', html, flags=re.DOTALL)
        
        # Tags cleanup (VRV -> remove, keep VRF. Remove Ливнёвка, Фильтрация, Вода-вода, Балансировка, Котлы)
        html = html.replace('<span class="tag">VRF/VRV</span>', '<span class="tag">VRF</span>')
        html = html.replace('<span class="tag">Ливнёвка</span>', '')
        html = html.replace('<span class="tag">Вода-вода</span>', '')
        html = html.replace('<span class="tag">Балансировка</span>', '')
        
        # Update Radiator heating in services
        html = html.replace('<h3>Радиаторное отопление</h3>', '<h3>Радиаторы</h3>')
        
        # Remove about gas
        html = html.replace('Газовые котлы, электрика', '')
        html = html.replace('Газовые и электрические котлы', '')
        
        # Add Installment plan block
        installment_html = """
<section id="installment" style="background:var(--g1); padding:60px 20px;">
  <div style="max-width:800px; margin:0 auto; background:var(--g2); padding:40px; border-radius:16px; border:1px solid var(--border); display:flex; gap:30px; align-items:center; flex-wrap:wrap;">
    <div style="font-size:60px; line-height:1; color:var(--g4);">📅</div>
    <div style="flex:1; min-width:300px;">
      <h2 class="sec-title" style="margin-bottom:12px; font-size:28px;">Рассрочка без процентов</h2>
      <p class="sec-desc" style="margin:0; text-align:left;">Внутренняя рассрочка. Первоначальный взнос — 50%. Остальное — равными платежами. Без банков, без процентов, без переплат</p>
    </div>
  </div>
</section>
"""
        # Insert installment before CATALOG
        html = html.replace('<section id="catalog">', installment_html + '\n<section id="catalog">')

        # Add Radiators to catalog nav
        html = html.replace('<button class="cat-btn" onclick="showCat(\'boilers\')">Водонагреватели с тепловым насосом</button>', '<button class="cat-btn" onclick="showCat(\'boilers\')">Водонагреватели с тепловым насосом</button>\n      <button class="cat-btn" onclick="showCat(\'radiators\')">Радиаторы</button>')
        
        # Create Radiators block in catalog
        radiators_cat = """
    <!-- RADIATORS -->
    <div class="cat-section" id="cat-radiators" style="display:none;">
      <div class="prod-grid">
        <div class="prod-card reveal">
          <div class="prod-img-wrap">
            <div style="width:100%; height:200px; background:#2a2a2a; display:flex; align-items:center; justify-content:center; color:#555; border-radius:8px;">Фото в разработке</div>
            <div class="prod-badge">Алюминий/Биметалл</div>
          </div>
          <div class="prod-info">
            <h3>Радиаторы для тепловых насосов</h3>
            <p>Алюминиевые и биметаллические радиаторы для системы отопления. Работают с тепловыми насосами — вода в них тёплая, а не кипяток. Безопасно, экономично, долговечно.</p>
            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите модель:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"Радиатор 500/80", "p":"$45", "s":"150 Вт/секция", "d":"500×80", "a":"500/80"}'>Радиатор 500/80</option>
                  <option style="color:#000" value='{"m":"Радиатор 500/100", "p":"$55", "s":"180 Вт/секция", "d":"500×100", "a":"500/100"}'>Радиатор 500/100</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Мощность:</span><strong class="d-pwr" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
"""
        html = html.replace('<!-- BOILERS -->', radiators_cat + '\n    <!-- BOILERS -->')

        # Replace SVGs with IMGs
        def replace_img(match, img_name):
            return f'<img src="img/{img_name}" class="prod-img" alt="{img_name}">'

        # 1. R32 Monoblock
        html = re.sub(r'<svg viewBox="0 0 300 200".*?ECO R32</text>\s*</svg>', '<img src="img/моноблоч инв тепл насос.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 2. R290 Commercial
        html = re.sub(r'<svg viewBox="0 0 300 200".*?R290</text>\s*</svg>', '<img src="img/коммер полн теп нас.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 3. R410A Commercial
        html = re.sub(r'<svg viewBox="0 0 300 200".*?R410A</text>\s*</svg>', '<img src="img/моноблоч коммерческий.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 4. R32 A+++
        html = re.sub(r'<svg viewBox="0 0 300 200".*?A\+\+\+</text>\s*</svg>', '<img src="img/моноблоч инв тепл насос.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 5. Fancoil Wall
        html = re.sub(r'<svg viewBox="0 0 300 200".*?НАСТЕННЫЙ ФАНКОЙЛ</text>\s*</svg>', '<img src="img/настенный фанкоил.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 6. Fancoil Floor
        html = re.sub(r'<svg viewBox="0 0 300 200".*?СТОЯЧИЙ ФАНКОЙЛ</text>\s*</svg>', '<img src="img/напольный фанкоил.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 7. Fancoil Cassette
        html = re.sub(r'<svg viewBox="0 0 300 200".*?КАССЕТНЫЙ ФАНКОЙЛ</text>\s*</svg>', '<img src="img/кассетный фанкоил.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 8. Warm floor
        html = re.sub(r'<svg viewBox="0 0 300 200".*?СИСТЕМА ТЁПЛЫЙ ПОЛ</text>\s*</svg>', '<img src="img/теплые полы.png" class="prod-img">', html, flags=re.DOTALL)
        
        # 9. Boilers
        html = re.sub(r'<svg viewBox="0 0 300 200".*?HEAT PUMP</text>.*?A\+</text>\s*</svg>', '<img src="img/большой.png" class="prod-img">', html, flags=re.DOTALL)
        html = re.sub(r'<svg viewBox="0 0 300 200".*?sunrain</text>.*?BOILER</text>.*?</svg>', '<img src="img/настенный водонаг.png" class="prod-img">', html, flags=re.DOTALL)
        
        # Insert CSS for prod-img
        html = html.replace('</style>', '  .prod-img { width: 100%; height: 200px; object-fit: contain; padding: 20px; }\n</style>')

        # Update Warm Floor price and items
        html = html.replace('21$ / м²', '28$ / м²')
        html = html.replace('21$', '28$')

        # Add boiler arrays - user wanted 2 vertical boilers (R290 and R134A) and 1 wall boiler
        # Current HTML has 2 boilers. I'll replace the first boiler card with R290, add another for R134A, and third is Wall.
        
        # R290 Vertical Boilers
        boiler_r290 = """<div class="prod-card reveal">
          <div class="prod-img-wrap">
            <img src="img/большой.png" class="prod-img">
            <div class="prod-badge eco">R290 Wi-Fi</div>
          </div>
          <div class="prod-info">
            <h3>Вертикальный водонагреватель с тепловым насосом R290</h3>
            <p>Хладагент R290, микроканальный теплообменник, ППУ 50мм, Wi-Fi управление, температура до 75°C.</p>
            <div class="prod-specs">
              <span>🌡️ до 75°C</span>
              <span>📶 Wi-Fi</span>
              <span>⚡ 220В/50Гц</span>
            </div>
            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите объем:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"YT-100TA1", "p":"$1 475", "d":"Ø620×1200", "a":"100 л"}'>Объем 100 л</option>
                  <option style="color:#000" value='{"m":"YT-200TA1", "p":"$1 850", "d":"Ø620×1672", "a":"200 л"}'>Объем 200 л</option>
                  <option style="color:#000" value='{"m":"YT-300TA1", "p":"$2 090", "d":"Ø620×1937", "a":"300 л"}'>Объем 300 л</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>
          </div>
        </div>"""
        
        boiler_r134a = """<div class="prod-card reveal">
          <div class="prod-img-wrap">
            <img src="img/вертикальныйц водонаг с тп r134a.png" class="prod-img">
            <div class="prod-badge eco">R134A Wi-Fi</div>
          </div>
          <div class="prod-info">
            <h3>Вертикальный водонагреватель с тепловым насосом R134A</h3>
            <p>Хладагент R134A, микроканальный теплообменник, ППУ 40мм, Wi-Fi, EVI до −25°C, до 75°C.</p>
            <div class="prod-specs">
              <span>🌡️ до 75°C</span>
              <span>📶 Wi-Fi</span>
              <span>❄️ EVI до −25°C</span>
            </div>
            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите объем:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"YT-200TB1", "p":"$2 020", "d":"Ø620×1672", "a":"200 л"}'>Объем 200 л</option>
                  <option style="color:#000" value='{"m":"YT-300TB1", "p":"$2 280", "d":"Ø620×1937", "a":"300 л"}'>Объем 300 л</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>
          </div>
        </div>"""
        
        # Replace the first vertical boiler with both R290 and R134A vertical boilers
        html = re.sub(r'<!-- Vertical boiler -->.*?<!-- Wall boiler -->', '<!-- Vertical boiler R290 -->\n' + boiler_r290 + '\n<!-- Vertical boiler R134A -->\n' + boiler_r134a + '\n<!-- Wall boiler -->', html, flags=re.DOTALL)
        
        # Modify the wall boiler to R134A wall boiler
        html = html.replace('YT-080GV/GH', 'YT-080GV/GH')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated all files.")
