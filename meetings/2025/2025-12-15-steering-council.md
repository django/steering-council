---
date: 2025-12-15
members:
  - Emma Delescolle
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
attendees:
  - Catherine Holmes
---


## Agenda

- Sovereign Tech Fund
- Actions review
- GSoC 2026 project identification
- Versioning scheme change

## Action items

- Emma: Draft blog post on 6.x Features, needs review
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Help with GSoC Working Group governance
    - [https://github.com/django/dsf-working-groups/pull/63](https://github.com/django/dsf-working-groups/pull/63) 
- Tim: Draft handover documentation for 7.x Steering Council
- Tim: Rework Steering Council eligibility requirements
- Tim: Iterate on Technical Governance document
- Tim: Teams Charters
    - Security Team - Need to settle on roles / responsibilities
    - Releasers - Need to generate draft based on feedback
    - Mergers - Need to generate draft based on feedback
    - Ops - Need to generate draft based on feedback
    - Triage & Review - Tim and Lily to follow-up async
    - Translations - Need to reach out to Claude
- Carlton & Tim: Need to invite Tom to meetings and Slack
- Making a general request asking for mentors
- Tim: Coordinate with Bhuvnesh and Apoorv on next steps with GSoC Mentors

### Sovereign Tech Fund

- Some items might have some overlap with GSoC projects, which could affect their timing.
- Is there more community approval needed for the first project (The Admin)? Emma already made a proof of concept.
- The news that the PSF directly received a large grant from the fund changes what was previously the perception of the grant. Jeff Triplett is reaching out to the PSF to understand how this worked and if the DSF could receive this sort of funding. This amount of funding would be massively impactful for the DSF, if it could cover work that is performed by the Fellows. This is just something to keep in mind with projects, not necessarily every project.

### GSoC 2026 project identification

- Review [new features queue](https://github.com/orgs/django/projects/24)
    - Projects (have not been mentioned to proposed mentor):
    - [Ability to customize model Meta & migration generation](https://github.com/django/new-features/issues/73) with shangxiao
    - [Merge Django CORS to core](https://github.com/django/new-features/issues/8) with Adam Johnson
    - [Switch to Playwright tests for integration testing](https://github.com/django/new-features/issues/13) with Tom Carrick
    - [Add ergonomic control over behaviour of missing variables in templates](https://github.com/django/new-features/issues/5) with Lily Foote
        - Lily likely doesn’t have time but would potentially be a co-mentor if time allowed. Tim noted that it was ideal to have two mentors per project.
    - Adding Django Upgrade to Django with Adam Johnson
        - [There’s a forum thread](https://forum.djangoproject.com/t/making-django-upgrade-part-of-deprecation-policy-and-release-cycle/43377)
- Good ideas:
    - [Integrate Environment Variable Management (Inspired by django-environ) into Django Core](https://github.com/django/new-features/issues/61)
    - [Add support for generate_series in postgres](https://github.com/django/new-features/issues/25) - Lily mentioned some abstractions? This may be too small.
        - Simon Charette
        - Sage
        - Lily
    - Auth Improvements
- [One Time Password/Token Generation and Validation](https://github.com/django/new-features/issues/22)
- [Deprecate the current User model for authentication and authorization](https://github.com/django/new-features/issues/4)
- [Auth system improvements](https://github.com/django/new-features/issues/12)
- [A better auth API (row and field level permissions)](https://github.com/django/new-features/issues/17)
- Potential people to ask:
- Carlton
- Andrew Miller
- Emma Delescolle
    - [Creating a plan for adding types to Django](https://github.com/django/new-features/issues/23)
        - [Has easy code contribution steps too?](https://github.com/django/new-features/issues/23#issuecomment-2849283302)
        - Potential people to ask:
            - [Nikita Sobolev](https://github.com/sobolevn), [Marti Raudsepp](https://github.com/intgr)
    - [Experimental Feature flag](https://github.com/django/new-features/issues/3)
        - Tim: This feels like it would require a DEP
        - Lily: We could commit to giving these DEPs an early review / priority
        - Potential people to ask:
            - Florian
            - Andrew Miller
- Good first issues:
    - [Store the cache alias on the cache backend instance](https://github.com/django/new-features/issues/95)
    - [Make advanced ORM functionality more discoverable](https://code.djangoproject.com/ticket/36657)
    - [Document using the ORM in other Python projects](https://github.com/django/new-features/issues/35)

### Versioning Scheme Change
- Do we want to advance this?
    - Not clear yet, should revisit with Carlton again in the future
- Emma: Would really like to see us have a sponsor funded extended long term support version
    - HeroDev offers commercial support for legacy Django
        - Thibaud and Catherine are talking with them
        - Potentially an opportunity for a smaller (10% of their Django business) amount of money but for allegedly very limited work. Exact details aren’t known yet. But this is an option if the Fellows aren’t able to do the work.
- If the Fellows end up being open to supporting old versions, if there is enough compensation to cover their time… how would we communicate with those companies, governments, etc who are likely customers for this? Especially governments and certain corporations may move slowly, that they might want something that is supported for at least 5 years. Smaller companies may be on outdated versions as well.
    - Social media (might reach employees even if not the governments and companies themselves), forms, front page of website, conferences and meetup spreading news.
