---
date: 2025-10-06
members:
  - Carlton Gibson
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
attendees:
  - Catherine Holmes
  - Natalia Bidart
---

## Agenda

- Team to WG Structure update
- Fellows
    - How is New Features repo going
- Experiments in Django


## Action items

- Tim: Preliminary review of DEP 10 adjustments
- Tim: Open a few third party package docs references in the docs
    - Add mention of django-upgrade to release notes docs 
- Emma: Draft blog post on 6.x Features - still need to setup a meeting with the fellows about that
- Frank: Write blog post about packages eco-system
- All: Start process of reviewing new-features ideas, propose an action and request feedback
- All: Collect preferences for 6.1 release [and now Django on the Med roadmap]
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Check with fellows if billing scheme is ok
    - Plan another meeting with Lexi once the above is done

### Team to WG Structure update

- https://github.com/django/dsf-working-groups/pull/56
- Natalia is working through the security team charter this week
    - Wants to make it clear there are areas people can help the Fellows
    - With the draft proposal, there's been an increase in people proactively responding to messages which is great!

### How is New Features repo going

- There’s difficulty in communicating what’s good for Django community versus Django core
- We may want to have a new features team to help review these things opposed to SC members who have time
    - Could have a office hours recurring call for triage (open to community)
    - Potentially there might be onboarding into the triage and review team.
    - There's value in distinguishing emoji reaction votes from community members
- Need for more visibility of third-party package in the docs
    - Discussion on adding third-party package references to the docs
    - Make the changes one at a time
    - Could we extend the new features repo to include having a pathway for packages to be added to the docs

### Experiments in Django

- Kubernetes has an experimental API that can be used as inspiration
- Suggestion would be to have a `from django._experiments import something`
    - Could be a separate package to be installed
- An underlying goal would be to make upgrades/transitions easier
- We should promote django-upgrade
