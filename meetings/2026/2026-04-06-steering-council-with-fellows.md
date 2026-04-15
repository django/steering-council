---
date: 2026-04-06
members:
  - Carlton Gibson
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
other_attendees:
  - Jacob Walls
---

## Agenda

- CSP support for Media asset objects and CSP support in the admin's script tags
- `EMAIL_PROVIDERS` DEP
- Request for a "noop" attribute on `get_user()`
- Annual release DEP
- New features process

## Action items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Technical Governance document
    - Waiting on DSF board to share plan publicly
- Tim: Teams Charters
    - Security Team - Need to reach out about remaining steps
    - Translations - Need to reach out to Claude
- Frank: Create Github Action for [evaluating initial PRs against checklist](https://github.com/frankwiles/pr-playground)
    - Pending last review/testing from Natalia
    - Some followups can happen later,
        - Exemptions for experienced rule-breakers?
        - Exemptions for typos in scripts
        - [https://forum.djangoproject.com/t/limiting-pr-creation-to-verified-contributors-collaborators/44205](https://forum.djangoproject.com/t/limiting-pr-creation-to-verified-contributors-collaborators/44205/)
- Tim: Re-review CSP thread
- Carlton: Annual release DEP
    - Working on it, should target for a month
- All: Review EMAIL_PROVIDERS DEP	

## CSP Support for Media assets and CSP support in the admin's script tags

- Jacob: keen for 6.1, because it's a bit of a blocker for adopting 6.0 CSP in some projects
- [https://forum.djangoproject.com/t/csp-nonce-support-for-form-media-classes-and-admin-scripts/44698](https://forum.djangoproject.com/t/csp-nonce-support-for-form-media-classes-and-admin-scripts/44698)
- Do we anticipate major disagreement to the template tag approach?
    - If there's a can we do both, we can do that part later

## EMAIL_PROVIDERS DEP

- This needs approval
- [https://github.com/django/deps/pull/105/files](https://github.com/django/deps/pull/105/files)
- This was an accepted ticket already, the DEP was created to centralize the discussions
- Needs review from SC and approval
    - Deadline week after DjangoCon Europe

## Request for a "noop" attribute on `get_user()`

- Jacob redirected to newfeatures, now has confirmation from django-guardian they would use it
- [https://github.com/django/new-features/issues/130](https://github.com/django/new-features/issues/130)
- Will only be used by test client with `force_login`
- Similar to `get_natural_key` with dependencies attribute
- Django-guardian maintainers received it positively
- Lily to move it forward in new features

## Annual release DEP

- This work is continuing
- Carlton is soliciting feedback from Fellows
- Working with Adam Johnson with django-upgrade adoption (separate thing though)

## New features process

- Lily to review through this soon
- Jacob raised a concern about slowing pipeline of new features since the initial leg for 6.2
- If we need a bigger feature, CTE DEP is an option, and composite foreign keys
- Oracle partnership to contribute vector field
