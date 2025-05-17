---
layout: page
title: Essays
permalink: /essays
---

<ul>
{% for post in site.posts %}
    {% if post.categories.first == "essay" %}
        <li>
            {{ post.date | date: '%d/%m/%y'}} <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endif %}
{% endfor %}
</ul>