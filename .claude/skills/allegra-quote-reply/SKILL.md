---
name: allegra-quote-reply
description: Turn a client's job-request email into a quote-ready reply for Allegra Marketing • Print • Mail (Palatine). Researches the client and sender, compares the request to past PrintSmith jobs, checks which quote specs are missing, and drafts a warm reply that asks for them. Use when Brian pastes a client email asking for a print, mail, sign or promo job, or says "quote reply", "new job request", or "prep a reply for [client]".
---

# Allegra Quote Reply

**Who it's for:** Brian at Allegra Marketing • Print • Mail, Palatine.
**When:** a client emails asking for a job and Brian needs to reply before he can quote it.
**Output:** a 2-minute brief in chat, plus a JSON brief Brian loads into the Allegra Quote Assistant page (`app/index.html`).

## Inputs

1. **The client's email.** Brian pastes it in. If he hasn't, ask for it and stop.
2. **Job history.** By default `data/past-jobs.csv` (sample data in PrintSmith Vision export columns). If Brian names a PrintSmith export file, use that instead. Match its columns by meaning: Invoice, Date, Account, Contact, Description, Product, Quantity, Size, Stock, Colors, Finishing, Total.

## Steps

### 1. Read the request
Pull out the company, the sender's name and title, their email domain, and every item they're asking for (product, quantity, size, dates, anything else).

### 2. Research the client
Use web search. Keep it to what helps the reply and the quote:
- **Company snapshot:** what they do, location(s), approximate size, website, and any recent news (openings, moves, events, hiring) that explains why they need this job now.
- **Contact background:** the sender's role and how long they've been there, from public sources.
- **LinkedIn:** search the web for the person's and company's public LinkedIn pages (for example `"Dana Kowalski" "Harper Ridge" LinkedIn`). Use only what shows in public search results. Don't sign in or scrape LinkedIn. Give the profile URL if you find one, and say clearly when you couldn't confirm it's the right person.
- Record every source URL. Never invent facts: if something isn't found, write "Not found".

### 3. Compare to past jobs
- **Customer history:** match on account name (and email domain if the account name differs). List their past jobs, the last order date, and the total spent.
- **Similar jobs:** find up to 5 past jobs with the same product type, ordered by closeness in quantity and size. Show the price per piece for each (Total ÷ Quantity) and the low–high range.
- These prices are for Brian's quote only. **Never put prices in the client email.**

### 4. Check the quote specs
Mark each one `found`, `unclear` or `missing`, quoting the email's words for anything found:

| key | spec |
| --- | --- |
| `quantity` | Quantity, or quantity breaks |
| `size` | Finished size |
| `product` | Product type (postcard, brochure, banner…) |
| `stock` | Paper or material: weight, finish |
| `color` | Ink and color: 4/4, 4/0, black only |
| `finishing` | Folding, binding, cutting, coating, corners |
| `artwork` | Print-ready files, or needs design |
| `due` | In-hands or due date |
| `delivery` | Pickup, delivery, shipping, or mailing (EDDM / mailing list) |

For a request with several items (for example postcards and business cards), check the specs for each item.

### 5. Pick one upsell
Choose the one Allegra service that fits best, from the eight services: marketing, print, mail, design, web, signs, promo, labels. Tie it to something real in the email or the research (for example, a new location suggests EDDM postcards to the surrounding neighborhoods, or signs for the opening).

### 6. Draft the reply
Warm and consultative, in Brian's voice:
- Thank them, and show you understood the project in one sentence. If they're a returning customer, mention the last job you did for them.
- Ask for the missing and unclear specs as a short bulleted list of plain questions. No jargon: write "full color on both sides?", not "4/4?".
- Mention the one upsell in one or two sentences, as an offer and not a push.
- Say when they'll get the quote: "within one business day" once you have the details.
- Customer-focused, second person, benefit first. No hype, no emoji. Sentence case.
- Sign off:
  ```
  Thanks,
  Brian
  Allegra Marketing • Print • Mail | Palatine
  <<phone>> | <<website address>>
  ```
  Keep the `<<phone>>` and `<<website address>>` placeholders unless Brian gives the real details.

## Output

**In chat**, give the 2-minute brief in this order:
1. **The ask:** one line.
2. **Who they are:** 3–4 bullets (company, contact, LinkedIn, news), with sources.
3. **History with Allegra:** returning or new, past jobs, last order.
4. **Similar jobs and pricing:** a small table with the per-piece range.
5. **Missing specs:** the list.
6. **Draft reply:** subject and body, ready to copy.

**Then save** `briefs/YYYY-MM-DD-<company-slug>.json` in this shape, and tell Brian to load it into the Allegra Quote Assistant page with **Load Claude brief**:

```json
{
  "version": 1,
  "createdAt": "2026-11-05",
  "client": { "company": "", "contact": "", "title": "", "email": "", "website": "" },
  "email": "the original email text",
  "research": {
    "snapshot": ["..."],
    "contact": ["..."],
    "linkedin": { "person": "url or null", "company": "url or null", "note": "..." },
    "news": ["..."],
    "sources": [{ "title": "", "url": "" }]
  },
  "upsell": { "service": "mail", "idea": "..." },
  "specs": [{ "key": "quantity", "status": "found", "value": "about 5,000 postcards" }],
  "reply": { "subject": "", "body": "" }
}
```

`briefs/sample-harper-ridge.json` is a worked example (a made-up client).
