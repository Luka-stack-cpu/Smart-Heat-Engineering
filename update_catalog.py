import re
import json

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Nav links
html = html.replace('href="#services"', 'href="services.html"')
html = html.replace('href="#faq"', 'href="faq.html"')
html = html.replace('href="#contact" class="nav-cta"', 'href="callback.html" class="nav-cta"')
html = html.replace('href="#contact"', 'href="callback.html"') # Some other contact links

# Revert specific internal anchor links if any
# Actually, the user might want to keep the contact section at the bottom.
# So I should only change the specific nav links:
html = html.replace('onclick="toggleMenu()">Услуги', 'onclick="toggleMenu()">Услуги') # already handled by href replace
html = html.replace('href="services.html" onclick="toggleMenu()"', 'href="services.html"')
html = html.replace('href="faq.html" onclick="toggleMenu()"', 'href="faq.html"')

# We will inject the catalog logic now.
# Replace R32 Monoblock (A++)
target_r32_app = """            <div class="prod-models">
              <div class="prod-model-row"><span>БЛН 009TA1 (до 100м²)</span><strong>2 438$</strong></div>
              <div class="prod-model-row"><span>БЛН 012TA1 (до 120м²)</span><strong>2 553$</strong></div>
              <div class="prod-model-row"><span>БЛН 012TA3 (до 120м², III ф.)</span><strong>2 852$</strong></div>
              <div class="prod-model-row"><span>БЛН 015TA1 (до 160м²)</span><strong>3 864$</strong></div>
              <div class="prod-model-row"><span>БЛН 015TA3 (до 160м², III ф.)</span><strong>3 990$</strong></div>
              <div class="prod-model-row"><span>БЛН 018TA1 (до 200м²)</span><strong>4 370$</strong></div>
              <div class="prod-model-row"><span>БЛН 018TA3 (до 200м², III ф.)</span><strong>4 508$</strong></div>
              <div class="prod-model-row"><span>БЛН 026TA3 (до 280м², III ф.)</span><strong>5 370$</strong></div>
              <div class="prod-model-row"><span>БЛН 032TA3 (до 360м², III ф.)</span><strong>6 500$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20тепловой%20насос%20R32.%20Хочу%20узнать%20подробности." class="prod-btn" target="_blank">Узнать цену</a>"""

rep_r32_app = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь дома:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"БЛН 009ТА1", "p":"$2 438", "s":"3.4–10.2 кВт", "d":"1005×375×800", "a":"100 м²"}'>Площадь 100 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 012ТА1", "p":"$2 553", "s":"4.6–12.8 кВт", "d":"1005×375×800", "a":"120 м²"}'>Площадь 120 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 015ТА1", "p":"$3 864", "s":"5.2–16.8 кВт", "d":"1025×380×1320", "a":"160 м²"}'>Площадь 160 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТА1", "p":"$4 370", "s":"6.8–20.5 кВт", "d":"1077×377×1460", "a":"200 м²"}'>Площадь 200 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 026ТА3", "p":"$5 370", "s":"11.8–28.6 кВт", "d":"1127×427×1560", "a":"280 м²"}'>Площадь 280 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 032ТА3", "p":"$6 500", "s":"14.5–36.3 кВт", "d":"1127×427×1560", "a":"360 м²"}'>Площадь 360 м²</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Мощность:</span><strong class="d-pwr" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_r32_app, rep_r32_app)

# R32 A+++
target_r32_appp = """            <div class="prod-models">
              <div class="prod-model-row"><span>БЛН 006ТБ1 (до 80м²)</span><strong>3 703$</strong></div>
              <div class="prod-model-row"><span>БЛН 010ТБ1 (до 120м²)</span><strong>3 850$</strong></div>
              <div class="prod-model-row"><span>БЛН 010ТБ3 (до 120м², III ф.)</span><strong>4 013$</strong></div>
              <div class="prod-model-row"><span>БЛН 014ТБ1 (до 165м²)</span><strong>4 508$</strong></div>
              <div class="prod-model-row"><span>БЛН 014ТБ3 (до 165м², III ф.)</span><strong>4 669$</strong></div>
              <div class="prod-model-row"><span>БЛН 018ТБ1 (до 200м²)</span><strong>5 531$</strong></div>
              <div class="prod-model-row"><span>БЛН 018ТБ3 (до 200м², III ф.)</span><strong>5 669$</strong></div>
              <div class="prod-model-row"><span>БЛН 024ТБ3 (до 260м², III ф.)</span><strong>6 095$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20тепловой%20насос%20A%2B%2B%2B%20R32." class="prod-btn" target="_blank">Узнать цену</a>"""

