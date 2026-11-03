---
date: 2026-11-02
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Tom Carrick
---

## Agenda

- Fellows
- sqlparse announcement
- DEP exposure via Forum threads
- GSoC Ideas
- Remaining SC Goals/Focuses

## Action items

- Sovereign Tech Agency
    - ~~Tim and Jacob met with Mirko~~
- Tim: Teams Charters
    - [https://github.com/django/dsf-working-groups/pull/98](https://github.com/django/dsf-working-groups/pull/98)
- ~~Tim: Post quarterly outreach message~~
- ~~Tim: Comment on memcached clients~~
- New Features improvements
    - Revisit the language around closing, so we can close things
    - Create a curated view of issues for people to participate in a high-impact area
    - Create new project board views with documentation/blog post with how to participate in new feature process
- Jacob: Review Translators Charter
- Carlton: Posting to the maintainer’s sqlparse forum thread
- Tim: Tag new feature historical tag for the extracting the ORM for historical context
- Tim: Follow up with Jonathon about the forum links on the DEPs

## Fellows

- Feature freeze is mid-January
- Carlton will work with Caleb to complete the async transactions PR before the feature freeze.
- CompositeField: Some plans from Jacob around reducing complexity.

## sqlparse announcement

- [https://forum.djangoproject.com/t/sqlparse-is-no-longer-maintained-implications-for-django/46346](https://forum.djangoproject.com/t/sqlparse-is-no-longer-maintained-implications-for-django/46346)
- This is a package the maintainer is not planning to maintain anymore, and also is not planning to transfer to someone else.
- sqlparse is only used in the test runner –debug-sql flag, not even when `DEBUG=True`
    - Has nearly caused performance/security issues with Django
    - Also used in test runner and inspectdb
- Options:
    - Are there alternatives?
    - We can likely retain this for a while, because it just had a release.
    - Frank identified [a rust crate](https://crates.io/crates/sqlparser/0.53.0) we could wrap
    - Could fall back on unformatted sql?    - Could we ask if there is a community member who has the bandwidth to maintain it?
        - Is it worth turning it over to the Fellows?
        - There is no Django Commons issue.
        - Is it worth reframing with the maintainer and seeing if they could keep it? There was some pushback on that idea.
        - It would mean forking it and starting from there, because the maintainer does not intend to transfer it.
    - We could make clear that this is for users who accept the security risk only.
        - Review the security boundary for what’ll be accepted.
        - It’s NOT for untrusted code. RunSQL, inspectdb, debug SQL only — Doesn’t have to be 100% bulletproof
    - It’s worth making a thread for the community- deciding that it would be best to use the author’s thread, in case the author wants to contribute.

## DEP exposure via Forum threads

- [https://forum.djangoproject.com/t/where-is-the-dep-discussion/46183](https://forum.djangoproject.com/t/where-is-the-dep-discussion/46183)
- [https://github.com/django/deps/issues/125](https://github.com/django/deps/issues/125)
- [https://github.com/django/deps/pull/126](https://github.com/django/deps/pull/126)
- A user posted saying that these discussions are supposed to be part of a DEP.
- The goal would be for the SC to read and give the user clarity.
- We want to avoid splitting discussion and not getting enough on the PR
- We should include the new DEPs on the quarterly announcements
- Can we automate this if we’re just relaying this to the forum?
    - Yes, Andy Miller and Online Community WG is suggesting
    - The other thread can be locked on GitHub or the Forum
- Do we want to make an intermediate change or wait on the OCWG?
    - Tim to follow up with Jonathon

## GSoC Ideas

- [GSoC 2027 ideas](https://docs.google.com/spreadsheets/d/1kpA4l1x81dYDA-TQ4NPdTBPDBzhufyWUaCCPce6Gb1c/edit?usp=drive_link)
- At some point when people seem done submitting and SC council members have had time to review, the SC needs to vet them and see if they are worth a summer focusing on.
- Emma: What is the status of DEP 17? Carlton says that if it’s an issue that has existed for years, it is probably not a good GSoC project, because if it was easy, it would have been done years ago.

## Remaining SC Goals/Focuses

- Tim’s:
    - Facilitating new feature flow
    - Supporting SC election process
    - Supporting the transition to the new SC
- What else are other SC members interested in?
- Since DjangoCon Europe is early next year, could there be a workshop for encouraging interested members to learn about joining the Steering Council?
    - Could ask other former SC / Technical board members
    - Could include board members
        - The board election is soon, but may be delayed
    - Could ask Team or WG chairs
- Lily to continue to shepherd the Django on the Med work
    - One may require a deprecation
        - On Jacob’s radar
- Emma: Should we formalize the new feature flow
    - Tim: What would be involved in this?
    - Emma: Some kind of announcement would be the minimum step
- Emma: We should have dedicated pages for DEPs and new features
    - Andy has a DEP static site [https://github.com/django/deps/pull/112](https://github.com/django/deps/pull/112), [https://tranquil-pavlova-402378.netlify.app/](https://tranquil-pavlova-402378.netlify.app/)
    - Tim made an attempt: [https://github.com/tim-schilling/new-features-dashboard](https://github.com/tim-schilling/new-features-dashboard), [https://tim-schilling.github.io/new-features-dashboard/](https://tim-schilling.github.io/new-features-dashboard/?state=open&sort=total_reactions%3Adesc)
    - Carlton: For most community members, we need to highlight which ones they should focus on. There’s a lot of content there and it’s overwhelming for a new person. We can lean on the quarterly contributor outreach messages.
