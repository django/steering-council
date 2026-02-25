---
date: 2026-02-16
members:
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
other_attendees:
  - Catherine Holmes
---

## Agenda

- Action items review
- django-tasks future
- Adding formatter for CSS & JS
- Types in Django
- Liaison Discussion

## Action items

- Emma: Draft blog post on 6.x Features
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack 
- Sovereign Tech Fund
      - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
      - Plan another meeting with Lexi once the above is done
- Tim: Iterate on Technical Governance document
      - Pending resolution on decision making
      - Pending Jacob Kaplan-Moss feedback
- Tim: Teams Charters
      - Security Team \- Looking for chair / co-chair
      - Translations \- Need to reach out to Claude
      - T\&R Pending review from team [https://github.com/tim-schilling/dsf-working-groups/pull/6](https://github.com/tim-schilling/dsf-working-groups/pull/6) 
      - Ops \- [Public PR](https://github.com/django/dsf-working-groups/pull/73) pending review from community and Board
      - Releasers \- [Public PR](https://github.com/django/dsf-working-groups/pull/72) pending resolution of mergers team
      - Mergers \- [Public PR](https://github.com/django/dsf-working-groups/pull/71) pending discussion between Tim and Jacob
- Emma: Advance [modern csrf new feature](https://github.com/django/new-features/issues/98), draft DEP
- Frank: Follow-up on security team charter email
- Lily: Follow-up on django.tasks email thread
- Tim: Create new feature issue (put into ‘in progress’)

## Actions review

* On security team, would it work to have Catherine as a facilitator / chair role for the logistics?
  * Would need to be purely administrative and clear instructions
  * Would it work for Frank to officially be the chair, with Catherine as support.
  * Frank to follow-up on email chain

## django.tasks future

* Referencing email from Jake Howard

  *After much git munging, I've extracted the RQ and DB backends into their own packages and repositories, and published them to PyPI:*

* [*https://github.com/RealOrangeOne/django-tasks-db*](https://github.com/RealOrangeOne/django-tasks-db)
* [*https://github.com/RealOrangeOne/django-tasks-rq*](https://github.com/RealOrangeOne/django-tasks-rq)

  *They've also been removed from the original django-tasks repository. I've also wound back the metadata feature. That means django-tasks is now purely a backport of django.tasks suitable for older versions of Django (4.2+), and the DB and RQ backends exist separately, compatible with applications or libraries using either django.tasks or django-tasks.*


  *Hopefully that will help with explanation and understanding of the state of the ecosystem, and how django-tasks fits into it. I've opened a [discussion](https://github.com/RealOrangeOne/django-tasks/discussions/241) on the repository to centralise questions.*


  *I suspect the next steps now are to change the documentation such that django-tasks is referenced in the main Tasks documentation as being a backport, rather than containing additional backends? **If that sounds sensible I can get a ticket up.***


  *My intention is to foster design discussions on the future of django.tasks in the django-tasks repository, and once they're more cemented, open either DEPs for the notable features, or new-feature issues for the smaller ones*.

* Add django-tasks-db, rq packages to our ecosystem page
* Lily: We can reply to Jake with agreement and “let’s go\!”

## Adding formatter for CSS & JS

* [https://forum.djangoproject.com/t/adding-a-formatter-for-css-js/25754/35](https://forum.djangoproject.com/t/adding-a-formatter-for-css-js/25754/35)
* Need to create a new feature issue for it?
* Tom is interested in picking this back up, but doesn’t want to run into a 15 step road block.
* Is this something feasible?
  * Yes this is.
* Tim: Create new feature issue, use in progress column

## Types in Django

* Kraken released a blog post on typing a django project
* Frank talked with Carl from Astral about their typing effort, will try to meet up at PyCon

## Liaison Discussion

* There was a brief discussion about what being a liaison means for a steering council member to a different working group? What does it mean as a board member being a liaison to a different group? Whether or not the group has meetings. Noting that public meeting notes are very helpful when a liaison cannot attend every meeting.
* Potentially Catherine can help some of these groups, note taking, stand in liaison.
* Do some of these groups need training of some kind, including on organization or meeting running?
* Can some of these groups be helped by automation? Automatic meeting note creation, etc. Some messages could be automatically sent. This could go with an integrated slackbot ‘add this to next week’s meeting notes’
* Does the Steering Council need to do some of these automated things?
* Project board makes sense with swim lanes
* Look into private/public boards with issues
