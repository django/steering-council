---
date: 2025-10-13
members:
  - Emma Delescolle
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
attendees:
  - Catherine Holmes
  - Natalia Bidart
---

## Agenda

- [async] Approved DEPs
    - [0016 - Name the main command](https://github.com/django/deps/blob/main/accepted/0016-name-main-command-django.rst) Django PR: [#100](https://github.com/django/deps/pull/100) 
    - 0015 - Improved startproject interface PR: [#98](https://github.com/django/deps/pull/98)
- Django on the Med


## Action items

- Merge PR #98 (DEP 15)
- Tim: Preliminary review of DEP 10 adjustments
- Tim: Open a few third party package docs references in the docs
    - Add mention of django-upgrade to release notes docs 
    - Mention community page AND django packages
- Emma: Draft blog post on 6.x Features - still need to setup a meeting with the fellows about that
- Frank: Write blog post about packages eco-system
- All: Collect preferences for 6.1 release
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Check with fellows if billing scheme is ok
    - Plan another meeting with Lexi once the above is done

### Approved DEPs

- Need to merge PR: #98
- Announce the approved DEPs?
    - Do we want a blog post? This may help us get people to do exactly what Frank and Carlton were hoping for
- On the topic of project templates
    - Copier, cookiecutter and Django’s own project template
    - Django project templates
        - Was post hooks in the past
        - Would be nice to have templates maintained outside of Django core
    - Do we want to support plugins for project templates
        - Run pip install, then `django new`
        - Could we use Pluggy here?
            - Emma has been working on a modernization of admin that utilizes Pluggy
            - Let’s mention this on the DEP and get community feedback.

### Django on the Med

- Carlton led roadmapping session
    - Many ideas were proposed
- Lily led new-features repo review
- Mariusz and Simon progressed DB backed on_delete functionality
- Want to utilize new uuid7 functionality and deprecate postgres specific uuid4
- Research into updating the docs for implementing raw SQL
    - https://code.djangoproject.com/ticket/36657
- How beneficial would it be to have a newer contributor there?
    - It may also help keep them around
    - There are things that Carlton and Paolo want to do to support others to attend
    - There was at least one attendee who showed up because of the convenient  location
- What is the difference between these sprints and the conference sprints
    - They are extra day long
    - It’s not the end of the conference
    - Newcomers do take up attention and energy and may impact productivity of others
- Daniele Procida mentioned tracking progress and value to attract sponsors
- How do we want to incorporate these sessions into our DEP 10 re-write?
    - We should remove those references from DEP 10 and have it float up the SC in whatever way
