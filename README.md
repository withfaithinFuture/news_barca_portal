# ⚽ FC Barca Services

**FC Barca Services** — микросервисный проект на Django с поддержкой аутентификации, управления контентом, обратной связью через Telegram и WebSocket-чатом.  
Используются Docker, Redis, PostgreSQL и Nginx для масштабируемости и высокой производительности.

---

## 📚 Сервисы

| Сервис               | Описание                                                                 |
|----------------------|--------------------------------------------------------------------------|
| **auth_service**     | Регистрация и аутентификация пользователей (JWT/OAuth)                   |
| **content_service**  | Управление контентом (фото/видео), лайки, WebSocket-чат                  |
| **feedback_service** | Обратная связь через Telegram Bot API                                    |
| **nginx**           | Обратный прокси и маршрутизация запросов между сервисами                |
| **db**              | PostgreSQL — основная реляционная база данных                            |
| **redis**           | Брокер сообщений для WebSocket и кеширования                            |

---

## 🧰 Технологии

### 💻 Backend
- **Python 3.11**
- **Django** (основной веб-фреймворк)
- **Django Channels** (поддержка WebSocket в `content_service`)
- **Gunicorn** (WSGI) / **Daphne** (ASGI)
- **PostgreSQL** (основная СУБД)
- **Redis** (брокер сообщений и кеш)

### 🐳 Контейнеризация
- **Docker** (изоляция микросервисов)
- **Docker Compose** (управление контейнерами)
- **Nginx** (обратный прокси + балансировка нагрузки)

### 🌐 Интеграции
- **Telegram Bot API** (обратная связь в `feedback_service`)

### 🧪 Тестирование
- **pytest** / **unittest**
- **GitHub Actions** (CI/CD)

---

## 🚀 Быстрый старт

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/withtrrtuture/fc_barca_services.git
   cd fc_barca_services
