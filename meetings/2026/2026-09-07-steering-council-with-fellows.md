---
date: 2026-09-07
members:
  - Carlton Gibson
  - Emma Delescolle
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Jacob Walls
  - Natalia Bidart
  - Sarah Boyce
---

## Agenda

- DjangoCon US New Features discussion
- Using extras to package other tools
- [Experimental features GSoC Project](https://github.com/django/new-features/issues/3#issuecomment-5464308812)
- Fellows topics
  - Ping: [CompositeField DEP](https://github.com/django/deps/pull/113)
  - Status of [Content Type Parsing DEP](https://github.com/django/deps/pull/88)
- Case study blog posts
- Django usage telemetry/metrics

## Action items

- Sovereign Tech Fund
    - Emma: Get one or more project(s) ready (maybe Admin or at least list of places to start)
    - Plan another meeting with Lexi once the above is done
- Tim: Teams Charters
    - Translations Team - Need to reach out to Claude
- Carlton: DEP 20
    - ~~Final clean ups~~
    - ~~Short sentence describing new release process~~
    - ~~Short blog post draft with clear transition timeline statement.~~
- New Features improvements
    - Revisit the language around closing, so we can close things
    - Create a curated view of issues for people to participate in a high-impact area
    - Create new project board views with documentation/blog post with how to participate in new feature process
- Tim: Review Lexi's email and forward along
- Fellows: Review suggested major features

## Action Items Review

- DEP 20
  - Have the list of the last bits to implement to get it from accepted to final
- Lexi reached out regarding about sovereign tech fund via email
  - > One of the available areas is **Technical Debt Management** – essentially hands-on engineering work aimed at reducing maintenance burden and improving long-term sustainability, with the work delivered as maintainer-ready contributions
  - The other major projects that were originally discussed either turned into GSoC or aren't properly scoped for the sovereign tech fund.

## DjangoCon US New Features discussion

- Major changes for 6.2
  - Big features that may in vicinity of finish lines:
    - [https://github.com/django/django/pull/16905](https://github.com/django/django/pull/16905) moving a model between apps
    - [https://github.com/django/django/pull/18805](https://github.com/django/django/pull/18805) multiline template tags
      - There were some issues in a test project that suggests it may be a bit further than we'd like for 6.2
      - Could potentially reduce scope
    - [https://github.com/django/django/pull/21226](https://github.com/django/django/pull/21226) injectable comments into SQL for tracability (AI heavy)
    - [https://github.com/django/django/pull/18863](https://github.com/django/django/pull/18863) Composite GFK support
    - [https://github.com/django/django/pull/18332](https://github.com/django/django/pull/18332) expanding the messages API
    - [https://github.com/django/django/pull/20336](https://github.com/django/django/pull/20336) initial filters on QuerySet classes
    - [https://github.com/django/django/pull/16329](https://github.com/django/django/pull/16329) Embed raw queries as subqueries
  - Highlight/focus/attention:
    - Moving models between apps
      - Shai planning on working on during DotM
      - Emma has an django-devs mailing list for proposal for moving models between apps, it was a fairly small change
        - Premise was to be able to write migrations within the (models?) via contribute_to_class
        - [https://stackoverflow.com/questions/24311993/how-to-add-a-new-field-to-a-model-with-new-django-migrations/27450550#27450550](https://stackoverflow.com/questions/24311993/how-to-add-a-new-field-to-a-model-with-new-django-migrations/27450550#27450550)
    - ~~Rate limiting~~
      - Needs a DEP
      - Need to identify what is the universal functionality we need, "the 80% solution"
      - Likely not a 6.2 release because there isn't an agreed upon solution yet
    - Initial filters on QuerySet
      - Jacob: this seems reasonable
    - Fellows please review the list of features to see what's close
  - Other features:
    - [https://github.com/django/django/pull/21855](https://github.com/django/django/pull/21855) Added support for HTTP QUERY method
    - [https://github.com/django/django/pull/16381](https://github.com/django/django/pull/16381) QuerySet.select_for_share()
    - [https://github.com/django/django/pull/19298](https://github.com/django/django/pull/19298) Handle returning rows in update and bulk_update
  - Smaller features
    - [https://github.com/django/django/pull/21847](https://github.com/django/django/pull/21847) Improving debug messaging for CSRF errors
    - [https://github.com/django/django/pull/18468](https://github.com/django/django/pull/18468) Adding QuerySet.executed_queries
    - [https://github.com/django/django/pull/19603](https://github.com/django/django/pull/19603) Partitioned cookies (AI heavy)
  - Proposed message [6.2 major feature check-in](https://docs.google.com/document/d/12qAwQ5g_4yiZa0XtcQpMho6UVVnhEdIVhKKheknh6KU/edit?usp=sharing)
    - It's not necessary for us to have "major features" after big changes in 6.0 and 6.1
- Quarterly outreach to ask for attention in specific areas
  - Thoughts
    - Can we add a DSF sponsored email list?
      - The Board is working on a quarterly newsletter, but was sidelined for ED work
    - This would start as a blog post and forum post, until newsletter is created
  - Help filling out
    - Carlton will help after DotM
    - We should send this after DotM when things are usually better defined
- Django on the Prairie
  - Paolo convinced Frank to host!
  - Sprint days in Lawrence at the REVSYS office
  - Proposed time is in spring
  - Should we have guidelines on how to host these events?
    - Goal for DotM is to document how to host and run
    - Have start on Django specific bit here: [https://github.com/django/new-features/blob/main/hosting-new-feature-review.md](https://github.com/django/new-features/blob/main/hosting-new-feature-review.md)
    - On trademarking and using DjangoCon terminology: [https://www.djangoproject.com/foundation/conferences/](https://www.djangoproject.com/foundation/conferences/)

## Fellows

- FYI: we're getting confident triage from agent-wielding beginners now. No action needed for now (hopefully)
  - When new tickets are created, we're seeing LLM generated triage acceptance messages
  - No action needed for now since Fellows still review latest actions and can revert things as necessary

### CompositeField DEP

- Ping: [CompositeField DEP](https://github.com/django/deps/pull/113)
- Simon and Lily have taken an initial look
  - Carlton: Looks amazing and what we need!
- Hopefully Simon can review during DotM
- Needs Steering Council review

### Content Type Parsing DEP

- Status of [Content Type Parsing DEP](https://github.com/django/deps/pull/88)
- Chris M has put up a 3rd party package, but hasn't marketed it
- Things have stalled out a bit
  - There were concerns about JSON parsing on views that didn't have it before
  - This is a security concern for projects that update into new Django functionality
  - Could be a transitional setting to transition it
- We merged in the multipart classer attribute
- Can we dedicate Fellow time to this?
  - Yes
  - Jacob may spend time on this after DotM

## Using extras to package other tools

- There's the third-party package perspective from the GSoC project: [https://github.com/django/deps/pull/118](https://github.com/django/deps/pull/118)
- Could also be used to build commercial relationships, such as with Mongo, etc
  - Is there any hesitancy from packaging company sponsored packages with Django, assuming they're a sponsor of Django?
  - Frank: This seems to make a lot of sense for databases
  - Carlton: Nick Pope did work on this in the past
    - Memcached, etc
  - Lily: Sounds good on the vendor extras
  - Emma: We need to discuss what this process would look like
    - This is likely a board and steering council process.
    - Tim: We can try to redirect the DEP to focus on existing extras rather than experimental
  - Django[experimental]
    - This seems like the best way to handle it

## Experimental features GSoC Project

- Praful and Andy have things for folks to review
- [https://github.com/django/deps/pull/118](https://github.com/django/deps/pull/118) Third-party packages and extras
- Experimental features as a third-party package
  - [Repository](https://github.com/prafulgulani/django-experimental/tree/main)
  - [Discussion Thread](https://forum.djangoproject.com/t/implementing-a-formal-experimental-api-for-django/45217)
  - This could be something for 2028
- [https://github.com/django/deps/pull/117](https://github.com/django/deps/pull/117) feature flags
  - [Repository](https://github.com/prafulgulani/django-featurevault)
  - [Discussion Thread](https://forum.djangoproject.com/t/feature-flags-framework-for-django/45900)

## Case Studies with Django projects

- Tim to start doing case study blog posts for projects using Django
- If folks have big, old, cool projects, let him know for future iterations

## Django usage telemetry/metrics

- Tim's been working on [Django Probe](https://github.com/tim-schilling/django-probe/) idea on his own time
- Opt-in versus opt-out
  - This is a third party package, with toml file configuration
  - When collecting dependencies, only collect pypi dependencies
    - Need to look into private pypi
- Would need to be aware of blind spots this would this create
  - Deprecating something because it's not used in this could just mean people who use it aren't opted in
  - Some organizations are unable to respond to surveys or fill this out, but that doesn't mean their usage isn't warranted
