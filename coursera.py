from random import sample
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests


def get_web_page(url, payload=None):
    return requests.get(url, payload).text


def get_courses_list(xml_text):
    xml_bytes_text = bytes(xml_text, encoding='utf-8')
    xml = etree.XML(xml_bytes_text)
    courses_list = []
    for element in xml.iter('*'):
        if element.text.rstrip():
            courses_list.append(element.text)
    return courses_list


def get_random_elements_from_list(list_elements, count_random_elements=20):
    return sample(list_elements, count_random_elements)


def find_coursera_courses_info(courses_urls):
    courses_info = []
    for url in courses_urls:
        html_page = get_web_page(url)
        course_info = get_course_info(html_page)
        courses_info.append(course_info)
    return courses_info


def get_course_info(course_slug):
    soup = BeautifulSoup(course_slug, 'html.parser')
    course_info = {}
    course_info['title'] = soup.find('h1', class_='title').string
    start_date = soup.find('div', class_='startdate').string
    course_info['starting_date'] = start_date.split(maxsplit=1)[1]
    languages = soup.find('div', class_='language-info').text
    course_info['language'] = languages.split(',')[0]
    course_info['duration_in_weeks'] = len(soup.find_all('div', class_='week'))
    rating_tag = soup.find('div', class_='ratings-text')
    if rating_tag:
        course_info['rating'] = rating_tag.string.split()[0]
    else:
        course_info['rating'] = 'No rating'
    return course_info


def output_courses_info_to_xlsx(courses_info, filepath='coursera_courses.xlsx'):
    excel_book = Workbook()
    sheet = excel_book.active
    sheet.title = 'Coursera'
    sheet['A1'] = 'Course title'
    sheet['B1'] = 'Starting date'
    sheet['C1'] = 'Language'
    sheet['D1'] = 'Duration (weeks)'
    sheet['E1'] = 'Rating'
    for row, course in enumerate(courses_info):
        sheet.cell(row=row + 2, column=1, value=course['title'])
        sheet.cell(row=row + 2, column=2, value=course['starting_date'])
        sheet.cell(row=row + 2, column=3, value=course['language'])
        sheet.cell(row=row + 2, column=4, value=course['duration_in_weeks'])
        sheet.cell(row=row + 2, column=5, value=course['rating'])
    excel_book.save(filepath)


if __name__ == '__main__':
    coursera_courses_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    xml_text = get_web_page(coursera_courses_url)
    courses_list = get_courses_list(xml_text)
    random_courses_list = get_random_elements_from_list(courses_list, 3)
    coursera_courses_info = find_coursera_courses_info(random_courses_list)
    output_courses_info_to_xlsx(coursera_courses_info)
