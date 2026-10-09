# Contributing a takeaway memo

For each paper you are assigned, write a memo that turns the paper into checks
a reviewer could run on someone else's manuscript.

This is not a summary. A summary says what the paper found. A memo says what
the paper obligates a reviewer to look for, and proves it with a page number.

Your memos become part of `/review-methods`, an open-source review agent in
this repository. A paper may be assigned to more than one student so that
independent readings can be compared.

---

## Mechanics

1. Copy the template below into `<lastname>-<bibkey>.md`.
   Example: `kim-roth_pretest_2022.md`.
2. Write the memo. About 1,500 words.
3. Submit the completed `.md` file through the course submission channel.
4. Submit one `.md` file per paper.

`references/` is the merged, curated version of everyone's work. It is built
by the instructor from `contrib/`. Do not write there.

---

## Two hard rules

**Every check must be anchored to a page.** A claim about what the paper says
carries a page number, or it earns no credit. Not a section name, not "the
authors argue," but a page. If you are working from a preprint, say so and give
the preprint's page.

**Quotes are 40 words or fewer.** This repository is public. Short quotes for
scholarly criticism are fine; block quotes are not. Paraphrase the rest.

A paper may establish a first-best design that cannot be added after data
collection. In that situation, a memo may recommend a clearly labeled
second-best analysis that follows from the paper's framework. Explain what the
fallback can and cannot establish; do not treat it as equivalent to the
first-best design.

---

## The six questions

Answer these in order, in prose. No headings required beyond the ones in the
template, no YAML, no code.

**1. What does the paper establish?**
Two or three sentences in your own words. Enough that a reader who has not
read the paper knows what is at stake.

**2. What should a reviewer check in someone else's manuscript because of
this paper?**
Two to five checks, and more are fine when the paper genuinely supports
them; every additional check must clear the same evidence bar. Each is stated
as something a reviewer could actually do
while reading a manuscript. "Check whether the paper reports the power of its
pre-trend test" is a check. "Consider the importance of parallel trends" is
not.

**3. Where in the paper does each check come from?**
A direct quote with a page number, then one or two sentences connecting the
quote to the check. This is the most heavily weighted question.

**4. When does each check apply, and when does it not?**
Be narrow. A check that applies to every quantitative paper is worthless: it
becomes noise the agent emits on every manuscript, and reviewers stop reading.
State the design features that trigger it, and at least one nearby case where
it should stay silent. This is the question students find hardest and the one
that determines whether the finished agent is usable.

**5. What does the failure look like on the page?**
The concrete thing you would see in a manuscript that has the problem: a
sentence, a figure, a table pattern, a robustness appendix that is missing.

**6. Name two published papers.**
One where the check should trigger, one where it should not. One line each on
why. These become the agent's test cases, so pick papers you have actually
looked at.

---

## Template

Copy from here down.

```markdown
# <Paper short title>

**Contributor:** <name as it should appear in the repository>

**Full citation:** <as given to you>

## 1. What the paper establishes

## 2. Checks for a reviewer

## 3. Evidence

## 4. Scope

## 5. What failure looks like

## 6. Test cases
```

---

## Worked example

Read [`EXAMPLE-atsusaka_kim_2025.md`](EXAMPLE-atsusaka_kim_2025.md) before you
start. It is a complete memo on Atsusaka and Kim (2025), on measurement error in
ranking questions, written to the format above with real quotes and real page
numbers.

Notice what it does not do. It does not summarize the paper's proofs, and it
does not explain the estimators. It converts the paper into five things a
reviewer can look for, bounds when each applies, and says what the failure looks
like in print. A large share of its length goes to Q4, where the checks do
*not* trigger. That proportion is deliberate; match it.

Two more habits worth copying from it. Its check (c) is directional: it says
which way random responses can pull the estimate and what a null result could
be masking, and a directional check is worth more than a cautionary one. And its sharpest scope
boundary comes from the authors' own statement of their limits, which is where
the best scope conditions usually live. Read the limitations paragraph before
you write Q4.

Its check (e) also illustrates a second-best recommendation. A randomized
anchor is the preferred design, but it cannot be added after a survey has
already been fielded. In that case, plausible external benchmarks can support
a sensitivity analysis, provided the memo states that they do not identify the
random-response rate.

---

## Rubric (100 points)

| Q | Component | Points |
|---|---|---:|
| 3 | **Evidence.** Every check has a direct quote and a page number, and the quote actually supports the check. | 25 |
| 2 | **Checks are actionable.** Stated as something a reviewer does, not a topic to consider. Two to five of them; no hard upper limit if each is supported. | 25 |
| 4 | **Scope.** Narrow, with an explicit non-applies case for each check. | 20 |
| 1 | **Comprehension.** Accurate, in your own words. | 10 |
| 5 | **Failure signature.** Concrete and recognizable in a real manuscript. | 10 |
| 6 | **Test cases.** Two real papers, plausibly classified. | 10 |

**Zero-credit rule.** A check with no page-anchored quote earns nothing under
Q2 or Q3. Three checks with pages beat four checks where one is unsupported.

**Common ways memos lose points:**

1. The memo summarizes the paper instead of extracting checks. (Q2)
2. Checks are stated as topics, like "consider measurement error." (Q2)
3. Scope is universal, so the check would trigger on every manuscript. (Q4)
4. A quote is real but does not support the check drawn from it. (Q3)
5. Test cases are named but were never opened. (Q6)

---

## Attribution

Your chosen contributor name stays attached to your memo in `contrib/`, and
the merged entries in `references/` cite both the source paper and the
contributing students.

By submitting a memo, you authorize the instructor to publish your original
contribution in this repository under its MIT License. Quotations and other
third-party material remain the property of their respective rights holders
and are not licensed under MIT.
