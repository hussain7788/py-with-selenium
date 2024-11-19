
## Dominate is a Python library specifically designed for creating and manipulating HTML documents. \
## It provides a user-friendly way to build HTML structures programmatically without the need for a separate 
## template language.

import dominate
from dominate.tags import link, div, h1, p, a # Importing the tags we need

doc = dominate.document(title='Dominate Example')

with doc.head:
    link(rel='stylesheet', href='style.css')

with doc:
    with div(id='header'):
        h1('My Web Page')

print(doc)

### html2text is a Python library that converts HTML to plain text. 
# It is useful for extracting text content from HTML documents, \
from dominate.tags import div,span,input_, textarea
import html2text    

def test_span():
    return span('Email', input_(type="radio", disabled="true"))


def html_to_text(html):
    return html2text.html2text(html)


htm = test_span()
print(html_to_text(str(htm)))

text_area = div(
            textarea("I am Hussain", style="height:100px; width:500px;", disabled="true"))
print(text_area)
print(html_to_text(str(text_area)))