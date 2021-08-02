from random import randint

import requests
from bs4 import BeautifulSoup


def soup_aggregator(url):
    try:
        url = f'https://stackoverflow.com/questions/{url}'
        r = requests.get(url=url)
        bs_page = BeautifulSoup(r.text, features='lxml')
        question = bs_page.find(class_='s-prose js-post-body', attrs='text').text.strip()
        tags = bs_page.find(class_='post-taglist d-flex gs4 gsy fd-column', attrs='text').text
        answer = bs_page.find(class_='answer accepted-answer', attrs='text').text.strip('\n\n')
        result = f'TAGS:{tags}\nQUESTION:\n{question}\n\nANSWER{answer}\n{100 * "."}'
        return result
    except AttributeError:
        print(f'URL:{url} is not available\n'
              'Enter other number of question')


def line_stripper(file):
    if file is not None:
        string_with_empty_lines = file
        lines = string_with_empty_lines.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"
        print(string_without_empty_lines)
        return string_without_empty_lines
    else:
        none_result = 'Result not found'
        return none_result


def output_write(output_file):
    if output_file is not None:
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(output_file)
    else:
        print('Result unavailable')
        pass


def container():
    file = line_stripper(soup_aggregator(randint(1, 1000000)))
    output_write(file)


container()

if __name__ == 'main':
    container()
