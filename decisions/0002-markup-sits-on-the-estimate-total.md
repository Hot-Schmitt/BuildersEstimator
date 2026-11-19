---
number: 0002
title: Markup sits on the estimate total, as a percent or a dollar amount
status: accepted
date: 2026-11-18
decided_by: owner
area: pricing
supersedes:
superseded_by:
---

## Decision

Markup applies to the estimate total, not to individual line items. The builder
chooses whether to enter it as a percent or as a dollar amount, by a toggle on the
cost summary.

It sits on all cost, including tax and contingency, which is how his own sheet works.
A dollar markup does not grow when cost is added later, and the cost summary says so
on screen.

Markup per line item, and markup per cost type, are parked — not refused.

## Why

Three reasons, in order of weight.

His own estimate sheet applies a single overhead-and-profit line at exactly 25% of all
cost (verified against his sheet by script). Matching how he already works is the
first rule of this tool.

He asked for the percent-or-dollar choice himself.

Research found no industry standard to defer to. The main residential estimating
tools all offer both approaches and leave it to the builder: CoConstruct offers
per-line markup in columns or markup rows on the project subtotal; ConstructionOnline
offers per-line markup as a fixed amount, a percent of cost, or an amount per unit;
Buildertrend has a default markup or margin by cost type; Procore applies a markup to
the whole estimate or to selected cost codes. Checked 2026-11-18. With no standard to
follow, his own sheet decides.

## Considered instead

**Markup per line item, or per cost type.** Genuinely useful for a builder who marks
up subcontractors differently from materials, and it is what several competitors lead
with. Parked because his sheet does not work that way, and because the project rule is
to keep the tool small. Revisit if the builder asks for it.

## What it costs us

A percent markup on the total cannot exclude a single line. A pass-through cost such
as a permit fee, which a builder might not want to mark up, gets marked up like
everything else. There is no way around that without the per-line markup we just
parked.

The markup base is also not fully confirmed. "Markup sits on all cost" is read from
his sheet, not stated by him. Whether he *means* to mark up sales tax and contingency,
and whether he has pass-through costs he deliberately leaves out, are open questions
for him in `docs/builder/questions.md`. If his answers differ, this decision's base
changes even though the percent-or-dollar choice stands.

## His words

> As far as markup to his total bill as a percent, a dollar amount, that is also a
> toggle that he can choose. But I want to think through how most builders would want
> this. Would they generally do it on the line item or as the total bill?

## Links

- `docs/builder/questions.md` — the open questions that could move the markup base.
- Shared estimate format, `docs/format.md`: percent-or-dollar markup is one of the
  twelve changes approved for version 0.5.
- Research sources, 2026-11-18: coconstruct.com/learn-construction-software/applying-markup-by-columns-vs-rows;
  help.constructiononline.com/en/markup-vs.-margin; help.constructiononline.com/en/set-estimate-defaults-1;
  buildertrend-publicroadmap.launchnotes.io; v2.support.procore.com/product-manuals/estimating-project/tutorials/add-adjustments-to-an-estimate
