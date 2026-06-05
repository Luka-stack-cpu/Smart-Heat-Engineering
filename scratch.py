import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract parts
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', content, re.DOTALL)
nav_match = re.search(r'(<nav>.*?</nav>.*?</div>)', content, re.DOTALL)
footer_match = re.search(r'(<footer>.*?</footer>)', content, re.DOTALL)

head = head_match.group(1) if head_match else ""
nav = nav_match.group(1) if nav_match else ""
footer = footer_match.group(1) if footer_match else ""

# FAQ
faq_content = """
<section id="faq-page" style="padding-top: 150px; padding-bottom: 100px; min-height: 80vh; background: var(--dark);">
  <div style="max-width: 820px; margin: 0 auto;">
    <div class="sec-head" style="text-align:center;">
      <h1 class="sec-title">Вопросы, которые нам задают чаще всего</h1>
      <p class="sec-desc" style="margin:0 auto;">Если не нашли ответ — просто позвоните. Мы не кусаемся</p>
    </div>
    
    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Сколько стоит установка теплового насоса?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Зависит от объекта. Дом 120 м² — примерно $800–1200 за монтаж. Но лучше вызвать нас на замер, тогда скажем точно. Замер бесплатный</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Можно ли поставить тепловой насос в квартиру?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Можно, если есть балкон или технический этаж для наружного блока. Внутри ставим настенный бойлер или фанкойлы. Звоните, посмотрим вашу планировку</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Работает ли насос при −25°C?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Да, если это модель с технологией ЭВИ. В нашем каталоге такие есть — смотрите бытовые и коммерческие серии. При −25°C он теряет немного мощности, но дом отапливает</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Сколько служит тепловой насос?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Сам компрессор — 10–15 лет. Мы даём гарантию 2 года на оборудование и 1 год на монтаж. Но с обслуживанием работает дольше</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Что выгоднее — тепловой насос или газ?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">В Кыргызстане газ есть не везде. Если газа нет — насос однозначно выгоднее электрического котла. Если газ есть — считайте по тарифам, но насос ещё и охлаждает летом</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Нужен ли тёплый пол или хватит радиаторов?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Тёплый пол комфортнее и экономичнее — вода в нём тёплая, а не горячая. Но радиаторы тоже работают. Если ремонт с нуля — рекомендуем пол. Если уже живёте — радиаторы быстрее поставить</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Можно ли управлять насосом со смартфона?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Да, большинство наших моделей имеют Wi-Fi. Приложение на русском, можно задать расписание, температуру по комнатам, смотреть расход энергии</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">А если насос сломается зимой?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">У нас есть сервисная служба. В рабочее время приедем в тот же день. Вне рабочего — экстренный выезд. Но ломаются они редко, если ставят правильно</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Сколько времени занимает монтаж?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Квартира с бойлером — 1 день. Дом 120 м² с тёплым полом — 2–3 дня. Большой коммерческий объект — до недели. Всё зависит от сложности</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">Вы работаете только в Бишкеке?<span class="faq-arrow">+</span></button>
        <div class="faq-ans"><div class="faq-ans-inner">Нет, ездим по всему Кыргызстану. Были в Иссык-Куле, Нарыне, Оше, Джалал-Абаде. Дальше едем — дорогу оплачиваете вы, но это небольшая сумма</div></div>
      </div>
    </div>
  </div>
</section>
<script>
  function toggleFaq(btn) {
    const item = btn.parentElement;
    const ans = item.querySelector('.faq-ans');
    const inner = item.querySelector('.faq-ans-inner');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(el => {
      el.classList.remove('open');
      el.querySelector('.faq-ans').style.maxHeight = null;
      el.querySelector('.faq-arrow').style.transform = 'rotate(0deg)';
    });
    if (!isOpen) {
      item.classList.add('open');
      ans.style.maxHeight = inner.scrollHeight + "px";
      btn.querySelector('.faq-arrow').style.transform = 'rotate(45deg)';
    }
  }
  function toggleMenu() { document.getElementById('mobileMenu').classList.toggle('open'); document.getElementById('burger').classList.toggle('open'); }
</script>
"""

with open("faq.html", "w", encoding="utf-8") as f:
    f.write(f"{head}\n<body>\n{nav}\n{faq_content}\n{footer}\n</body></html>")

# Services
services_content = """
<section id="services-page" style="padding-top: 150px; padding-bottom: 100px; min-height: 80vh; background: var(--black);">
  <div style="max-width: 1300px; margin: 0 auto;">
    <div class="sec-head" style="text-align:center; margin-bottom: 60px;">
      <h1 class="sec-title">Что мы делаем кроме продажи коробок</h1>
    </div>
    
    <div class="services-grid">
      <div class="srv-card">
        <div class="srv-icon">📐</div>
        <h3>Проектирование</h3>
        <p>Не начинаем монтаж, пока не нарисуем схему. Где поставить наружный блок, как развести трубы, сколько фанкойлов нужно — всё считаем заранее. Экономит ваши деньги и наши нервы</p>
      </div>
      <div class="srv-card">
        <div class="srv-icon">🔧</div>
        <h3>Монтаж</h3>
        <p>Наши бригады — не случайные люди с авито. Работают по стандартам, знают оборудование SolarEast, Sunrain и NULITE вдоль и поперёк. Средний монтаж дома 120 м² — 2–3 дня</p>
      </div>
      <div class="srv-card">
        <div class="srv-icon">🧼</div>
        <h3>Обслуживание</h3>
        <p>Раз в год приедем, проверим давление, почистим фильтры, обновим прошивку. Как у стоматолога — лучше профилактика, чем ремонт</p>
      </div>
      <div class="srv-card">
        <div class="srv-icon">🛡️</div>
        <h3>Гарантийный ремонт</h3>
        <p>Если что-то сломалось по нашей вине — чиним за свой счёт. Если по вине производителя — сами общаемся с заводом. Вам не придётся доказывать, что вы всё делали правильно</p>
      </div>
    </div>
    <div style="text-align:center; margin-top: 50px;">
      <a href="callback.html" class="btn-primary" style="font-size: 16px; padding: 16px 32px;">Нужна консультация?</a>
    </div>
  </div>
</section>
<script>function toggleMenu() { document.getElementById('mobileMenu').classList.toggle('open'); }</script>
"""

