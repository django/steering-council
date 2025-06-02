---
date: 2025-05-26
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
attendees:
  - Catherine Holmes
  - Natalia Bidart
---

## Agenda

- Community page update
- Team to WG transition update
- Fellows:
    - Headline features
    - Async related: Middleware modernization
    - Request for Vote: Admin Keyboard Shortcuts and Command Palette - Django Internals
- Feature review process
- Lilian Tran’s improvements to the contributor workflow
- Sprint Ideas for Django on the Med? ��️


## Action items

- SC: Review DSF 2024 annual report excerpt
- Frank making 2025-04-14’s notes ready to share with the public.
- Frank: Add Baptiste as a reviewer on djangoproject.com PR 2060
- Emma: Draft blog post on 6.x Features
- Carlton to create a new ticket for a new column and close the others for issues 4 and 12
- Tim: Rework security team WG PR


### Community page update

- PR: https://github.com/django/djangoproject.com/pull/2060 
- Issue: https://github.com/django/djangoproject.com/issues/1909 
- We want to add third party documentation
    - Cdrf classy django rest framework
    - Ccbv
    - Django girls tutorial and website
- Ask Baptiste to take a look at change for the website
- The steering council is taking ownership of maintenance in the medium and long term
- We need to start preparing for the next steering council on transition information


### Team to WG transition update

- Security team is next, Tim needs to revamp Rob’s initial suggestion for a next review
- The intention is not to expand the purview of the security team, but to get it formalized.


### Fellows discussion

#### Headline features

- It's understood these are all just preferences and not demands
- Django-csp
    - The admin may not be compliant with csp
    - There’s some unfinished work to make this work, specific to GeoDjango
    - There’s a branch to remove the inline JS
- Django tasks
    - This is the next priority
- Django async
    - May slip depending on priorities and availability
    - Capacity may be a problem here

#### Async middleware modernization

- All the existing middlewares use the old style
- Should we start moving the middlewares to the new style?

#### Admin Keyboard Shortcuts and Command Palette

- There’s a question about maintainability for javascript when Fellows don’t feel like Javascript is something they are experts at
    - The junit tests we have feel a bit clunky
    - Playwright may help, but converting would take lot of work
    - Are we going to accept the risk of adding JS to the library despite a potential lack of expertise with it?
    - Do we need to ask what’s do-able in core vs as a third-party package? 
- Do they need to create a DEP for the shortcuts and command palette?
    - This has effectively been started
- We’re going to need a marketing strategy for the django-tasks db backend already, so we could practice here
    - We could use pip extras here django[db-tasks]
- The feature could be the ability to easily make these shortcuts, and what they are will need to be defined in the DEP.


### Feature review process

- We need to set up a time to review things
- Could use a bit more clarity around which items we’re discussing and moving around
- ORM standalone
    - Could be marked as docs where we will accept more how-to documentation
    - Note that we would be open to optimizations

### Improvements to contributor workflow

- https://ontowhee.github.io/2025/05/19/searching-django-contributor-activities.html 
- https://www.youtube.com/watch?v=NaHzmw31aoA 
- What can we do to support Lilian with this?
    - Any integrations with Trac, but we’re not sure. Baptiste is the person who will know


### Django on the Med

- Twice a year
- Can we add a focus for those sprints?
- Looking for a breakfast sponsor
