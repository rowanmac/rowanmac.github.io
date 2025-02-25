---
layout: page
title: Irish History Brief
permalink: /irishHistoryBrief/
---
<ul>
{% for post in site.posts %}
    {% if post.categories.first == "ihb" %}
        <a href="{{ post.url }}">{{ post.title }}</a>
    {% endif %}
{% endfor %}
</ul>