# Coursera Dump

Скрипт выводит в файл формата excel информацию (название, дату начала, язык, продолжительность и рейтинг) о курсах, опубликованных на сайте [coursera.org](https://www.coursera.org). Курсы выбираются случайным образом.

## Пример запуска скрипта
Скрипт имеет два необязательных параметра: `count_courses` и `excel_file`. 
`count_courses` - количество курсов (значение по умолчанию _20_), информация о которых будет выведена в файл `excel_file` (значение по умолчанию _coursera\_courses.xlsx_)

    $ python coursera.py --excel_file coursera.xlsx --count_courses 14

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
