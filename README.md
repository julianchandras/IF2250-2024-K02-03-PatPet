# IF2250-2024-K02-03-PatPet

## Overview

![Beranda PatPet](doc/beranda.png "Selamat Datang di Patpet")
PatPet merupakan aplikasi untuk manajemen dan pemeliharan hewan peliharaan. PatPet dapat menampilkan profil dan biodata setiap hewan peliharaan yang dimiliki. Tidak hanya itu, pengguna juga dapat mencatat seluruh aktivitas hewan peliharaan yang dimiliki dan disajikan dalam bentuk kalendar. Tersedia juga artikel-artikel mengenai hewan dan cara pemeliharaannya.

## Prerequisites

- `Python` 3.X installed


## Setup

### Dependencies
Untuk melakukan instalasi terhadap library yang digunakan, ketik pada terminal perintah berikut:
```bash
pip install -r requirements.txt
```

### PyTest (Optional)

Untuk melakukan unit test, ketik pada terminal perintah berikut:
```bash
pytest
```


## Menjalankan Aplikasi


1. Pastikan seluruh dependencies telah di-install dan berada pada directory 'IF2250-2024-K02-03-PatPet'
2. Untuk menjalankan aplikasi, ketik pada terminal perintah berikut:

```bash
py src/main.py
```


## Struktur Database

### 1. Activity

| Field        | Type    | Null | Key | Default | Extra          |
| ------------ | ------- | ---- | --- | ------- | -------------- |
| activity_id  | INT     | NO   | PRI | NULL    | auto_increment |
| activity_name  | TEXT    | NO   |     | NULL    |
| activity_date      | DATE    | NO   |     | NULL    |
| start_time      | TIME    | NO   |     | NULL    |
| end_time | TIME    | NO   |     | NULL    |
| pet_id | INT    | NO   |     | NULL    | REFERENCES pets(pet_id) ON DELETE CASCADE

### 2. Article

| Field         | Type    | Null | Key | Default | Extra          |
| ------------- | ------- | ---- | --- | ------- | -------------- |
| article_id    | INT | NO   | PRI | NULL    | auto_increment |
| title         | TEXT    | NO   |     | NULL    |
| content      | TEXT    | NO   |     | NULL    |

### 3. Foods

| Field        | Type    | Null | Key | Default | Extra                                               |
| ------------ | ------- | ---- | --- | ------- | --------------------------------------------------- |
| food_id      | INT | NO   | PRI | NULL    | auto_increment                                      |
| food_name        | TEXT    | NO   |     | NULL    |

### 4. Pet

| Field    | Type    | Null | Key | Default | Extra          |
| -------- | ------- | ---- | --- | ------- | -------------- |
| pet_id | INT | NO   | PRI | NULL    | auto_increment |
| pet_name     | TEXT    | NO   |     | NULL    |
| species     | TEXT    | NO   |     | NULL    |
| age     | INT    | NO   |     | NULL    |
| medical_record     | TEXT    | NO   |     | NULL    |
| image     | BLOB    | NO   |     | NULL    |

### 5. Pet Food

| Field     | Type    | Null | Key | Default | Extra                        |
| --------- | ------- | ---- | --- | ------- | ---------------------------- |
| pet_food_id | INT  | NO   | PRI | NULL    | auto_increment|
| pet_id  | INT | NO   |  | NULL    | REFERENCES pets(pet_id) ON DELETE CASCADE  |
| food_id  | INT | NO   |  | NULL    | REFERENCES foods(food_id) ON DELETE CASCADE  |

## Authors & Contributions

### Authors

| NIM      | Name                  | GitHub                                            |
| -------- | --------------------- | ------------------------------------------------- |
| 13521044 | Rachel Gabriela Chen  | [chaerla](https://github.com/chaerla)             |
| 13521046 | Jeffrey Chow          | [JeffreyChow19](https://github.com/JeffreyChow19) |
| 13521074 | Eugene Yap Jin Quan   | [yuujin-Q](https://github.com/yuujin-Q)           |
| 13521094 | Angela Livia Arumsari | [liviaarumsari](https://github.com/liviaarumsari) |
| 13521100 | Alexander Jason       | [AJason36](https://github.com/AJason36)           |

### Contributions

| NIM      | Contributions                             |
| -------- | ----------------------------------------- |
| 13521044 | Home page, database, controller, unittest |
| 13521046 | Recipe list, article list, CI/CD          |
| 13521074 | Note editor (add/edit) page, testing      |
| 13521094 | Recipe detail page, article detail page   |
| 13521100 | Recipe editor (add/edit) page             |