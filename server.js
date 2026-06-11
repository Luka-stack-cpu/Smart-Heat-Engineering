require('dotenv').config({ path: require('path').resolve(__dirname, '.env') });

const express = require('express');
const cors = require('cors');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

// === DEBUG ENV VARIABLES ===
console.log('--- ENV DEBUG ---');
console.log('SUPABASE_URL:', process.env.SUPABASE_URL ? 'Loaded' : 'MISSING');
console.log('SUPABASE_SERVICE_KEY:', process.env.SUPABASE_SERVICE_KEY ? 'Loaded' : 'MISSING');
console.log('-------------------');

if (!process.env.SUPABASE_URL || !process.env.SUPABASE_SERVICE_KEY) {
  console.error('FATAL ERROR: Supabase credentials are missing in .env');
  console.error('Пожалуйста, добавьте SUPABASE_URL и SUPABASE_SERVICE_KEY в файл .env!');
  process.exit(1);
}

const app = express();
const PORT = process.env.PORT || 3000;

// Supabase client (Server-side)
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_KEY
);

app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// Базовые данные по умолчанию (чтобы админ-панель не была пустой)
const DEFAULT_DATA = {
  texts: {
    heroTitle: "Тепловые насосы<br>и инженерные<br><em>системы под ключ</em>",
    heroSub: "Проектируем, монтируем и обслуживаем отопление, вентиляцию, холодильное оборудование и водоснабжение. Берём на себя всё — от расчёта до запуска.",
    about: "Мы — не перекупщики с Ошского рынка. 8 лет ставим тепло в дома по Кыргызстану. Знаем, как работает наше оборудование в наших морозах.",
    warranty: "Гарантия 2 года на оборудование, 1 год на монтаж. Сервисное обслуживание — пожизненно. Если что-то сломалось — приедем, разберёмся, починим. Без бюрократии"
  },
  contacts: {
    phone: "+996 999 699 620",
    address: "Бишкек, Токтоналиева 104",
    wa: "996999699620"
  },
  floorPrice: 28,
  equipment: [
    { category: 'heat-pumps', name: 'Тепловой насос R32', model: 'БЛН-009ТА1', price: 2500, image: 'моноб_инвент_теп_нас_2_no_bg_preview_carve_photos.png' },
    { category: 'fancoils', name: 'Настенный фанкойл', model: 'ФП 68БГ', price: 320, image: 'настенный фанкоил.png' },
    { category: 'fancoils', name: 'Настенный фанкойл', model: 'ФП 85БГ', price: 480, image: 'настенный фанкоил.png' },
    { category: 'fancoils', name: 'Кассетный фанкойл', model: 'ФП 34КМ', price: 510, image: 'кассетный_фанкоил_no_bg_preview_carve_photos.png' },
    { category: 'radiators', name: 'Биметаллический радиатор', model: 'Royal Thermo (секция)', price: 8, image: 'radiator.png' },
    { category: 'warm-floor', name: 'Труба PE-RT Valfex', model: 'Бухта 200м', price: 120, image: 'теплые полы.png' },
    { category: 'boilers', name: 'Бойлер косвенного нагрева', model: 'Drazice 200L', price: 850, image: 'вертикальныйц_водонаг_с_тп_r134a_removebg_preview.png' }
  ]
};

/**
 * GET: получить все данные сайта
 */
app.get('/api/data', async (req, res) => {
  try {
    const { data, error } = await supabase
      .from('site_content')
      .select('*');

    if (error) throw error;

    // Начинаем с дефолтных данных
    const result = JSON.parse(JSON.stringify(DEFAULT_DATA));

    // Накладываем данные из Supabase поверх дефолтных
    if (data && data.length > 0) {
      data.forEach(item => {
        try {
          // Пытаемся распарсить значение (если оно сохранено как строка JSON)
          result[item.key] = typeof item.value === 'string' ? JSON.parse(item.value) : item.value;
        } catch (e) {
          result[item.key] = item.value;
        }
      });
    }

    res.json(result);

  } catch (err) {
    console.error('GET error:', err.message);
    // В случае ошибки с БД отдаём дефолтные данные, чтобы сайт не сломался
    res.json(DEFAULT_DATA);
  }
});

/**
 * POST: обновить данные сайта (CMS)
 */
app.post('/api/data', async (req, res) => {
  const { password, data } = req.body;

  if (password !== 'smart2024') {
    return res.status(401).json({ error: 'Неверный пароль' });
  }

  try {
    const formatted = Object.entries(data).map(([key, value]) => ({
      key,
      // Сохраняем объекты как JSON-строку, чтобы избежать [object Object] в текстовых колонках
      value: typeof value === 'object' ? JSON.stringify(value) : value
    }));

    for (const item of formatted) {
      // Проверяем, существует ли уже такой ключ
      const { data: existing, error: selErr } = await supabase
        .from('site_content')
        .select('key')
        .eq('key', item.key);

      if (selErr) throw selErr;

      if (existing && existing.length > 0) {
        // Если ключ есть, обновляем
        const { error: updErr } = await supabase
          .from('site_content')
          .update({ value: item.value })
          .eq('key', item.key);
        if (updErr) throw updErr;
      } else {
        // Если ключа нет, создаем
        const { error: insErr } = await supabase
          .from('site_content')
          .insert({ key: item.key, value: item.value });
        if (insErr) throw insErr;
      }
    }

    res.json({ success: true });

  } catch (err) {
    console.error('POST error:', err.message);
    res.status(500).json({ error: err.message });
  }
});

const server = app.listen(PORT, () => {
  console.log(`Сервер запущен на http://localhost:${PORT}`);
  console.log(`API: http://localhost:${PORT}/api/data`);
});

server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.error(`ОШИБКА: Порт ${PORT} уже занят другим процессом.`);
    process.exit(1);
  }
});