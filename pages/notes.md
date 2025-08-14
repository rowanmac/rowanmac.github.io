---
layout: page
title: Notes
permalink: /notes
---

* TOC
{:toc}

# General
---

<ul>
{% for post in site.posts %}
    {% if post.categories.size == 1 and post.categories contains "note" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Learning Portuguese
---

<ul>
{% for post in site.posts %}
    {% if post.categories contains "note" and post.categories contains "learningPortuguese" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Reading Journals
---

<ul>
{% for post in site.posts %}
    {% if post.categories contains "note" and post.categories contains "readingJournal" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Book Reviews
---

<ul>
{% for post in site.posts %}
    {% if post.categories contains "note" and post.categories contains "review" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Source Commentaries
---

<ul>
{% for post in site.posts %}
    {% if post.categories contains "note" and post.categories contains "commentary" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

