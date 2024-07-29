
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