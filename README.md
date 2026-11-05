# Allegra Quote Assistant

A research and outreach tool for Allegra Marketing • Print • Mail, Palatine.

**Goal (Step 1):** When a client emails asking for a job, Brian gets a 2-minute brief and a reply that is ready to send. The brief covers who the client is, what Allegra has done for them before, how similar jobs were priced, and which quote details are still missing. The reply asks for those details and offers one relevant upsell.

## The two parts

| Part | What it does | Where |
| --- | --- | --- |
| **Claude skill** `/allegra-quote-reply` | Does the full job: web research on the company, the contact and their public LinkedIn; past-job comparison; spec check; the draft reply. Saves a JSON brief. | `.claude/skills/allegra-quote-reply/SKILL.md` |
| **Allegra Quote Assistant page** | An Allegra-branded page. Paste an email to get the spec check, past jobs, price ranges and a draft reply right away. Load a Claude brief to add the research. | `app/index.html` (built from `app/template.html`) |

## How to use it

1. Copy the client's email.
2. In Claude Code, open this repo and run `/allegra-quote-reply`, then paste the email. Claude gives you the brief in chat and saves `briefs/<date>-<company>.json`.
3. Optional: open the Quote Assistant page and click **Load Claude brief** to see everything in one place. Edit the reply, then click **Copy reply**.

You can also skip Claude: paste the email into the page and click **Build reply**. You'll get everything except the web and LinkedIn research.

## Job history (PrintSmith Vision)

`data/past-jobs.csv` holds **25 made-up sample jobs** in PrintSmith export columns:

`Invoice, Date, Account, Contact, Description, Product, Quantity, Size, Stock, Colors, Finishing, Total`

To use real data, export invoice or job history from PrintSmith Vision as a CSV with those columns. Column names don't have to match exactly: *Customer*, *Qty*, *Job Description* and *Invoice Total* all work. Then either:
- replace `data/past-jobs.csv` (the skill reads it), or
- click **Load PrintSmith CSV** on the page. The page remembers the file in your browser only.

Prices from past jobs stay in the brief for your quote. They never go into the client email.

## Rebuilding the page

After you change `app/template.html`, `data/past-jobs.csv` or the sample brief, run:

```
python3 app/build.py
```

## Design

The page uses the Allegra Design System: Allegra purple (#522E90) for one main purple element (the sidebar), Roboto for type, Caveat only for *We're all in*, square-leaning corners, and the service colors for the upsell marker.

## Next ideas

Following "smaller is better, build the next one tomorrow":
- Turn the brief into a pitch deck for the product they asked about
- Pull the email straight from Gmail or Outlook and save the reply as a draft
- A follow-up email after the quote goes out
