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
{% for book in site.books %}
    {% if book.categories contains "review" %}
        <li><a href="{{ book.url }}"><i>{{ book.title }}</i>{% if book.author %} by {% if book.author.size == 1 %}{{ book.author[0].given }} {{ book.author[0].family }}{% else %}{% for person in book.author %}{% if forloop.last == true %} and {% endif %}{{ person.given }} {{ person.family }}{% if forloop.last == false %}, {% endif %}{% endfor %}{% endif %}{% endif %}
          {% if book.editor %}edited by {% if book.editor.size == 1 %}{{ book.editor[0].given }} {{ book.editor[0].family }}{% else %}{% for person in book.editor %}{% if forloop.last == true %} and {% endif %}{{ person.given }} {{ person.family }}{% if forloop.last  == false %}, {% endif %}{% endfor %}{% endif %}{% endif %}</a></li>
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

