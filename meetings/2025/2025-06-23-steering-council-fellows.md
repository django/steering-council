---
date: 2025-06-23
members:
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
attendees:
  - Catherine Holmes
  - Natalia Bidart
  - Sarah Boyce
---

## Agenda

- Community page update
- Team to WG transition update
- Fellows:
    - Upcoming absences
    - Admin keyboard shortcuts and Javascript
    - New meeting time option
- Moving more to asynchronous discussions

## Action items

- Emma: Draft blog post on 6.x Features
- Carlton to create a new ticket for a new column and close the others for issues 4 and 12
- Tim: Rework security team WG PR
- Frank: Write blog post about packages eco-system
- Frank: Create issue for icon on light theme
- Sovereign Tech Fund
    - Get one or more project(s) ready
    - Check with fellows if billing scheme is ok
    - Plan another meeting with Lexi once the above is done
- Tim: Relay the how to guide on how to achieve keyboard shortcuts, can reference third party package to integrate it
- Tim: Arrange meeting with Accessibility team and Fellows, cc steering council
- Tim: Coordinate with Carlton to move Fellows to the earlier meeting

### Community page update

- PR: https://github.com/django/djangoproject.com/pull/2060 
- Issue: https://github.com/django/djangoproject.com/issues/1909 
- PR was merged and deployed
- https://www.djangoproject.com/community/ third party packages
- Need a blog post
- Need to fix the icon on light mode

### Team to WG transition update

- No update

### Fellows discussion

#### Upcoming absences

- Sarah and Natalia both have absences and communicated it to the Steering Council

#### Admin keyboard shortcuts and Javascript

- https://github.com/django/django/pull/19579
- https://forum.djangoproject.com/t/request-for-vote-admin-keyboard-shortcuts-and-command-palette/41037
- Fellows prefer this to be a third party app, not initially added to django core, at least at first.
- Proposed code lacks tests and is still going through consideration.
- Any change would require tests and consideration.
- Possible middle ground of it being a highly visible third party by putting it in the default options and it would have to be opted out of.
- Possibly it can also be put in the docs.
- Possibly could be a customized method where the hooks are in place but the shortcuts change.
- Next step is for Tim to coordinate discussion between Fellows and Accessibility team

#### New meeting time option

- Fellows will be joining the alternative meeting time


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


### Moving more to asynchronous discussions

- This is prompted by schedule conflicts innate in having a global board in different timezones.
- Need a way to have a way to remind people about things and solicit feedback
- Could have the way for someone to share that they are 0 or “indifferent” and let others make choices
- Need to come to an agreement that it’s okay to remind each other
