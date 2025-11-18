---
date: 2025-09-01
members:
  - Carlton Gibson
  - Emma Delescolle
  - Lily Foote
  - Tim Schilling
attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
---

## Agenda

- Team to WG Structure update
- Ecosystem page
- Django on the Med
- Our Q4 Season
    - DEP 10
    - Roadmap
- Fellows:
    - General catch up
    - Django 6.0
    - Django 6.1



## Action items

- Tim: Preliminary review of DEP 10 adjustments
- Tim: Create PR to add experimental or similar section to ecosystem page
- Carlton: Add Jacob Walls to meeting invite
- Emma: Draft blog post on 6.x Features
- Frank: Write blog post about packages eco-system
- All: Start process of reviewing new-features ideas, propose an action and request feedback
- All: Collect preferences for 6.1 release [and now Django on the Med roadmap]
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Check with fellows if billing scheme is ok
    - Plan another meeting with Lexi once the above is done


### Team to WG Structure update

- Working on finalizing a new PR with Jeff for the Security team.
- Need to get feedback from SC and Security team next

### Ecosystem page

- Slow progress on PR to add ecosystem page to search
    - https://github.com/django/djangoproject.com/pull/2136 
- Track interest on experimental section discussion in SC Forum section 


### Django on the Med

- We want to hold a “Roadmap Workshop” — to help advance and elaborate key ideas.
    - "What are your hit list items? Can you give some breakdown of that?"
    - Will be asking Thibaud if he’s coming to run a similar roadmap session
    - If Thibaud isn’t there, we’ll ask for a template
    - If Steering Council members have features or ideas to bring up in roadmap discussion
    - Goal is to come out of the sprints with more elaborate documents to help people to work on things


### Our Q4 Season

#### DEP 10

- Start on at sprints of DCUS
- Try to default to yes with oversight

#### Roadmap

- Django on the Med
- Need to revisit our new issues board
    - Lily and Emma are going to meet to discuss things


### Fellows:

#### General catch up

- General warning that both Natalia and Jacob will be at DjangoCon, and Sarah will be away, so only minimum work will be done during that time.

#### Django 6.0

- https://docs.djangoproject.com/en/dev/releases/6.0/ Plus django tasks
- There’s a lot on the Fellows’ plate
    - Feature freeze is coming up
    - The next two weeks has zero Fellow availability outside security and release blockers
- Django Tasks is being reviewed by Fellows
    - Everything else is being pushed
    - Maybe autofield will be reviewed?
- There is flexibility in release dates reminder
- The feature freeze can be done and then the release delayed if needed reminder


#### Django 6.1

- Jacob is the release manager
- Features
    - Async database connection and cursors: https://github.com/django/django/pull/18408
        - May be a good 3rd party package
        - This is a good thread which goes over what is worthwhile to make async and the maintenance challenges we need to juggle with it: https://forum.djangoproject.com/t/is-dep009-async-capable-django-still-relevant/30132/
        - It also references a discussion on the Python forum that we're not alone in finding adding async to a sync-first package challenging: How can async support dispatch between sync and async variants of the same code?
        - Experimental DEP may not be helpful here as it wouldn't allow us to change an API in a .X release cycle
    - Model fetch modes: https://github.com/django/django/pull/17554
        - Django-seal
        - Django-auto-prefetch (other 3rd party package)
        - Mature
    - Database level cascading options: https://github.com/django/django/pull/16851
        - Needs refresh and re-push
    - Moving models between apps: https://github.com/django/django/pull/16905
        - Needs refresh and re-push
- Should try to be more ambitious with the Django on the Med roadmapping to identify next features for 6.1 and 6.2
