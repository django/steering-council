---
date: 2026-03-02
members:
  - Emma Delescolle
  - Frank Wiles
  - Lily Acorn
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
---

## Agenda

- Liaison roles
- DSF and Oracle
- Security team policy changes
  - Supporting email submissions
  - Switching to GHSA, Curl is [reverting back to HackerOne](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/)
- DEPs
  - Support for Common Table Expressions
  - Dictionary-based EMAIL_PROVIDERS

## Action items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively
      - Paste - plan publish - communicate with other authors on slack - Emma
      - Share on #marketing channel in Slack
- Sovereign Tech Fund
      - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
      - Plan another meeting with Lexi once the above is done
- Tim: Technical Governance document
      - Check with DSF board if they are asking for public comment
      - Create plan to adopt new governance
      - Share publicly with plan
- Tim: Teams Charters
      - Security Team \- Looking for chair / co-chair
      - Translations \- Need to reach out to Claude
      - T&R Pending review from team [https://github.com/tim-schilling/dsf-working-groups/pull/6](https://github.com/tim-schilling/dsf-working-groups/pull/6)
      - Ops \- [Public PR](https://github.com/django/dsf-working-groups/pull/73) pending review from community and Board
      - Releasers \- [Public PR](https://github.com/django/dsf-working-groups/pull/72) - request board approval
      - Mergers \- [Public PR](https://github.com/django/dsf-working-groups/pull/71) - request board approval

### Action Items Discussion

* Tech governance, pending Emma and Frank
  * There's an open concern around the vote of no confidence
    * Are we prepared to handle this?
    * Bring this up with the board
    * We can include this on the plan as an open question to the community.
* Security team
  * There are pros and cons of having a chair who is not a Fellow.
    * Currently, Fellows are at capacity, however Natalia believes that they will have a little more time soon with Sarah returning from leave.
    * Discussion of what the rolls of a chair are inside and outside of the meeting.
    * Outside of the meeting, Tim thinks most tasks will fall more on the Fellows.
    * Discussion of how often meetings should happen. Natalia has been attempting to organize a month meeting, because async seems to be a struggle. Frank questions if this is an issue that meetings would help with.
  * Start with Natalia as chair for the next year. Frank would be there as a liaison. Catherine available to help as needed.

## Liaison roles

* What are the expectations for this?
  * Visibility?
  * Supporting the teams?
* What teams/WG do we need visibility on?
  * Accessibility
  * Website WG
  * Marketing
  * Releasers
  * Mergers
  * Triage and Review
  * Security
* What are our priorities?
* Scope
  * Read minutes
  * Be member on async channel
    * Can set expectations around ignoring the channel and tell people to ping me when I'm needed
  * Attend a meeting once a quarter/6mos
  * Be available as called / available
* Which teams have async communication
  * T&R - Discord
  * Accessibility - Discord
  * Ops - Discord
  * Website - Slack and Discord
  * Online communities - Discord
  * Fellows - Slack
  * CoC - Slack
  * Mergers & Releasers - Slack Group DM
  * Security - Email only for now, pending charter
* Do we want to try this with an understanding we are trying to know if it's sustainable for the future?

## DSF & Oracle

* See email from Jeff.
* DSF Point of contact
* 3 week reviews
* Vector Fields and Oracle Backend
* Database Provider fundraising
* Are we okay with these asks so the board can move forward with?
  * Yes, Tim to follow up on email

## Security team policy changes

* Supporting email submissions
  * Not necessarily changing, brought up as a topic
  * GitHub prevents people from actively contributing, so we should retain a non-GitHub option
  * Could create form option to allow a person to submit something
    * Frank to follow-up with this
* Switching to GHSA, Curl is [reverting back to HackerOne](https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/)
  * Primary concern is shared board for security issues which GHSA supports
  * Constraints:
    * CI doesn't run for private reports for GHSA
  * Django Security Team is entirely on GitHub, isn't entirely present on HackerOne
  * The board has already started us on the path to leave HackerOne

## DEPs

* [Support for Common Table Expressions](https://github.com/django/deps/pull/106)
  * Needs an initial review
* [Dictionary-based EMAIL_PROVIDERS](https://github.com/django/deps/pull/105)
  * Needs feedback around specific cases on deprecation paths
  * Ideally want to get this in for 6.1 (May 17th)
  * Natalia would like a SC member to read and look for red flags in next couple weeks
