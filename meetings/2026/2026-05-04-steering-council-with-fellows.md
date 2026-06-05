---
date: 2026-05-04
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
  - Sarah Boyce
---

## Agenda

- Logical properties and values in CSS
- Accessibility team leeway on code improvements
- DEP 20: Annual Release Process ([link](https://github.com/django/deps/pull/109))
- DEP 19: New technical governance ([link](https://github.com/django/deps/pull/107))
- DEP 18: Email providers ([link](https://github.com/django/deps/pull/105))
- Google Summer of Code

## Action items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Technical Governance document
- Tim: Teams Charters
    - Security - Transitioning last open items to team discussions
    - Translations Team - Need to reach out to Claude
- Carlton: Annual release DEP
- Review DEP 18 by end of week

## Logical properties and values in CSS

- [New features](https://github.com/django/new-features/issues/148), requested by Accessibility team
- Regarding gritQL
    - Was there a discussion on this, why this in particular?
        - Can ask on new-features to ask for clarification on justification
- Seems like a positive
    - Concerns around backwards compatibility where we change the definitions of styles (Customisations)
        - Would require heads up and ideally we don't do this, but the admin is an exception to the backwards compatibility policy
    - It'll be helpful to mention this early on in a blog post that this is happening, who will be impacted, what expect things.

## Accessibility team leeway on code improvements

- They are discussing linting rules and the GritQL rules, but are spending time on "how do we do this from a process" perspective. Feels like we're letting processes get in the way of people doing positive work.
- Natalia wants to assure accountability. That there will be support there.
- The team doesn't have the capacity to be a required aspect of the whole contribution process. The team does not want to be a blocker, which was information that came from within the accessibility team.
- This is part of the volunteer nature. Sarah brings up the 'wave' nature of this. People surge in involvement, and then disappear, which is natural in volunteering. It can be a problem if Accessibility team review is required or strongly desired.

## DEP 20: Annual release process

- Discussion has been both positive and constructive
- A few decision points to settle. How many versions of Python to support:
    - Green only vs Plus last yellow Python support
        - Carlton: I genuinely don't know which way is best here. Leaned to Plus Last Yellow because of e.g. Linux distributions.
        - There is the [deadsnakes PPA for ubuntu](https://launchpad.net/~deadsnakes) which provides all versions of python as .deb packages
        - General sentiment is that "Green Only (whilst appealing) is too aggressive".
    - Version numbering
        - We WON'T all agree on this (everyone has a favourite)
        - But we CAN all live with any option we choose.
        - "What colour?"
        - YYYY vs YY v N
            - CalVer or Like-SemVar
        - Discussion wasn't conclusive, as predicted ☺️

## DEP 19: New technical governance

- Document structure: Do we need to move the final place to this into the docs as the source of truth to allow incremental updates?
    - [https://github.com/django/deps/pull/107#discussion_r3104952597](https://github.com/django/deps/pull/107#discussion_r3104952597)
    - [https://docs.djangoproject.com/en/6.0/internals/organization](https://docs.djangoproject.com/en/6.0/internals/organization)
    - Right now, docs would work well.
        - [https://docs.djangoproject.com/en/6.0/internals/organization/#:~:text=governance%20of%20other%20technical%20teams%20within%20the%20Django](https://docs.djangoproject.com/en/6.0/internals/organization/#:~:text=governance%20of%20other%20technical%20teams%20within%20the%20Django)
- Transparency in decision making process
    - [https://github.com/django/deps/pull/107#discussion_r3142528926](https://github.com/django/deps/pull/107#discussion_r3142528926)

## DEP 18: Email providers

- The PR is ready to merge
- Natalia: Mike has been doing stellar work

## Google Summer of Code

- All four project proposals were accepted!
