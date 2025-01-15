---
layout: page
title: Books
permalink: /books
---
{% for book in site.books %}
- <a href="{{ book.url }}">{{ book.title }} - {{ book.authors }}</a>
{% endfor %}