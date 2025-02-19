---
layout: page
permalink: /books
---
{% for book in site.books %}
    {% include bookDirectoryTemplate.html %}
{% endfor %}