---
layout: page
title: Lists
permalink: /Lists
---
<ul>
{% for list in site.lists %}
    <li><a href="{{ list.url }}">{{ list.title }}</a></li>
{% endfor %}
</ul>