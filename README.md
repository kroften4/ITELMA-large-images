# REST API Endpoints

### GET /list/

Возвращает список всех картинок

### GET /list/`<img_name>`

Возвращает элемент списка с названием `<img_name>`

```json
{
    "name": "ameba",
    "last_opened": "2024-11-23T22:01:06.045371Z",
    "file": "http://127.0.0.1:8000/images/ameba/original.png"
}
```

### GET /previews/`<img_name>`

Возвращает превью к картинке с названием `<img_name>`

```json
{
    "id": 1,
    "file": "/images/ameba/preview.png",
    "original": "ameba"
}
```

### GET /tiles/`<img_name>`?scale=`<scale>`&x=`<x>`&y=`<y>`

Возвращает тайл изображения `<img_name>` по масштабу `<scale>` с координатами `<x>`, `<y>`

```json
{
    "id": 1,
    "scale": 1,
    "x": 0,
    "y": 0,
    "file": "/images/ameba/scale_1/t_0_0.png",
    "original": "ameba"
}
```

### POST /upload/ file:`<file>` name:`<name>`

Создает изображение `<file>` (+превью и тайлы) с именем `<name>` (должно быть уникальным)

```json
{
    "message": "Media uploaded successfully.",
    "data": {
        "name": "ameba",
        "last_opened": "2024-11-23T22:01:06.045371Z",
        "file": "http://127.0.0.1:8000/images/ameba/original.png"
    }
}
```
