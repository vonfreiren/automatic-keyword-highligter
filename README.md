# automatic-keyword-highligter
Script used to edit and highlight keywords in articles (Markdown files)

It's achieved by doing the following:

- Opening and reading the desired markdown file.
- Collecting the relevant words. For example, excluding HTML elements such as <p> or <div>.
- Getting the most relevant keywords from the text. Stop words are not used.
- (Optional) getting keywords not used in the vocabulary.
- Replacing the text with the markdown (Jekyll) formatting.
- Saving the new markdown file with the automatic formatting done.
