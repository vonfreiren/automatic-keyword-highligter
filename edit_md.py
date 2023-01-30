import re

def edit_file(file_path, keywords, split_word = 'Introduction'):
    pigment_key = '`'

    with open(file_path, "r") as f:
        md_content = f.read()
        intro = md_content.split(split_word)[0]
        text = md_content.split(split_word)[-1]

    lines = text.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith("##"):
            for key in keywords:
                word = key
                word = " " + word + " "
                lines[i] = re.sub(r'\b' + re.escape(word) + r'\b', pigment_key + word + pigment_key, lines[i])

    text = "\n".join(lines)
    md_content = intro + split_word + text

    with open(file_path, "w") as file:
        file.write(md_content)
        print("File saved: " + file_path)
