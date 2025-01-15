---
layout: page
title: Articles
permalink: /articles
---

{% for article in site.articles %}
- [{{ article.bibliography }}]({{ article.url }})
{% endfor %}