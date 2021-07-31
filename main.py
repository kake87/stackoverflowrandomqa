import requests
from random import randint

from bs4 import BeautifulSoup


def soup_aggregator(url):
    try:
        url = f'https://stackoverflow.com/questions/{url}'
        r = requests.get(url=url)
        bs_page = BeautifulSoup(r.text, features='lxml')
        question = bs_page.find(class_='s-prose js-post-body', attrs='text').text.strip()
        tags = bs_page.find(class_='post-taglist d-flex gs4 gsy fd-column', attrs='text').text
        answer = bs_page.find(class_='answer accepted-answer', attrs='text').text.strip('\n\n')  
        result = f'TAGS{tags}QUESTION\n{question}\n{100*"."}\nANSWER{answer}'
        return result
    except AttributeError:
        print( f'URL:{url} is not available\n'
                'Enter other number of question')

def line_stripper(file):
    string_with_empty_lines =  file
    lines = string_with_empty_lines.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    string_without_empty_lines = ""
    for line in non_empty_lines:
        string_without_empty_lines += line + "\n"
    print(string_without_empty_lines)
    return string_without_empty_lines

def output_write(output_file):
    if output_file!=None:
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(output_file)
    else:
        print('Unwritebale')
        pass

def container():
    file = line_stripper(soup_aggregator(randint(1,1000000)))
    file
    output_write(file)

container()

if __name__ == 'main':
    container