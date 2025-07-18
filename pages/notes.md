---
layout: page
title: Notes
permalink: /notes
---

# General
---

<ul>
{% for post in site.posts %}
    {% if post.categories[0] == "note" and post.categories.size == 1 %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Learning Portuguese
---

<ul>
{% for post in site.posts %}
    {% if post.categories[0] == "note" and post.categories[1] == "learningPortuguese" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Reading Journals
---

<ul>
{% for post in site.posts %}
    {% if post.categories[0] == "note" and post.categories[1] == "readingJournal" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>


