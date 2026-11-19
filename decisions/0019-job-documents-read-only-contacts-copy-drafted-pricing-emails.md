---
number: 0019
title: Job documents, a read-only contacts copy, and drafted pricing emails
status: accepted
date: 2026-11-16
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

Around the estimate, the tool also keeps:

- **Each job's documents in one place**, filed under its site address. Each document
  gets a label saying what it is, separate from its file name; the labels include "Full
  plan set".
- **A read-only copy of his vendor and sub contacts**, loaded from his exported contact
  list. The operations app stays the master.
- **Request pricing:** the owner ticks a job's documents and contacts, and the tool
  drafts the email, as a prepared draft in his mail program or through the phone's share
  menu. For now the owner sends, not the builder.

Rules for the request emails (self-review decisions 6 and 7): the subject uses the site
address only; line item wording goes without quantities unless ticked; one email per
contact, so subs do not see each other; a warning when the text holds another contact's
name; cost documents cannot be ticked for sending. "Requested, waiting" is set by a
"Mark as sent" tap, not by drafting, and is kept in the job's request records, not in
the estimate file.

## Why

Getting prices from vendors and subs is part of making an estimate, and the owner wanted
the documents, the contacts and the email draft all in one spot.

## Considered instead

**A connection to an email account, sending or drafting on screen.** Parked for the
operations app: large to build for the gain. The owner agreed it makes no sense for now.

**The tool keeping its own editable contact list.** Rejected: two lists to keep in step,
against one source of truth. See decision 0024.

**The job name (address plus client name) as the email subject.** Narrowed to the site
address only, because every vendor would otherwise get the client's name.

## What it costs us

The tool is growing past "small". Each of the three is small alone; together they are a
second area beside estimating (recorded as a known limit on 2026-11-16). The contacts
copy duplicates a list the operations app owns. A plain mail link cannot carry
attachments, and which mail program the owner sends from, and what program the contact
export comes out of, were still open in the current-state document. Addresses and
contact names are real data and stay on the owner's computer.

## His words

> have all the documents in one place

> he can just export his contact list and I'll load it into the software we're building

> I agree options see for emails makes no sense. I will be the one sending the emails
> most likely in the beginning until I build this as a full application... click the
> documents from that project... all in one spot to draft an email

("options see" is transcription for "option C", the email account connection.)

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 1,
  checked against the working log, part 2, section 2 and part 3, section 2.
- Decision 0024: choosing the vendor or sub. Decision 0051: the Request pricing screen.
