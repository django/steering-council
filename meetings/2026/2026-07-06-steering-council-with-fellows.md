---
date: 2026-07-06
members:
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Andy Miller
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
  - Sarah Boyce
---

## Agenda

- Experimental Flags GSoC Project
- Action Items Review
- DEP 19 approval
- Fellows:
  - DEP for table-valued expressions
  - Sphinx theme for the local django docs build
- Oracle Test Pilot discussion recap

## Action items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively: [https://drive.google.com/file/d/1DwDLCsJ13LeYZWA9-zAFBQccF2zpjzkh/view?usp=drive_link](https://drive.google.com/file/d/1DwDLCsJ13LeYZWA9-zAFBQccF2zpjzkh/view?usp=drive_link)  ← still to do
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Teams Charters
    - Security - Add explicit line about board having oversight
    - Translations Team - Need to reach out to Claude
- Carlton: Finalize DEP 20 and prepare for voting
- Write a blog post on Triptych project
- New Features improvements
    - Revisit the language around closing, so we can close things
    - Create a curated view of issues for people to participate in a high-impact area
    - Create new project board views with documentation/blog post with how to participate in new feature process

## Experimental Flags GSoC Project- with Guest Andy Miller

- Discussions:
    - Original with proposed ideas: [https://django-dsf.slack.com/archives/C0871FA52GP/p1769614095013299](https://django-dsf.slack.com/archives/C0871FA52GP/p1769614095013299)
    - April conversation: [https://django-dsf.slack.com/archives/C0871FA52GP/p1777527929921949](https://django-dsf.slack.com/archives/C0871FA52GP/p1777527929921949)
    - June conversation: [https://django-dsf.slack.com/archives/C0871FA52GP/p1780431555624099](https://django-dsf.slack.com/archives/C0871FA52GP/p1780431555624099)
- Our notes: [2026-02-02 Steering Council](https://docs.google.com/document/d/1lZkYfZA7GAGs3td1vj0rG-spwwWjH222TemyPkCNlnE/edit?tab=t.0)
- Has side things around the project for the mentee, but wants to know what Fellows and SC wants
- Natalia thought of this as a research project, not expecting actionable things from the project, but options to pursue later. Natalia gave feedback with this in mind, expecting the project to be exploratory. When major changes to Django were being discussed, Natalia felt like she needed to check in. Her preference is that this project stay research focused.
- Frank agrees with the research aspect of the project. Possibly reconvening and seeing how to go forward after the research is over. What does adding Pluggy to the discussion look like?
- Jacob: from the Forum discussion, he is reading what has been done so far as an argument designed to convince, rather than a whitepaper style, attempting to be more objective pro and con list, which he would like to see.
- Andy was not aware of the research aspect, and thinks this will be helpful to reframe this as exploring many avenues and options. He appreciates the clear expected output, for the research to then be available for others.
- Frank: look at Waffle for reference. Even though they have problems.
- Frank: notes that he thinks contrib has lost its meaning and suggests moving towards retiring the term.

## DEP 19 Approval

- We should approve this to get it on the board's approval for July
- Frank, Tim, Lily are in agreement with it. Need to follow-up async with Carlton and Emma

## Fellows

### Sphinx theme for the local django docs build

- Use a well-known sphinx theme (Furo) for local docs builds?
- This avoids porting our private CSS to the django/django repo
- CSS/theme for the built docs
    - PoC: [https://github.com/nessita/django/pull/53](https://github.com/nessita/django/pull/53)
    - Frank: do whatever is easiest

### Table-valued expressions DEP

- [https://github.com/django/deps/pull/113](https://github.com/django/deps/pull/113)
- Earlier feedback would be helpful for the project
- Should be ready this week
- Lily to take a deeper look
