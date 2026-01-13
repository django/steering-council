---
date: 2026-01-05
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
  - Tom Carrick
---

## Agenda

- Revisit meeting times
- DEP 17 Content Negotiation
- New Trac triage state
- Annual Release Cycle DEP
- Steering Council Eligibility
- CLA for Django
- Consensus on 6.0 Community Blog Post
- 6.1 new features status
- Merging external packages docs pages
- Django Tasks


## Action Items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively: https://drive.google.com/file/d/1DwDLCsJ13LeYZWA9-zAFBQccF2zpjzkh/view?usp=drive_link
    - Paste - plan publish - communicate with other authors on slack - Emma
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Help with GSoC Working Group governance
    - https://github.com/django/dsf-working-groups/pull/63 
    - Need to follow-up
- Tim: Draft handover documentation for 7.x Steering Council
    - Tim: Follow-up with Thibaud on election process
- Tim: Rework Steering Council eligibility requirements
- Tim: Iterate on Technical Governance document
- Tim: Teams Charters
    - Security Team - Need to settle on roles / responsibilities
    - Translations - Need to reach out to Claude
    - T&R - Need to follow-up
- Tim: Write up message on CLA alignment
- Making a general request asking for mentors
- Frank: Update ecosystem page to create Tasks section, remove from experimental
    - Potentially add wrapper packages to the experimental sections
- Frank: Write up post on things we accomplished last year
- All: Add goals/ideas for 2026 to private thread
- Natalia: Remove external packages page from the docs
- Natalia: Follow-up with Jake on django-tasks



### DEP 17 Content Negotiation

- Farhan has been playing with django-bolt and discovered there’s a much faster parser
- https://github.com/django/new-features/issues/105
- Can we advance this now, rather than waiting? It is pressing at this moment.
    - Carlton replied to Farhan to confirm the scope of the smaller approach. If agreed we will advance to Trac. 
- Agreement to move it forward on the new features repo.

### New Trac triage state

- Want to add needscommunityinput or something similar
- https://forum.djangoproject.com/t/volunteers-wanted-to-update-triage-workflow-docs/37937
- Name will be discussed in slack. Natalia will make proposals to vote on.

### Annual Release Cycle DEP

- Carlton wants to draft an initial version

### Steering Council Eligibility

- Private link to longer iteration of the eligibility requirements
- Tim is looking for feedback for this draft he made.
    - Specifically around the indicators
- Have a focus on making the word choice accessible to non-native english speakers.
- Some members note that they wouldn’t have thought themselves qualified until conversations with community members, so it would be good for it to be clear for future potential applicants.

### CLA For Django

- They are necessary for people working with some corporations
- Likely can’t remove it, but can make it optional and less prominent
- Ideally we’d go through the archives/email inboxes of PDFs to create a new archive
- It is important to make sure that private information stays private, as there is personal information involved.
- Potentially new precedent from Oracle and Google makes this less pressing.
- Some options:
    - Welcome new contributor message
    - PR template
- If it is optional, it needs to be clearly stated either way. Jacob brought up that it sometimes happens that people will avoid actually making a pull request because of “bureaucracy”, even if they have already done the other work.

### Consensus on 6.0 Community Blog Post

- Next Steps: 
    - Create the blog in the admin. 
    - Set a publish time
    - Talk with others in Slack who might be scheduling other blog posts. The goal would be to give each post a few days of prominence when possible.
- Note: We are already halfway to the 6.1 feature freeze! 

### Merging external packages docs pages

- https://forum.djangoproject.com/t/possible-merging-of-2-doc-pages/42819/
- Natalia brought up that there is a page for external packages, and a different new page that the steering council made of recommended third party packages. She thinks that newer users might have confusion.
- The external page that Natalia brought up is very old, and that page can just be removed.
- Can add django-localflavor to the internationalization docs
- Natalia to propose a PR

### Django Tasks

- Need to update the ecosystem page to highlight Tasks section/category
- Ideally we’d link to Django Tasks project
    - There’s concern about naming between Django proper and the django-tasks project
        - Django Tasks Framework?
        - Django Tasks Backend?
    - Does django-tasks have a backend that’s production ready?
    - Natalia to follow up with Jake
