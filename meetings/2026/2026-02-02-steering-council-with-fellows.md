---
date: 2026-02-02
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
  - Tom Carrick
---

## Agenda

- Action items review
- FOSDEM
- GSoC Projects
- Fellow Topics
    - Monitoring PRs for “DEP Needed”
    - [Backward compatibility for admin template block composition](https://code.djangoproject.com/ticket/36887#comment:2)
    - Can we advance [django-async-backend for ASGI only](https://github.com/django/new-features/issues/7#issuecomment-3824612657) right now?
- New features review

## Action Items

- Emma: Draft blog post on 6.x Features
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Help with GSoC Working Group governance
    - https://github.com/django/dsf-working-groups/pull/63 
- Tim: Iterate on Technical Governance document
    - Tim: Rework Steering Council eligibility requirements
    - Natalia: Please review qualities vs traits usage in Steering Council Eligibility
    - Blocked by election process from Thibaud
- Tim: Teams Charters
    - Security Team - Need to settle on roles / responsibilities
    - Translations - Need to reach out to Claude
    - T&R - T&R Pending review from team
    - Ops - [Public PR](https://github.com/django/dsf-working-groups/pull/73) pending review from community and Boar
    - Releasers - [Public PR](https://github.com/django/dsf-working-groups/pull/72) pending resolution of mergers team
    - Mergers - [Public PR](https://github.com/django/dsf-working-groups/pull/71) pending discussion between Tim and Jacob
- Frank: Write up post on things we accomplished last year
- Emma: Advance [modern csrf new feature](https://github.com/django/new-features/issues/98), draft DEP
- Carlton: Move new feature 96 (django-staticsite) forward
- Frank: Reach out to Carl Meyer / Astral regarding ty with Django
- Emma: Close new feature 81 due to lack of support
- Tim: Follow-up with Andy Miller and Bhuvnesh about experimental flags GSoC project
- Tim: Follow-up with Bhuvnesh on allowing types in Django GSoC project


### Actions Review

- Django-distill new feature discussion around direction
  - https://github.com/django/new-features/issues/96 
  - Distill is end of life, it was a full re-write to prepare for new package (django-staticsite)
  - Good with adding hooks to support it
      - Need to move this forward on the new-features repo
  - The rest of the functionality would require more discussions due to increased maintenance burden.
      - Should look into what other packages need before advancing a larger solution forward (for example wagtail-bakery)
      - Fellows noted still being currently loaded with security work, so additional duties are difficult.

### FOSDEM

- Emma’s talk went really well!
- Applied for a microgrant via nlnet.nl for admin refactor (django-admin-deux)
    - nlnet.nl does cover (only) research work with grants from 5 to 50K. They might be suitable for preliminary work on both auth and typing
    - Next round of funding for nlnet.nl has a deadline in 1st April (basically every 2 months)
- Sovereign Tech Fund doesn’t do proof of concepts, so we’d need a DEP and a POC
    - Contrary to prior understanding, the German Tech Fund was not represented.
    - The confusion comes from a new entity currently being formed, the European Sovereign Tech Fund (which was very much present)
    - The EU STF is still a work in progress and currently does not have budget, this is the situation for at least several more months (likely 1 year + though) and therefore we should keep an eye out but direct our effort to other existing structure for now
    - The EU STF has a page listing OSS projects and companies who endorse the project. Emma communicated with Tom about that (more of a board decision than an SC one)
    - The one thing the German STF does not cover is "research work", ie: for project work, we need to have a PoC in place
    - There are multiple projects that have been granted several grants by the German STF. AFAIU it is fine as long as there is no overlap between the grants

### GSoC Projects

- https://code.djangoproject.com/wiki/SummerOfCode2026
- Experimental APIs
    - Question from Andy on direction and scope
      > Broadly I think it's starting with definitions, design and documentation of what experimental means for Django both for new features and extending existing features. This will likely end up altering the existing new features process.
We may also have documentation on expectations of design and existing adoption as a package if appropriate?
      > 
      > There is then documentation/policy for when once a experimental features stable.
      > 
      > Ideally we might have a toy/example feature that goes through the process to some degree, or perhaps a small feature that's a good candidate for the process?
      > 
      > Generally I have more ideas as questions than concrete proposals there needs to be a couple of rounds of community feedback baked in as well…
    - The feature flag feature would likely need a DEP
        - Review of other packages that have implemented this
    - The two paths forward are implementing the initial process for experimental and then the new-feature/DEP for feature flags.
- Adding types
    - Relevant aspect maybe? https://github.com/django/new-features/issues/117 
    - Protocol examples from Simon Charette around [Resolvable and Compilable](https://forum.djangoproject.com/t/revisiting-types-in-django-dep-14/37832/11)
        - Could be nicely scoped with clear deliverables
        - This would be an exploratory project to see what this would look like
            - Check on the CI checking
            - Check on scope of documentation
            - Add to django-tasks as a stretch goal?
    - Django tasks had types and were removed from before getting merged
    - Streaming with TaskGroups
        - https://github.com/django/django/pull/19364
    - Astral’s ty typechecking
        - Working on something for Django, we should see what that is and coordinate
        - Carl Meyer would be a great contact for this.
    - On whether we allow typing in Django
        - If this goes forward, Natalia needs to see a plan for how it will progress.
        - Natalia does not want to see a very large number of tiny PRs related to this.
- [Regarding future GSoC projects and getting community buy in to work on them] Need to advance these ideas to discover where people have “no votes”



### Monitoring PRs for “DEP Needed”

- Fellows wonder where to draw the line on to require or not require a DEP
- Potential DEPs:
    - JS lexer: https://github.com/django/django/pull/19561
    - Logical CSS: https://github.com/django/django/pull/17560
        - Tim: Is this going to break 3rd-party packages?
            - Jacob: This gets to my next agenda item!
            - Tom: Admin css is a bit of a moving target, so this isn’t a huge deal
    - Dictionary-based EMAIL providers settings: https://code.djangoproject.com/ticket/35514#comment:24
        - Trying to shift the deprecation path to the same for storages.

### Backward compatibility for admin template block composition

- https://code.djangoproject.com/ticket/36887#comment:2
- Backwards compatibility is a best effort, if we have a good reason we can cause it.

### Can we advance django-async-backend for ASGI only right now?
- https://github.com/django/new-features/issues/7#issuecomment-3824612657
- Contributor has questions about the "single event loop" proposal for multiple async_to_sync calls under WSGI
- This is a someday maybe yet
    - Free threading in python is coming in 3.15
- If a person needs both, use a SyncWorker and then an AsyncWorker with a reverse proxy to distribute between the two


### New features review
- https://github.com/django/new-features/issues/81
- Should we close this since the requestor is not interested in discussing?
    - Yes
