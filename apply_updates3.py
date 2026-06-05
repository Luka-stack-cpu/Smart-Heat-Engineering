import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ---------------------------------------------------------------
# 1. Rebuild the services grid (it was emptied by regex)
# ---------------------------------------------------------------
services_grid = """      <div class="srv-card reveal">
        <div class="srv-icon">❄️</div>
        <h3>Тепловые насосы</h3>
        <p>Воздух-вода системы нового поколения. Работают до −25°C, экономят до 70% на отоплении. Считаем окупаемость ещё до монтажа.</p>
        <div class="srv-tags"><span class="tag">Воздух-вода</span><span class="tag">COP 4.5+</span><span class="tag">EVI</span></div>
        <a href="https://wa.me/996999699620?text=Здравствуйте!%20Меня%20интересуют%20тепловые%20насосы." class="srv-btn" target="_blank">💬 Обсудить в WhatsApp</a>
      </div>
      <div class="srv-card reveal reveal-delay-1">
        <div class="srv-icon">🌡️</div>
        <h3>Системы фанкойлов</h3>
        <p>Монтаж центральных систем кондиционирования с фанкойлами. Подходит для офисов, гостиниц, торговых площадей — там, где нужно зонировать климат.</p>
        <div class="srv-tags"><span class="tag">VRF</span><span class="tag">2-трубная</span><span class="tag">4-трубная</span></div>
        <a href="https://wa.me/996999699620?text=Здравствуйте!%20Меня%20интересуют%20системы%20фанкойлов." class="srv-btn" target="_blank">💬 Обсудить в WhatsApp</a>
      </div>
      <div class="srv-card reveal reveal-delay-2">
        <div class="srv-icon">♨️</div>
        <h3>Тёплые полы</h3>
        <p>Водяные тёплые полы — от стяжки до финального покрытия. Правильный пирог, укладка и подключение к тепловому насосу. 28$ / м² под ключ.</p>
        <div class="srv-tags"><span class="tag">Водяной</span><span class="tag">PE-RT X16</span><span class="tag">Под ключ</span></div>
        <a href="https://wa.me/996999699620?text=Здравствуйте!%20Меня%20интересует%20монтаж%20тёплого%20пола." class="srv-btn" target="_blank">💬 Обсудить в WhatsApp</a>
      </div>
      <div class="srv-card reveal reveal-delay-3">
        <div class="srv-icon">🔧</div>
        <h3>Радиаторы</h3>
        <p>Алюминиевые и биметаллические радиаторы. Работают с тепловыми насосами — вода тёплая, а не кипяток. Безопасно, экономично, долговечно.</p>
        <div class="srv-tags"><span class="tag">Алюминий</span><span class="tag">Биметалл</span><span class="tag">Монтаж</span></div>
        <a href="https://wa.me/996999699620?text=Здравствуйте!%20Меня%20интересуют%20радиаторы." class="srv-btn" target="_blank">💬 Обсудить в WhatsApp</a>
      </div>
      <div class="srv-card reveal">
        <div class="srv-icon">💧</div>
        <h3>Водонагреватели с тепловым насосом</h3>
        <p>Установка накопительных водонагревателей с тепловым насосом. Горячая вода круглый год с минимальным расходом электроэнергии.</p>
        <div class="srv-tags"><span class="tag">R290</span><span class="tag">R134A</span><span class="tag">Wi-Fi</span></div>
        <a href="https://wa.me/996999699620?text=Здравствуйте!%20Меня%20интересуют%20водонагреватели%20с%20тепловым%20насосом." class="srv-btn" target="_blank">💬 Обсудить в WhatsApp</a>
      </div>"""

html = html.replace(
    '    <div class="services-grid">\n      \n  </div>',
    '    <div class="services-grid">\n' + services_grid + '\n    </div>'
)

# ---------------------------------------------------------------
# 2. Fix warm floor materials list
# ---------------------------------------------------------------
# Find old warm floor description and update
html = html.replace(
    'Пеноплекс 3см, фольгоизол, монтажная сетка, труба PE-RT, коллектор, демпферная лента',
    'Пеноплекс 5см, фольгоизол, зонтики, монтажная пена, сетка, труба PE-RT X16 Valfex, коллектор, соединители, демпферная лента, шкаф коллекторный, хомуты'
)

# ---------------------------------------------------------------
# 3. Fix "до −30°C" remaining occurrences (any encoding)
# ---------------------------------------------------------------
html = html.replace('−30°C', '−25°C')
html = html.replace('-30°C', '−25°C')

# ---------------------------------------------------------------
# 4. Remove any remaining mentions of gas/boilers as direction
# ---------------------------------------------------------------
html = html.replace('Работаем с газом, электрикой, тепловыми насосами — подберём то, что выгоднее именно у вас.', 'Работаем с тепловыми насосами — экономично, надёжно, без зависимости от газа.')
html = html.replace('вода-вода, геотермальные системы', 'воздух-вода системы')
html = html.replace('Воздух-вода, вода-вода, геотермальные системы.', 'Воздух-вода системы нового поколения.')
html = html.replace('<span class="tag">Геотермаль</span>', '')

# ---------------------------------------------------------------
# 5. Remaining 1000+ fixes (in metadata)
# ---------------------------------------------------------------
html = html.replace('10 лет опыта, 1000+ объектов', '8 лет опыта, 300+ объектов')

# ---------------------------------------------------------------
# 6. Fix any remaining 2-3 days / 13 days
# ---------------------------------------------------------------
html = html.replace('2–3 рабочих дня', '1–3 дня')
html = html.replace('13 рабочих дней', '1–2 дня')

# ---------------------------------------------------------------
# 7. Footer link for Радиаторы
# ---------------------------------------------------------------
html = html.replace(
    '<a href="#catalog" onclick="showCat(\'boilers\')">Водонагреватели с тепловым насосом Sunrain</a>',
    '<a href="#catalog" onclick="showCat(\'boilers\')">Водонагреватели с тепловым насосом</a>\n      <a href="#catalog" onclick="showCat(\'radiators\')">Радиаторы</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done. Services rebuilt, warm floor, gas mentions, footer links updated.")
