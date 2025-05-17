---
layout: page
title: Notes
permalink: /notes
---
<ul>
{% for post in site.posts %}
    {% if post.categories.first == "note" %}
        <li>{{ post.date | date: '%d/%m/%y'}} <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

