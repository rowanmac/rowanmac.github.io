---
layout: page
title: Essays
permalink: /essays/
---

*Longer form essays. Mostly college work. Will be expanded.*

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