---
date: 2025-12-01
members:
  - Carlton Gibson
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
---

## Agenda

- DEP 10 Revisions
- Google Summer of Code (GSoC) 2026
- Security topics
    - Low quality HackerOne reports
    - GitHub Security Advisories
- Translations for Django

## Action Items

- Emma: Draft blog post on 6.x Features - still need to setup a meeting with the fellows about that
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Facilitate discussion amongst Security Team about progressing https://github.com/django/dsf-working-groups/pull/56 
- Tim: Help with GSoC Working Group governance
- Tim: Draft handover documentation for 7.x Steering Council
- All: Review new features repo on Dec 15 for GSoC opportunities


### DEP 10 Revisions

- Shared with the Board
- Thibaud provided some good questions:
    - Do we want to formalize a Roadmap?
        - Is this part of the DEP?
        - A roadmap is pretty unknown at this point which makes it difficult to commit to
        - Wagtail has a great roadmap
            - Has paid development efforts which makes it easier to predict
            - Makes it easy to sponsor efforts
        - Roadmap would be dependent on who the audience is
        - 6.1 has several features identified because the PRs were progressing and seemed likely to make it in or already had
        - Tim relay that we’re going to punt on this and/or this is part of a multi-team effort
    - Adjustments to the eligibility requirements
        - Tim is going to revise these based on Thibaud’s feedback
            - Try to highlight trait, have 2-3 sentences and then have the examples
            - Potentially there is nothing wrong and trusting the community to vote for the right people.  Potentially with the example of needing a CoC exclusion. Potentially ‘all DSF members are eligible unless under an active CoC ban.’
        - Need to mention that we want a mix of experiences. Potentially attempting to ensure continent representation. Potential ideas: 
            - Ensured seats for Geographical diversity? (Advisory role?) 
            - Ensured (e.g. 2?) “technical seats”?
    - Adjustments to the election process to be less rigid
        - Do we want to move the election process out entirely?
            - Tim will explore options here with Thibaud
        - Noted that multiple people expressed interest in helping applicants strengthen their personal statements.


### Security Reports

#### Low quality HackerOne Reports

- There are many low quality HackerOne security reports which take up a lot of time.
- Curl library is dealing with something similar, 142 HackerOne submissions, only 8 valid reports
- HackerOne is a historic source of lower quality reports
- A proposal has been made to remove HackerOne as a source
- Have we reached out to HackerOne?
    - Not sure we have (Catherine- the board has recently become aware, and no one has reached out yet.)
    - (Catherine) Thibaud believes dropping them is correct. The rest of the board has had access to the conversation, but not necessarily seen it.
- The Steering Council supports dropping Hacker One
    - If the rest of the security identifies a concern, please relay to the Steering Council
    
#### GitHub Security Advisories

- The Security Team will be switching to GitHub Security advisories for tracking, but will use own tools for artifacts and releases

### Google Summer of Code 2026

- Bhuvnesh and Apoorv were admins last year
    - Tim confirmed with them on Discord they're interested again
    - They are open to chairing/co-chairing a working group
    - Tim offered help with the governance piece
- Challenge last year was identifying mentors and projects
    - We need to help identify mentors for projects.
    - Should have two mentors per project
    - Need to be clear about what the end goals are for new features (likely third-party package)
- From history: It’s important there’s one person who knows they are responsible for ticking off the TODOs at the given dates. (It’s not hard per se BUT it can’t be forgotten)
- Put out a call for mentors
- Review new features repo in next meeting for agreed upon / well defined ideas
    - Reach out to people who could be mentors
    - django new management command (start project) DEP is a strong candidate

### Translations for Django

- Transifex has a few thousand open requests (1925 open requests)
- There’s some documentation referencing the role, but not docs about the role
- Claude would likely help with defining a team charter
    - The Charter should identify the resources, processes and be just enough to empower people to do things
