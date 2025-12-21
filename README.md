## Image captioning с помощью VLM
Генерация описаний картинок с помощью VLM (Qwen2.5-VL-3B).

### Локальная сборка и запуск
- Сборка приложения:
```bash
docker compose build
```
- Запуск приложения:
```bash
docker compose up
```

### Запуск из готового образа с GHCR
Чтобы запустить приложение из готового образа с GHCR, необходимо:
- Спуллить готовый образ:
```bash
docker pull ghcr.io/soundwave-77/vlm_captioning:latest
```
- Поднять контейнер из скачанного образа:
```bash
docker run -p 8501:8501 ghcr.io/soundwave-77/vlm_captioning:latest
```

После этого можно перейти на `http://0.0.0.0:8501/` и протестировать приложение