rep_r32_appp = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь дома:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"БЛН 006ТБ1", "p":"$3 703", "s":"2.50–8.30 кВт", "d":"1100×445×850", "a":"80 м²"}'>Площадь 80 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 010ТБ1", "p":"$3 850", "s":"4.20–12.2 кВт", "d":"1100×445×850", "a":"120 м²"}'>Площадь 120 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 014ТБ1", "p":"$4 508", "s":"5.30–16.5 кВт", "d":"1100×480×850", "a":"165 м²"}'>Площадь 165 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТБ1", "p":"$5 531", "s":"6.20–20.5 кВт", "d":"1110×445×1450", "a":"200 м²"}'>Площадь 200 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 024ТБ3", "p":"$6 095", "s":"6.50–26.1 кВт", "d":"1110×445×1450", "a":"260 м²"}'>Площадь 260 м²</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Мощность:</span><strong class="d-pwr" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_r32_appp, rep_r32_appp)

# R410A Commercial
target_r410a = """            <div class="prod-models">
              <div class="prod-model-row"><span>DNL-050TA1 (до 450м²)</span><strong>9 810$</strong></div>
              <div class="prod-model-row"><span>DLN-100TA1 (до 900м²)</span><strong>17 710$</strong></div>
              <div class="prod-model-row"><span>DLN-200TA1 (до 1800м²)</span><strong>27 830$</strong></div>
              <div class="prod-model-row"><span>DLN-400TA1 (до 3500м²)</span><strong>50 600$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20коммерческий%20тепловой%20насос%20R410A." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_r410a = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"DNL-050ТА1", "p":"$9 810", "s":"45 кВт", "d":"1252×1076×1870", "a":"450 м²"}'>Площадь 450 м²</option>
                  <option style="color:#000" value='{"m":"DNL-100ТА1", "p":"$17 710", "s":"90 кВт", "d":"2198×1096×2176", "a":"900 м²"}'>Площадь 900 м²</option>
                  <option style="color:#000" value='{"m":"DNL-200ТА1", "p":"$27 830", "s":"180 кВт", "d":"2330×1150×2400", "a":"1800 м²"}'>Площадь 1800 м²</option>
                  <option style="color:#000" value='{"m":"DNL-400ТА1", "p":"$50 600", "s":"350 кВт", "d":"2800×2200×2450", "a":"3500 м²"}'>Площадь 3500 м²</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Мощность:</span><strong class="d-pwr" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_r410a, rep_r410a)

# R290 Commercial
target_r290 = """            <div class="prod-models">
              <div class="prod-model-row"><span>BNL-050TC3 — III фазы</span><strong>13 486$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20коммерческий%20насос%20R290%20BNL-050TC3." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_r290 = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"BNL-050ТС3", "p":"$13 486", "s":"17.56–50 кВт", "d":"1155×990×1880", "a":"500 м²"}'>Площадь 500 м²</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Мощность:</span><strong class="d-pwr" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_r290, rep_r290)

