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

# About
This is the list of issues for my bibliographic project, The Irish History Brief which is also hosted as a [newsletter on Substack](https://irishhistorybrief.substack.com/). In late 2024 I was looking for up-to-date information about what was being published in Irish history and I discovered that there really wasn't any frequently updated database. Since then I have been keeping my own notes on what is published on a month-by-month basis.

# Sourcing
I get my data from a wide base of sources: journal and publisher email alerts, RSS feeds, the Book Ireland Magazine First Flush section, quarterly publishing catalogues, social media etc. If you can think of any good sources of information that would increase coverage or notice any missed items please do let me know by emailing irishhistorybrief@gmail.com. I don't claim to have comprehensive coverage and it is hard to judge how much I miss every month but I try to amend missed items as soon as I become aware of them.

# Goals
The goal of this project is to publish at the end of every month a comprehensive list of new publishings in Irish history relevant to an academic audience. I don't aim to provide a full database with robust searching capabilities, [Irish History Online](https://www.iho.ie/) is the best place for that even if it is not fully up to date. This is only a newsletter, giving you a brief month-by-month overview of what is being worked on currently in Irish history. The borders of disciplines are often blurry and sometimes the works included might shade into archaeological, literary or linguistic studies but the main focus is on history based on written and oral sources.

# Method
Judging what is and what isn't academic can be a thorny issue, in my case I take a broad definition as being works released by a reputable publisher or written by a trustworthy author which might be of interest to an academic reader or enthusiast. My focus is on tracking and collecting the production of new research so I omit 2nd editions, reprintings, physical releases of works already published online, or works which appear to not offer any new perspective on Irish history. This is not to say I am shunning popular history. For example an independently researched and published work of local history would certainly be included, while a book called *100 amazing facts about Michael Collins* probably wouldn't (unless they really were amazing facts based on new analysis).

# What is included?
Expect to see books, both from university presses and generalist publishers, journal articles and academic book reviews. When book chapters are written by different authors, I try to list the chapters separately when I can get this information. I would love to include PhD theses and conference papers and am currently thinking about how I could conveniently and comprehensively access this data. It would also be nice to include things like articles, say for example from History Ireland magazine, or new documentaries, radio shows, podcasts etc, but I haven't found a good way to collect this data.

# Features & Planned Features
- [x] A monthly brief.
- [x] Individual pages for each work with more information.
- [x] A newsletter version.
- [ ] Options to export citation data to reference managment software.
- [ ] Directory of journals, publishers & scholars which have appeared in the brief.
- [ ] Inclusion of conference papers & PhD theses.
- [ ] Inclusion of newspaper articles and reviews, documentaries, radio features & podcasts.