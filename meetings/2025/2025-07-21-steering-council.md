---
date: 2025-07-21
members:
  - Emma Delescolle
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Kaplan-Moss
---

## Agenda

- New features process
- 6.1 release features
- Highlighting ecosystem page


## Action items

- Emma: Draft blog post on 6.x Features
- Carlton to create a new ticket for a new column and close the others for issues 4 and 12
- Tim: Rework security team WG PR
- Tim: DjangoCon Africa talk
- Tim: Reach out to Akash about database cascades
- Tim: Reach out to Baptiste about search on djangoproject.com with elasticsearch
- Frank: Write blog post about packages eco-system
- All: Start process of reviewing new-features ideas, propose an action and request feedback
- All: Collect preferences for 6.1 release
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Check with fellows if billing scheme is ok
    - Plan another meeting with Lexi once the above is done


### New features process

- Concerns about some features are being recreated on the forum
- Need to regularly check in and remove issues with too many thumbs down and move on with enough thumbs up.
- Before moving something to the second column, what is needed first, or what is needed after the move?
- Can create a separate channel or use the forum to identify the various issues that are being proposed to move, along with the text being sent. People can reply in thread and vote / comment approval.

### 6.1 release features
- Two ideas are Start Project command and project template DEP
- Emma wants to sit down with the fellows ~15min to talk about 6.x and blog post
- Composite Primary Keys continued:
    - https://github.com/django/django/pull/18863
    - https://github.com/django/django/pull/18865
    - https://github.com/django/django/pull/18868
    - Original author may not have time to continue, need to check with Csirmazbendeguz
- Database level cascades: https://github.com/django/django/pull/16851
    - Original author may not have time to continue, need to check with Akash
- Move model between apps
    - Would like to have a set of formal guidelines to help others. (“better story than three janky migrations”)
- Social media/blog post could be a good tool for this for those who don’t have specific individuals in mind
- Are there any new features that could get merged in for 6.1?
    - Check for items that have been pushed back to new features for discussion.

### Highlighting ecosystem page

- Mentioned in docs as of https://github.com/django/django/pull/19635 
- It’s currently not searchable.
    - This is difficult to implement because all the content is served differently
    - If it’s elastic search, we should be able to inject whatever content we want to
    - Need to ask Baptiste about elastic search
- Does the Website WG have a roadmap and or looking for areas of focus?
    - Can share the benefits of updating search to work with other pages with Website WG
    - There are other topics that aren’t searchable, which causes difficulty.
- A conversation about adding docs topics
    - There are topics that should be mentioned in the docs, but aren't
    - Daniele Procida may have suggestions on things to change for a larger docs overhaul
    - For example, the documentation doesn't mention REST and GraphQL
