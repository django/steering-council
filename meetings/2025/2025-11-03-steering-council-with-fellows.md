---
date: 2025-11-03
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Acorn
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
---

## Agenda

- Todo review
- New Admin
- Annual Release Cycle
- Request a DEP for django-upgrade
- Review of initial DEP 10 revision suggestions
- Security Team charter/PR

## Action Items

- Emma: Draft blog post on 6.x Features - still need to setup a meeting with the fellows about that
    - Reach out to Rob Hudson, Mike Edmunds, Calvin Vu
- Frank: Write blog post about packages eco-system (Do on own blog given recent dp.com post.) 
- All: Collect preferences for 6.1 release
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Carlton: Ask Adam to prepare DEP for django-upgrade as part of the release process. targeting 6.2 (6.1?) 

### Blog Posts

- There's a nice DSF post on the Django ecosystem
- Frank's packages eco-system post will be converted to a personal blog post and link to the DSF entry
- Emma is continuing to work on the 6.x feature post
    - Several people could be mentioned
    - Rob Hudson (django-csp), Mike Edmunds (django-anymail), Calvin Vu (Postgres search lexemes that was merged in)

### 6.1 Features

- Async db cursors: a whole repo, well advanced, third party package
- We have enough for a release already.
- Keep curating the Roadmap etc
- BUT most things are “as they come” rather than “needed for the next release”.

### Sovereign Tech Fund

- Need big projects. Potentially a project being adding a new admin, based on plugins to add features.
- Likely starting as a third party package and then potentially integrating into a release
- Adding Type annotations is a potential project Jacob Walls has suggested. Multiple projects can be applied for.
- The challenge is that for each idea, there needs to be a champion to talk to the fund. Lexi would potentially write multiple proposals, trying to get multiple accepted.

### Django and CalVer

- Carlton wrote a blog post about potentially moving to an annual release cycle that would include stopping support for past versions on a schedule, making every version three years of support.
    - Is the more aggressive “Green Python” approach something we can lean towards? More exciting certainly.
- “Extended support” (beyond LTS) is something we might charge for. Python versions and Security Patches.
    - The amount of money to be charged would need to be discussed.

### DEP 10 Revisions

- Current set of iterations look good, can continue with a new DEP
- “Default to Go, with brakes” not the other way round

### Security Team Charter
- Will continue. In SecTeam likely. Then back to PR.
