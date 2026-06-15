---
date: 2026-06-15
members:
  - Carlton Gibson
  - Frank Wiles
  - Tim Schilling
---

## Agenda

- Triptych Project
- Technical governance doc open questions
- New features repo

## Action items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Technical Governance document
    - Tim: Follow-up on Shai's comments on PR
- Tim: Teams Charters
    - Security - Transitioning last open items to team discussions
    - Translations Team - Need to reach out to Claude
- Carlton: Finalize DEP 20 and prepare for voting
- Write a blog post on Triptych project
- New Features improvements
    - Revisit the language around closing, so we can close things
    - Create a curated view of issues for people to participate in a high-impact area
    - Create new project board views with documentation/blog post with how to participate in new feature process

## Triptych Project

- Carlton highlighted this project from Carson Gross (HTMX), and proposed we sign a Letter of Collaboration with them
- [https://triptychproject.org/](https://triptychproject.org/)
- Tim: The third proposal is still in progress and hasn't been completed yet. The alternatives section is what's not complete.
- Carson will have a draft of a document for us to fill out
- Requires us to formalize
- We should write a blog post about why this is a benefit to the community
    - Add action items at the end to help bring other communities into it, like Flask

## Technical governance document open questions

- [https://github.com/django/deps/pull/107#discussion_r3104908486](https://github.com/django/deps/pull/107#discussion_r3104908486)
    - The professional skills are private and difficult to verify as a voter
    - These are meant to be for the DSF board to evaluate to determine if someone can stand for election. Not necessarily for voters to vote on.
    - These examples are just indications and are not a complete list of possible ways to show evidence. The indicator is possible evidence of the quality, not the quality itself.
- [https://github.com/django/deps/pull/107#discussion_r3104955516](https://github.com/django/deps/pull/107#discussion_r3104955516)
    - This is just explicitly mentioning an existing power of the CoC WG
    - We could remove this
        - This is in the rationale section, explaining why we're removing the limitation on processing DEPs during elections. It wouldn't be in the constitution.
    - There's value in stating that the SC is subject to CoC WG and and Board, but we want to avoid over-engineering a social structure
- Tim to finalize the DEP, we'll advance it when Lily and Emma review
- DSF Board will next meet in July to vote on it

## New Features Repo

- What can we do to improve this process?
    - We can't see the serious considerations that need opinions
    - Should we close ideas?
    - Frank: C++ alliance is in charge of Boost, well funded and experimenting
        - Using several agents to review each papers to provide early feedback without requiring a contributor to do that effort
        - Can we use AI to auto-tag and auto-review, identify severity
    - We should create embeddings and relationships between issues
    - We have two roles for this processing the queue
        - An earlier triager
        - An curator
    - How do we triage issues and provide critical feedback, without receiving negative feedback about that criticism?
    - Could use a round-robin approach to designate issues to specific people to dilute feedback
    - The phrase "This would be detrimental to Django" is a really high bar
        - We could reduce this, but it's a beneficial one.
    - We could add a new user interface wrapping GitHub APIs
        - Andy Miller has been doing work around this for DEPs
        - We want to highlight who has all voted
        - We want to identify who has contributed to Django, who is a DSF individual member
        - New functionality:
            - Auth
            - Increase vote options a bit more.
            - Add some metadata to the issues, as a summary of issues
    - We could encourage people to fill things out
        - Akin to Trey's whereabouts Earth game
    - Next steps:
        - Revisit the language around closing, so we can close things
        - Create a curated view of issues for people to participate in a high-impact area
        - Create new project board views
            - Add to documentation/blog post with how to participate in new feature process