# Fancoils
target_fc_wall = """            <div class="prod-models">
              <div class="prod-model-row"><span>ФП 68БГ — 3500/5250 Вт</span><strong>320$</strong></div>
              <div class="prod-model-row"><span>ФП 85БГ — 4500/6750 Вт</span><strong>480$</strong></div>
              <div class="prod-model-row"><span>ФП 102БГ — 5400/8100 Вт</span><strong>540$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20настенный%20фанкойл." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_fc_wall = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь/мощность:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"ФП 68БГ", "p":"$320", "s":"3500 Вт", "d":"1025×335×260", "a":"35 м²"}'>35 м² / 3500 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 85БГ", "p":"$480", "s":"4500 Вт", "d":"1135×370×260", "a":"45 м²"}'>45 м² / 4500 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 102БГ", "p":"$540", "s":"5400 Вт", "d":"1220×360×260", "a":"54 м²"}'>54 м² / 5400 Вт</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_fc_wall, rep_fc_wall)

target_fc_floor = """            <div class="prod-models">
              <div class="prod-model-row"><span>ФП 136Л3 — 7400/11100 Вт</span><strong>580$</strong></div>
              <div class="prod-model-row"><span>ФП 170Л3 — 8500/12750 Вт</span><strong>680$</strong></div>
              <div class="prod-model-row"><span>ФП 204Л3 — 10000/15000 Вт</span><strong>750$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20напольный%20фанкойл." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_fc_floor = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь/мощность:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"ФП 136Л3", "p":"$580", "s":"7400 Вт", "d":"485×290×1680", "a":"74 м²"}'>74 м² / 7400 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 170Л3", "p":"$680", "s":"8500 Вт", "d":"520×285×1755", "a":"85 м²"}'>85 м² / 8500 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 204Л3", "p":"$750", "s":"10000 Вт", "d":"600×310×1900", "a":"100 м²"}'>100 м² / 10000 Вт</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_fc_floor, rep_fc_floor)

target_fc_cassette = """            <div class="prod-models">
              <div class="prod-model-row"><span>ФП 34КМ (1980/2980 Вт)</span><strong>570$</strong></div>
              <div class="prod-model-row"><span>ФП 51КМ (2980/4800 Вт)</span><strong>590$</strong></div>
              <div class="prod-model-row"><span>ФП 68КМ (3680/5480 Вт)</span><strong>600$</strong></div>
              <div class="prod-model-row"><span>ФП 85КМ (4980/7200 Вт)</span><strong>710$</strong></div>
              <div class="prod-model-row"><span>ФП 102КМ (5580/8180 Вт)</span><strong>720$</strong></div>
              <div class="prod-model-row"><span>ФП 136КМ (7080/10600 Вт)</span><strong>730$</strong></div>
              <div class="prod-model-row"><span>ФП 170КМ (9900/14500 Вт)</span><strong>820$</strong></div>
              <div class="prod-model-row"><span>ФП 204КМ (10400/15200 Вт)</span><strong>850$</strong></div>
              <div class="prod-model-row"><span>ФП 238КМ (11800/18000 Вт)</span><strong>890$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20кассетный%20фанкойл." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_fc_cassette = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите площадь/мощность:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"ФП 34КМ", "p":"$570", "d":"650×650×290", "a":"20 м²"}'>20 м² / 1980 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 51КМ", "p":"$590", "d":"650×650×290", "a":"30 м²"}'>30 м² / 2980 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 68КМ", "p":"$600", "d":"650×650×290", "a":"37 м²"}'>37 м² / 3680 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 85КМ", "p":"$710", "d":"800×800×290", "a":"50 м²"}'>50 м² / 4980 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 102КМ", "p":"$720", "d":"800×800×290", "a":"56 м²"}'>56 м² / 5580 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 136КМ", "p":"$730", "d":"800×800×290", "a":"71 м²"}'>71 м² / 7080 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 170КМ", "p":"$820", "d":"950×950×290", "a":"99 м²"}'>99 м² / 9900 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 204КМ", "p":"$850", "d":"950×950×290", "a":"104 м²"}'>104 м² / 10400 Вт</option>
                  <option style="color:#000" value='{"m":"ФП 238КМ", "p":"$890", "d":"950×950×290", "a":"118 м²"}'>118 м² / 11800 Вт</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_fc_cassette, rep_fc_cassette)

# Boilers
target_boiler_v = """            <div class="prod-models">
              <div class="prod-model-row"><span>YT-200TB1 — 200 л</span><strong>2 020$</strong></div>
              <div class="prod-model-row"><span>YT-250TB1 — 250 л</span><strong>2 170$</strong></div>
              <div class="prod-model-row"><span>YT-300TB1 — 300 л</span><strong>2 280$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20вертикальный%20бойлер%20с%20тепловым%20насосом%20R134A." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_boiler_v = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите объем:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"YT-200ТВ1", "p":"$2 020", "d":"Ø620×1672", "a":"200 л"}'>Объем 200 л</option>
                  <option style="color:#000" value='{"m":"YT-250ТВ1", "p":"$2 170", "d":"Ø620×1790", "a":"250 л"}'>Объем 250 л</option>
                  <option style="color:#000" value='{"m":"YT-300ТВ1", "p":"$2 280", "d":"Ø620×1937", "a":"300 л"}'>Объем 300 л</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_boiler_v, rep_boiler_v)

