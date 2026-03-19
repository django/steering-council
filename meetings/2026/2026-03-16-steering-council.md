---
date: 2026-03-16
members:
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
other_attendees:
  - Tom Carrick
---

## Agenda

- DEPs
- DSF & Oracle
- Adding django-manifeststaticfiles-enhanced to ecosystem page
- New features review

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
- All: Review Django Survey for Will Vincent
- Frank: Create Github Action for [evaluating initial PRs against checklist](https://github.com/frankwiles/pr-playground)
- Tim: Follow-up with James and other SC members about [django-manifeststaticfiles-enhanced](https://github.com/blighj/django-manifeststaticfiles-enhanced)

### Action Items Discussion

* Will Vincent is requesting a review for Django Survey 2026
  * Frank has been reviewing this earlier
* Frank is working on a github action to help fellows process PRs. This came out of a DSF office hours meeting
  * [https://github.com/frankwiles/pr-playground](https://github.com/frankwiles/pr-playground)
  * Tim had a few other things to work through, but it shouldn't block anything
  * Natalia had a few small changes to make


## DEPs

* [Support for Common Table Expressions](https://github.com/django/deps/pull/106)
  * Needs an initial review, taking a backseat to email providers
* [Dictionary-based EMAIL\_PROVIDERS](https://github.com/django/deps/pull/105)
  * Lily has reviewed initially, Natalia wanted a SC reviews in by today
  * Frank has reviewed, positive outlook
  * Has mostly been documenting what has been decided
  * On length of DEP
    * This may be helpful to implementers
    * It may have been shorter if we hadn't decided on as much implementation details beforehand
    * Process DEPs should be more readable

## DSF & Oracle

* A meeting occurred with Oracle

## Adding django-manifeststaticfiles-enhanced to ecosystem page

* [https://github.com/blighj/django-manifeststaticfiles-enhanced](https://github.com/blighj/django-manifeststaticfiles-enhanced)
* [Jacob wants to know if we could mention this package in the docs,](https://django-dsf.slack.com/archives/C0871FA52GP/p1773347664613369?thread_ts=1773347132.469789&cid=C0871FA52GP) I suggested this is where the ecosystem page needs to come in.
* This seems like a fit for the exploratory packages
* Check with James if he's using this in production
* Tim, Lily, Frank agree this can be added to the exploratory packages area of ecosystem page
* Tim to follow up with Emma and Carlton on Slack thread

## New features review

* We should try to asynchronously push this forward, but everyone has limited time. May be slow until May-ish
* Lily will try to work on this at sprints during DjangoCon Europe (April)
