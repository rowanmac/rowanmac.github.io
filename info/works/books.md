---
layout: page
title: Books
permalink: /books
---
{% for book in site.books %}
- <a href="{{ book.url }}">{{ book.title }} - {% if book.editors %}ed. {{ book.editors }}{% else %}{{ book.authors }}{% endif %}</a>
{% endfor %}