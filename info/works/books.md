---
layout: page
title: Books
permalink: /books
---
{% for book in site.books %}
- [{{ book.bibliography }}]({{ book.url }})
{% endfor %}