target_boiler_h = """            <div class="prod-models">
              <div class="prod-model-row"><span>YT-060GV/GH — 60 л</span><strong>940$</strong></div>
              <div class="prod-model-row"><span>YT-080GV/GH — 80 л</span><strong>1 000$</strong></div>
              <div class="prod-model-row"><span>YT-100GV/GH — 100 л</span><strong>1 100$</strong></div>
            </div>
            <a href="https://wa.me/996999699620?text=Здравствуйте!%20Интересует%20настенный%20бойлер%20с%20тепловым%20насосом." class="prod-btn" target="_blank">Узнать цену</a>"""
rep_boiler_h = """            <div class="prod-models">
              <div class="form-group" style="margin-bottom:12px;">
                <label style="font-size:13px;color:var(--muted);display:block;margin-bottom:6px;">Выберите объем:</label>
                <select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"YT-060GV/GH", "p":"$940", "d":"Ø470×977", "a":"60 л"}'>Объем 60 л</option>
                  <option style="color:#000" value='{"m":"YT-080GV/GH", "p":"$1 000", "d":"Ø470×1142", "a":"80 л"}'>Объем 80 л</option>
                  <option style="color:#000" value='{"m":"YT-100GV/GH", "p":"$1 100", "d":"Ø470×1282", "a":"100 л"}'>Объем 100 л</option>
                </select>
              </div>
              <div class="prod-dyn-info" style="display:none;background:rgba(39,168,95,0.05);padding:14px;border-radius:8px;border:1px solid var(--border2);animation:fadeIn 0.3s forwards;">
                <div class="prod-model-row"><span style="color:var(--white);">Модель:</span><strong class="d-mod" style="color:var(--g4);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Размеры:</span><strong class="d-dim" style="color:var(--white);"></strong></div>
                <div class="prod-model-row"><span style="color:var(--white);">Цена:</span><strong class="d-prc" style="color:var(--g5);font-size:18px;"></strong></div>
              </div>
            </div>
            <a href="#" class="prod-btn d-btn" target="_blank" style="display:none;">Написать в WhatsApp</a>"""
html = html.replace(target_boiler_h, rep_boiler_h)

# JS logic
js_logic = """
  <script>
    function updateProd(select) {
      const data = JSON.parse(select.value);
      const card = select.closest('.prod-card');
      const info = card.querySelector('.prod-dyn-info');
      const btn = card.querySelector('.d-btn');
      
      info.style.display = 'block';
      btn.style.display = 'flex';
      
      if (card.querySelector('.d-mod')) card.querySelector('.d-mod').textContent = data.m;
      if (card.querySelector('.d-pwr') && data.s) card.querySelector('.d-pwr').textContent = data.s;
      if (card.querySelector('.d-dim')) card.querySelector('.d-dim').textContent = data.d;
      if (card.querySelector('.d-prc')) card.querySelector('.d-prc').textContent = data.p;
      
      const msg = encodeURIComponent(`Здравствуйте! Интересует ${data.m} на ${data.a}. Хочу узнать подробнее`);
      btn.href = `https://wa.me/996999699620?text=${msg}`;
    }
    
    // trigger on load
    document.querySelectorAll('.area-select').forEach(sel => updateProd(sel));
  </script>
</body>
"""

html = html.replace('</body>', js_logic)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
