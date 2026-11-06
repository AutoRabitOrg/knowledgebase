# Standardizing release notes

Release notes follow style guide rule G-31:

```markdown
## <Product> <version>

**Release date:** 4 November 2026

### New features
#### <Short title>
...
### Enhancements
### Fixes
```

## Fix existing pages (about a minute)

Run this from your clone of the repository, on a Mac or Linux machine with `git`, `python3`, and `gh` signed in:

```bash
tools/release-notes/run.sh            # every product
tools/release-notes/run.sh Vault      # one product
```

Products: `ARM`, `DataLoader`, `CodeScan`, `"CodeScan Self-Hosted"`, `Vault`, `Guard`, `nCino`, `"IZ Suite"`.

The script:

1. Starts from the latest `main` in a temporary copy. Your folder and branches aren't touched.
2. Reformats headings, release dates, and section names. It never changes wording, never adds or removes lines, and never changes heading levels or page structure.
3. Runs `verify.py`, which proves every body line is identical and every heading and date keeps its version number and date. Any other change stops the run.
4. Runs the same checks GitHub runs on every pull request.
5. Shows a summary and asks before it pushes a branch and opens a pull request.

It writes two files to `~/release-notes-runs/<date>-<product>/`:

- `review.csv`: every heading and date it changed, before and after, for a quick skim.
- `needs-a-person.csv`: anything it couldn't convert safely, such as a date with no day.

**Merge the pull request the same day.** GitBook re-saves pages often. If GitHub shows a conflict, close the pull request and run the script again.

## Write new release notes

Write them in the G-31 format from the start. The pull request checks reject a release heading, date line, or section name that doesn't match. GitBook's AI applies the same rule from the style guide page.

## What the tools don't do

These need a person, because they change meaning or structure:

- Sorting items into New features, Enhancements, and Fixes when a release has no sections.
- Rewording fix titles to describe the corrected behavior.
- Merging, splitting, or moving pages. When you do, add a redirect in `.gitbook.yaml` so old links keep working.
