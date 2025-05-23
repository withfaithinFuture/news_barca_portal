# ⚽ FC Barca Services

**FC Barca Services** — микросервисный проект на Django с поддержкой аутентификации, управления контентом, обратной связью через Telegram и WebSocket-чатом. Используются Docker, Redis, PostgreSQL и Nginx.

---

## 📚 Сервисы

- `auth_service` — регистрация и вход пользователей
- `content_service` — контент (фото, видео, лайки, WebSocket)
- `feedback_service` — обратная связь через Telegram
- `nginx` — прокси и маршрутизация запросов
- `db` — PostgreSQL база данных
- `redis` — брокер сообщений для WebSocket

---

🧰 Используемые технологии
Проект построен с использованием современных технологий и инструментов:

💻 Backend
Python 3.11
Django — основной веб-фреймворк
Django Channels — поддержка WebSocket в content_service
Gunicorn / Daphne — сервера приложений для WSGI и ASGI
PostgreSQL — реляционная СУБД
Redis — брокер сообщений для WebSocket и кэша

🐳 Контейнеризация
Docker — изоляция микросервисов
Docker Compose — управление множеством контейнеров
Nginx — обратный прокси и маршрутизация запросов

📦 DevOps / CI
Git — контроль версий
GitHub Actions — автоматическое тестирование
Environment Variables (.env) — настройка конфигурации сервисов

🌐 Telegram интеграция
Telegram Bot API — для получения сообщений и обратной связи через feedback_service

🧪 Тестирование
pytest / unittest (в зависимости от реализации)
Автоматический запуск тестов при push в GitHub (CI)
