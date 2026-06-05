import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# R32 A++
old_r32_app = """<select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"БЛН 009ТА1", "p":"$2 438", "s":"3.4–10.2 кВт", "d":"1005×375×800", "a":"100 м²"}'>Площадь 100 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 012ТА1", "p":"$2 553", "s":"4.6–12.8 кВт", "d":"1005×375×800", "a":"120 м²"}'>Площадь 120 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 015ТА1", "p":"$3 864", "s":"5.2–16.8 кВт", "d":"1025×380×1320", "a":"160 м²"}'>Площадь 160 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТА1", "p":"$4 370", "s":"6.8–20.5 кВт", "d":"1077×377×1460", "a":"200 м²"}'>Площадь 200 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 026ТА3", "p":"$5 370", "s":"11.8–28.6 кВт", "d":"1127×427×1560", "a":"280 м²"}'>Площадь 280 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 032ТА3", "p":"$6 500", "s":"14.5–36.3 кВт", "d":"1127×427×1560", "a":"360 м²"}'>Площадь 360 м²</option>
                </select>"""

new_r32_app = """<select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"БЛН 009ТА1", "p":"$2 438", "s":"3.4–10.2 кВт", "d":"1005×375×800", "a":"100 м²"}'>100 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 012ТА1", "p":"$2 553", "s":"4.6–12.8 кВт", "d":"1005×375×800", "a":"120 м²"}'>120 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 012ТА3", "p":"$2 852", "s":"4.6–12.8 кВт", "d":"1005×375×800", "a":"120 м²"}'>120 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 015ТА1", "p":"$3 864", "s":"5.2–16.8 кВт", "d":"1025×380×1320", "a":"160 м²"}'>160 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 015ТА3", "p":"$3 990", "s":"5.2–16.8 кВт", "d":"1025×380×1320", "a":"160 м²"}'>160 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТА1", "p":"$4 370", "s":"6.8–20.5 кВт", "d":"1077×377×1460", "a":"200 м²"}'>200 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТА3", "p":"$4 508", "s":"6.8–20.5 кВт", "d":"1077×377×1460", "a":"200 м²"}'>200 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 026ТА3", "p":"$5 370", "s":"11.8–28.6 кВт", "d":"1127×427×1560", "a":"280 м²"}'>280 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 032ТА3", "p":"$6 500", "s":"14.5–36.3 кВт", "d":"1127×427×1560", "a":"360 м²"}'>360 м² (III фазы)</option>
                </select>"""

html = html.replace(old_r32_app, new_r32_app)


# R32 A+++
old_r32_appp = """<select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"БЛН 006ТБ1", "p":"$3 703", "s":"2.50–8.30 кВт", "d":"1100×445×850", "a":"80 м²"}'>Площадь 80 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 010ТБ1", "p":"$3 850", "s":"4.20–12.2 кВт", "d":"1100×445×850", "a":"120 м²"}'>Площадь 120 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 014ТБ1", "p":"$4 508", "s":"5.30–16.5 кВт", "d":"1100×480×850", "a":"165 м²"}'>Площадь 165 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТБ1", "p":"$5 531", "s":"6.20–20.5 кВт", "d":"1110×445×1450", "a":"200 м²"}'>Площадь 200 м²</option>
                  <option style="color:#000" value='{"m":"БЛН 024ТБ3", "p":"$6 095", "s":"6.50–26.1 кВт", "d":"1110×445×1450", "a":"260 м²"}'>Площадь 260 м²</option>
                </select>"""

new_r32_appp = """<select class="area-select" style="width:100%;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:var(--white);padding:10px;border-radius:8px;outline:none;" onchange="updateProd(this)">
                  <option style="color:#000" value='{"m":"БЛН 006ТБ1", "p":"$3 703", "s":"2.50–8.30 кВт", "d":"1100×445×850", "a":"80 м²"}'>80 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 010ТБ1", "p":"$3 850", "s":"4.20–12.2 кВт", "d":"1100×445×850", "a":"120 м²"}'>120 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 010ТБ3", "p":"$4 013", "s":"4.20–12.2 кВт", "d":"1100×445×850", "a":"120 м²"}'>120 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 014ТБ1", "p":"$4 508", "s":"5.30–16.5 кВт", "d":"1100×480×850", "a":"165 м²"}'>165 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 014ТБ3", "p":"$4 669", "s":"5.30–16.5 кВт", "d":"1100×480×850", "a":"165 м²"}'>165 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТБ1", "p":"$5 531", "s":"6.20–20.5 кВт", "d":"1110×445×1450", "a":"200 м²"}'>200 м² (I фаза)</option>
                  <option style="color:#000" value='{"m":"БЛН 018ТБ3", "p":"$5 669", "s":"6.20–20.5 кВт", "d":"1110×445×1450", "a":"200 м²"}'>200 м² (III фазы)</option>
                  <option style="color:#000" value='{"m":"БЛН 024ТБ3", "p":"$6 095", "s":"6.50–26.1 кВт", "d":"1110×445×1450", "a":"260 м²"}'>260 м² (III фазы)</option>
                </select>"""

html = html.replace(old_r32_appp, new_r32_appp)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html")
