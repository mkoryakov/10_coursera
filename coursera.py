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
    course_info['start_date'] = start_date.split(maxsplit=1)[1]
    languages = soup.find('div', class_='language-info').text
    course_info['language'] = languages.split(',')[0]
    course_info['duration_in_weeks'] = len(soup.find_all('div', class_='week'))
    rating_tag = soup.find('div', class_='ratings-text')
    if rating_tag:
        course_info['rating'] = rating_tag.string.split()[0]
    else:
        course_info['rating'] = None
    return course_info


def output_courses_info_to_xlsx(courses_info, filepath=''):
    info = 'title: %s\nstart_date: %s\nlanguage: %s\nduration: %s\nrating: %s'
    for course in courses_info:
        print(info % (course['title'], course['start_date'], course['language'],
                      course['duration_in_weeks'], course['rating']))


if __name__ == '__main__':
    coursera_courses_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    xml_text = get_web_page(coursera_courses_url)
    courses_list = get_courses_list(xml_text)
    random_courses_list = get_random_elements_from_list(courses_list, 3)
    coursera_courses_info = find_coursera_courses_info(random_courses_list)
    output_courses_info_to_xlsx(coursera_courses_info)
