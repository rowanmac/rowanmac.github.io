---
layout: page
title: Irish History Brief
permalink: /irishHistoryBrief/
---
<ul>
{% for post in site.posts %}
    {% if post.categories.first == "ihb" %}
        <li>
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endif %}
{% endfor %}
</ul>