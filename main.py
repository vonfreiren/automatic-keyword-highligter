from detect_keywords import get_scores
from edit_md import edit_file



def format_article(file_path, number_of_words=10, include_non_existing_words=False, number_of_non_exist_voc = 2,  split_word='Introduction', language='english'):

    results, words_not_voc = get_scores(file_path, language)

    top_results = results[:number_of_words]

    if include_non_existing_words:
        top_2_not_voc = words_not_voc[:number_of_non_exist_voc]
        for word in top_2_not_voc:
            text = word
            top_results.append(text)

    edit_file(file_path, top_results, split_word=split_word)




### Edit this file path

file_path = '/Users/javier/IdeaProjects/vonfreiren.github.io/_posts/2022-11-04-how-nutrition-is-impacting-your-life.md'

### Edit this file path

format_article(file_path, number_of_words=10, include_non_existing_words=False, number_of_non_exist_voc = 2,  split_word='Introduction', language='english')
