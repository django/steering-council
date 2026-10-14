---
date: 2026-10-05
members:
  - Carlton Gibson
  - Frank Wiles
  - Lily Foote
  - Tim Schilling
other_attendees:
  - Catherine Holmes
  - Jacob Walls
  - Natalia Bidart
---

## Agenda

- Fellows:
  - [Set returning DEP](https://github.com/django/deps/pull/113/) really needs reviews
    - Jacob to nudge next week, otherwise default approved
  - All memcached python clients are defunct
  - PyPy 8.0 support?
  - Python 3.15 support and makedirs semantics
    - [https://forum.djangoproject.com/t/proposal-make-file-upload-permissions-respect-umask/45022/](https://forum.djangoproject.com/t/proposal-make-file-upload-permissions-respect-umask/45022/)
- Sovereign Tech Fund resilience program
- Contributor outreach message

## Action items

- Sovereign Tech Fund
    - Tim applied for the Sovereign Tech Resilience program
    - Tim, Natalia, Jacob to meet with Erik next week about the Sovereign Tech Fund resilience program
- Tim: Teams Charters
    - Translations Team - Draft initial version for Fellows and Claude to review
    - [https://github.com/django/dsf-working-groups/pull/98](https://github.com/django/dsf-working-groups/pull/98)
- New Features improvements
    - Revisit the language around closing, so we can close things
    - Create a curated view of issues for people to participate in a high-impact area
    - Create new project board views with documentation/blog post with how to participate in new feature process
- Fellows: Review suggested major features
- Fellows: Give feedback on: [Quarterly contributor outreach](https://docs.google.com/document/d/1DY0UClQ_AgEqT5hDQh4Kr5CQordCyVt5FGEuiAYl5-w/edit?usp=sharing)
- Jacob: Review Translators Charter
- Carlton: Post on the forum about the state and migrating away from these packages (memcached python clients are defunct)
    - [https://forum.djangoproject.com/t/should-we-stop-recommending-pylibmc/42993/10](https://forum.djangoproject.com/t/should-we-stop-recommending-pylibmc/42993/10)
- Natalia: Create branch for file upload permissions change
- All: Have a week to re-read one last time, will approve at the end of the week if no concerns

## Fellows

### [Set returning DEP](https://github.com/django/deps/pull/113/) really needs reviews

- [https://github.com/django/deps/pull/113/](https://github.com/django/deps/pull/113/)
- Table valued expressions- looking for Steering Council Review and Approval
- Implementation was reviewed at Django on the Med
  - Seemed to be in the right direction. Simon provided some feedback on the PR
- Want to have the DEP approved so we can merge the PR when it’s ready
- Tim reviewed and thinks it looks good. His only comments were in regard to technical writing.
- People have a week to re-read one last time, will approve at the end of the week if no concerns

### All memcached python clients are defunct

- No memcached clients support Python 3.14
  - They haven’t updated the test suites
- Tim Graham has been merging changes for [https://github.com/linsomniac/python-memcached/](https://github.com/linsomniac/python-memcached/)
  - He doesn’t have permission to release it
- [https://github.com/mxamin/pylibmc2](https://github.com/mxamin/pylibmc2)
  - This one was picked up by another open source contributor who maintained another package and needed it
- Options
  - Redirect people to another project from an existing one
  - Extract the MemCached cache wrapper out of Django core under the Django org
  - Work to get a maintainer to pass off the project
- Next steps
  - Carlton: Post on the forum about the state and migrating away from these packages

### PyPy 8.0 support?

- PyPy 8.0 release [https://pypy.org/posts/2026/09/pypy-v800-release.html](https://pypy.org/posts/2026/09/pypy-v800-release.html)
- This supports Python 3.12
- Do we want to support this even though we know 3.12 will age out in a few months?
  - No, this feels like more work than it’s worth right now
- Our docs say that PyPy works
  - We should update this to reflect the reality
- Next steps:
  - Remove PyPy from the docs since we’re not testing against it
  - Remove references to PyPy: [https://code.djangoproject.com/ticket/36123](https://code.djangoproject.com/ticket/36123)
    - Re-adding testing for PyPy: [https://code.djangoproject.com/ticket/37363](https://code.djangoproject.com/ticket/37363)
  - Add mention somewhere explaining the removal? (Blog, release notes, ?)

### Python 3.15 support and makedirs semantics

- [https://forum.djangoproject.com/t/proposal-make-file-upload-permissions-respect-umask/45022/](https://forum.djangoproject.com/t/proposal-make-file-upload-permissions-respect-umask/45022/)
- Proposal: Created upload directories takes on umask from the process
  - Switch for Python 3.15
  - Add mention to release notes
- Current: The upload directories takes on the permissions set in `FILE_UPLOAD_DIRECTORY_PERMISSIONS`
- Natalia to create new branch with proposed changes and get feedback

## Sovereign Tech Fund resilience program

- We received a positive message that indicated we would be eligible. They had follow-up questions that Tim and Sarah have answered.
- Tim to respond via email, Tim reiterate uncertainty on our side of things in email
- Tim, Natalia, Jacob to meet with Erik next week.
- This meeting is likely to be feeling things out and determining what’s possible.

## Contributor outreach message

- Needs the three major things we want feedback on
  - Requires Fellows feedback
  - This can be done by the end of month
- [not discussed] Should we include a CTA for people to join Translators and GSoC WGs?
