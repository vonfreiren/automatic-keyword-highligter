import re

import markdown
from bs4 import BeautifulSoup



def get_text_article(file_path):
    split_word = 'Introduction'

    with open(file_path, "r") as f:
        md_content = f.read()

    base_text = md_content
    lines = base_text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("##"):
            split_word = line
            break


    html = markdown.markdown(md_content)
    html = html.split(split_word)[-1]
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all(['p','div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'ol', 'blockquote', 'a']):
        tag.unwrap()
    text = soup.get_text()
    text = re.sub('\n', ' ', text)
    #text = ' '.join(html.split())
    return text, split_word

