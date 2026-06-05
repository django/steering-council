---
date: 2026-06-01
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Jacob Walls
  - Natalia Bidart
---

## Agenda

- Action items review
-
- DEP 18 approval
- Fellows:
    - AI slop way down after GSoC application season
    - Discussion about PR quality bot auto-close behavior
    - DEP for table-valued expressions (GSoC)
    - Async model instantiation (because setting a GFK touches the db)
    - Moving models between apps ([PR](https://github.com/django/django/pull/16905))
    - Oracle test pilot ([forum](https://forum.djangoproject.com/t/proposal-leverage-oracle-test-pilot-for-django-ci/45197))
    - Redistributing licenses when ingesting community packages
- Advertising on [djangoproject.com](http://djangoproject.com)
- PyCon US recap

## Action items

- Emma: Draft blog post on 6.x Features: Rob is the only one who answered positively
    - Paste - plan publish - communicate with other authors on slack - Emma
    - Share on #marketing channel in Slack
- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Technical Governance document
- Tim: Teams Charters
    - Security - Transitioning last open items to team discussions
    - Translations Team - Need to reach out to Claude
- Tim: Follow up on Oracle thread

## Actions Review

- Tim: Need to revisit tech governance forum thread
- Security charter
    - Sarah Boyce merged several changes
    - We want to wrap this up and merge it
    - Jacob to follow up with Sarah to transition last open items
    - Frank is still pending joining the security list

## DEP 18 (MAILERS setting)

- [https://github.com/django/deps/pull/111](https://github.com/django/deps/pull/111)
- Need to post consensus on the DEP

## AI Slop

- This appears to be related to GSoC application window
- The PR auto-closing tool is helping as well
    - We're getting people caught by the PR being auto closed because the Trac "Has Ticket" isn't set
    - The auto-closer may need a little help
        - Could re-run the checker on the PR to re-open the PR
        - Step 3 description is invalid for what we actually want to happen
    - We should improve messaging about remediation step
    - Ideally the bot would auto-reopen if issues are fixed. This would require switching to a bot approach.
- Tim: Will follow up with GSoC WG on applicants and how many PRs they opened

## DEP Table-valued expressions

- [Early draft](https://github.com/p-r-a-v-i-n/deps/blob/relation-api/draft/table_value_expression.rst)
- Jacob has solicited feedback from ORM contributors and helped Pravin to create a draft
- Pravin should be creating a public DEP PR soon

## Async model instantiation

- Use case: acreate() delegating to asave(), see [ticket](https://code.djangoproject.com/ticket/36888#comment:11)
- Maybe a DEP?
- To solve Model.objects.acreate(), we need to support async model instantiation, which likely means we need an aset
    - [https://github.com/django/django/pull/20602#pullrequestreview-4391796527](https://github.com/django/django/pull/20602#pullrequestreview-4391796527)
- Jacob wants to know if this is a good idea and/or next steps
- Emma: This may be a place we could use Raphael's async/sync generation code
    - [https://github.com/django/deps/pull/99](https://github.com/django/deps/pull/99)

## Moving models between apps

- [PR](https://github.com/django/django/pull/16905)
- Bhuvnesh worked on polishing and incorporating latest feedback
- Should be ready for a final review
- Could be a headline feature for 6.2!!

## Oracle Test Pilot

- [Forum](https://forum.djangoproject.com/t/proposal-leverage-oracle-test-pilot-for-django-ci/45197)
- Oracle hosted way of running CI against the oracle database
- We would need to opt into this by directing a CI action against this
- Emma: Is this related to the Oracle partnership inquiry?
    - Frank: Will follow up on this
- Natalia: Can someone ask what the next steps are, what are they looking for from us?
    - They have implemented a github action that we could review
    - We want a PR that runs the tests against their DBs
    - Could use the magic Jenkins comment, or have a GitHub actions test workflow
    - Tim: Send a message to open a PR / ticket to create to proceed this forward.
- Emma: Is this something that we'll be able to rely on? What level of support would it offer?
    - We could use this as a supplemental approach
- Requirements are listed as:
    - Review technical eligibility by analyzing the current GitHub Actions workflow(s)
    - Proceed with Oracle Test Pilot onboarding by providing required OCI resources
    - Tim to reach out to get a sense of poster availability to make a PR

## Redistributing licenses when injecting community packages

- When working on show_urls command, [https://github.com/django/django/pull/21307](https://github.com/django/django/pull/21307)
- We are doing more merging of 3rd party libraries into main / advocating that this is the path forward for features
- We have other licenses hanging out in the source code
- Emma: When merging 3rd party library features, we could ask maintainers opinion
    - If the maintainer is involved it's easier to do
    - If the maintainer isn't it's trickier
- Frank: When merging 3rd party packages in, we could ask them to BSD3 it, so it's easier for us to merge in
- On code organization
    - Could have a license file that directs to the various areas
    - Could have a license at the top of each file or related to it
- Seems agreement on social direction of asking maintainers to switch to BSD3 and/or formally agree to switch licenses. / Highlight that this is going to be a problem
    - Would need changes to new features repo README / process
    - Follow up with Adam's cookiecutter and Django Commons best practices
- We should credit the authors/maintainers in docs

## Advertising on djangoproject.com

- Carlton: We should improve the corporate sponsorship story first
- Showing advertisements would remove corporate sponsorship benefits

## PyCon US Recap

- It was a good time
- Django and the DSF was mentioned in several talks
- The security of GitHub Actions was referenced
- We had several contributors to Django at sprints, mostly first-time contributors
