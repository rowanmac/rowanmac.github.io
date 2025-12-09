---
layout: page
title: Notes
permalink: /notes
---

* TOC
{:toc}

# Misc
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
{% for post in site.posts reversed %}
    {% if post.categories contains "note" and post.categories contains "learningPortuguese" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Lists
---

<ul>
{% for list in site.lists %}
        <li><a href="{{ list.url }}">{{ list.title }}</a></li>
{% endfor %}
</ul>

# Reading Journals
---

<ul>
{% for post in site.posts reversed %}
    {% if post.categories contains "note" and post.categories contains "readingJournal" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Reviews
---

<ul>
{% for post in site.posts %}
    {% if post.categories contains "note" and post.categories contains "review" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# 上海杂记
---

<ul>
{% for post in site.posts reversed %}
    {% if post.categories contains "note" and post.categories contains "shanghaiNotes" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

# Source Commentaries
---

<ul>
{% for post in site.posts %}
    {% if post.categories contains "note" and post.categories contains "sourceCommentary" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

