from random import sample
from lxml import etree
import requests
from bs4 import BeautifulSoup


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


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(courses_info, filepath=''):
    pass


if __name__ == '__main__':
    coursera_courses_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    xml_text = get_web_page(coursera_courses_url)
    courses_list = get_courses_list(xml_text)
    random_courses_list = get_random_elements_from_list(courses_list, 2)