with open("services.html", "w", encoding="utf-8") as f:
    f.write(f"{head}\n<body>\n{nav}\n{services_content}\n{footer}\n</body></html>")

# Callback
callback_content = """
<section id="callback-page" style="padding-top: 150px; padding-bottom: 100px; min-height: 80vh; background: var(--dark);">
  <div class="contact-grid">
    <div class="contact-info">
      <h1 class="sec-title">Давайте поговорим</h1>
      <p class="sec-desc">Иногда проще 10 минут поговорить, чем 2 часа читать форумы. Закажите звонок — мы перезвоним в удобное время и разберём вашу ситуацию. Бесплатно, без обязательств</p>
      <div style="margin-top: 40px; display: flex; flex-direction: column; gap: 16px;">
        <a href="https://wa.me/996999699620?text=Здравствуйте!%20Хочу%20задать%20вопрос." class="btn-wa" style="justify-content:center; padding: 18px;" target="_blank">
          <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.127.558 4.122 1.534 5.857L.054 23.394a.5.5 0 0 0 .612.612l5.537-1.48A11.94 11.94 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.907 0-3.692-.526-5.215-1.44l-.374-.222-3.882 1.038 1.038-3.882-.222-.374A9.944 9.944 0 0 1 2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
          Или напишите сразу в WhatsApp
        </a>
        <p style="color: var(--muted); text-align:center;">Или позвоните сами: <a href="tel:+996999699620" style="color:var(--g4);text-decoration:none;font-weight:600;">+996 999 699 620</a></p>
      </div>
    </div>
    
    <div class="contact-form">
      <div class="form-title">Форма заявки</div>
      <div class="form-group">
        <label>Ваше имя</label>
        <input type="text" id="cb-name" placeholder="Как к вам обращаться?">
      </div>
      <div class="form-group">
        <label>Телефон</label>
        <input type="text" id="cb-phone" placeholder="+996 XXX XXX XXX">
      </div>
      <div class="form-group">
        <label>Удобное время для звонка</label>
        <select id="cb-time" style="width:100%; background:rgba(255,255,255,0.05); border:1px solid var(--border); color:var(--white); border-radius:10px; padding:13px 16px; font-size:15px; font-family:'Inter',sans-serif; outline:none; appearance:none;">
          <option style="color:#000;">Утро 9–12</option>
          <option style="color:#000;">День 12–15</option>
          <option style="color:#000;">Вечер 15–18</option>
          <option style="color:#000;">Любое</option>
        </select>
      </div>
      <div class="form-group">
        <label>Тема звонка</label>
        <select id="cb-topic" style="width:100%; background:rgba(255,255,255,0.05); border:1px solid var(--border); color:var(--white); border-radius:10px; padding:13px 16px; font-size:15px; font-family:'Inter',sans-serif; outline:none; appearance:none;">
          <option style="color:#000;">Подобрать оборудование</option>
          <option style="color:#000;">Узнать цену монтажа</option>
          <option style="color:#000;">Гарантийное обслуживание</option>
          <option style="color:#000;">Другое</option>
        </select>
      </div>
      <button class="btn-primary form-submit" onclick="submitCallback()">Заказать звонок</button>
    </div>
  </div>
  
  <div id="cb-toast" style="position:fixed; bottom:100px; left:50%; transform:translateX(-50%) translateY(30px); background:var(--g2); border:1px solid var(--g4); color:#fff; padding:18px 24px; border-radius:12px; font-size:15px; font-weight:500; z-index:9998; opacity:0; transition:opacity 0.3s, transform 0.3s; pointer-events:none; max-width:90vw; text-align:center;">
    Отлично! Перезвоним в указанное время. Если передумаете — просто напишите в WhatsApp
  </div>
</section>

<script>
  function submitCallback() {
    const name = document.getElementById('cb-name').value;
    const phone = document.getElementById('cb-phone').value;
    if (!name || !phone) return;
    
    const toast = document.getElementById('cb-toast');
    toast.style.opacity = '1';
    toast.style.transform = 'translateX(-50%) translateY(0)';
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(-50%) translateY(30px)';
    }, 4000);
    
    document.getElementById('cb-name').value = '';
    document.getElementById('cb-phone').value = '';
  }
  function toggleMenu() { document.getElementById('mobileMenu').classList.toggle('open'); }
</script>
"""

with open("callback.html", "w", encoding="utf-8") as f:
    f.write(f"{head}\n<body>\n{nav}\n{callback_content}\n{footer}\n</body></html>")
