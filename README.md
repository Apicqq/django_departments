# Веб-страница иерархии департаментов организации

Информация о каждом сотруднике должна хранится в базе данных и содержит следующие данные:
- ФИО
- Должность
- Дата приёма на работу
- Размер заработной платы
- Подразделение - подразделения имеют структуру до 5 уровней

Дерево отображается в свёрнутом виде.

База данных должна содержит не менее 50 000 сотрудников и 25 подразделений в 5 уровнях иерархий
<small> <br>Наполнить базу данных тестовыми данными можно через management команду `python manage.py populate_fake_data`</small>

Управление записями CRUD осуществляется через административную часть Django

Зависимости:
- python = "^3.13"
- django = "^5.1.6"
- faker = "^36.1.1"
- django-bootstrap5 = "^24.3"