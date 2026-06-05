const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const DATA_FILE = path.join(__dirname, 'data.json');

app.use(cors());
app.use(express.json());
// Раздаем статические файлы из корня проекта
app.use(express.static(__dirname));

// Получение данных
app.get('/api/data', (req, res) => {
  fs.readFile(DATA_FILE, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Failed to read data' });
    }
    res.json(JSON.parse(data));
  });
});

// Обновление данных
app.post('/api/data', (req, res) => {
  const { password, data } = req.body;
  
  if (password !== 'smart2024') {
    return res.status(401).json({ error: 'Неверный пароль' });
  }

  fs.writeFile(DATA_FILE, JSON.stringify(data, null, 2), 'utf8', (err) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Ошибка сохранения' });
    }
    res.json({ success: true });
  });
});

app.listen(PORT, () => {
  console.log(`Сервер запущен на http://localhost:${PORT}`);
  console.log(`Админ-панель доступна по адресу: http://localhost:${PORT}/admin/`);
});
