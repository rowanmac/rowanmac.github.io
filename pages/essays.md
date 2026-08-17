---
layout: page
title: Essays
permalink: /essays/
---

<div class="pageIntro">Longer form essays. Mostly college work. Will be expanded.</div>

---

<ul>
{% for post in site.posts %}
    {% if post.categories.first == "essay" %}
        <li>
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endif %}
{% endfor %}
</ul>