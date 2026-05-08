# B2B Startup Metrics | Startup School

**Speaker:** Tom Blomfield (Group Partner at Y Combinator, former founder of Monzo and GoCardless)

## 1. Why Metrics Are Crucial for Startups
* **Making Better Decisions:** Good metrics are like flying an aircraft with instruments; without them, you are flying blind and not in control of your startup.
* **Pre-Launch Necessity:** You must build basic metrics into a product before launching. Launching without them (e.g., on Hacker News or Product Hunt) leaves you unaware if hundreds of new users are daily active, weekly active, or instantly churning.
* **Founder Competence:** Investors look for founders who are in command of their metrics (e.g., DAU/MAU percentage, ARPU). It is a major differentiator.
* **Warning - The "Too Many Metrics" Extreme:** Do not build a dashboard with 500 metrics before launch. When you have only a few hundred or thousand users, split testing every minor detail (like button colors) is impossible due to lack of volume. Focus on testing big decisions (e.g., $80/year vs. $200/year pricing).
* **Don't Hide Behind Metrics:** Metrics should not prevent you from getting out of the building. You must maintain a close, direct obsession with talking to customers (e.g., Brian Chesky hosting Airbnb users).

## 2. Choosing and Defining Your Key Metrics
* **Start Small:** Pick exactly 4 or 5 key metrics to track accurately at the beginning. This number will grow over time.
* **Simple Tooling:** Use straightforward analytics solutions. It can be a simple SQL query on your database or tools like PostHog (YC W20).
* **Strict Definitions:**
  * Agree on the precise definition of these 4 or 5 metrics company-wide and stick with them.
  * Internal disagreements (e.g., marketing claiming 2,500 leads while sales rejects them) destroy productivity.
  * *Crucial rule:* Keep metric definitions strictly consistent over time. Changing a definition just to make numbers look better (like switching from weekly to monthly active users) only fools yourself.

## 3. Revenue vs. Vanity Metrics
* **Vanity Metrics:** Metrics like page views, unique visitors, Gross Merchandise Value (GMV), or Gross Transaction Value (GTV) seem impressive but aren't tied directly to the success or profitability of the company.
* **The GMV Trap:** A B2B company might show rapidly growing GTV because they sign larger clients, but if they offer massive rebates or cashback, actual revenue could be flat. Tracking the wrong metric leads employees to optimize for the wrong things.
* **Revenue is King:** For almost all B2B companies, **Revenue** should be the primary key metric.
* **Honesty in Reporting:** Don't hide bad revenue numbers. Investors respect founders who consistently report zero revenue upfront if it's the truth, as it clarifies what actually needs to be fixed.

## 4. The Top 3 Metrics for Investor Updates
1. **Revenue**
2. **Net Burn Rate:** Monthly costs minus revenues (if you are loss-making). It is the amount your bank balance decreases every month.
3. **Runway:** Total bank balance divided by net burn rate (e.g., $1,000,000 in bank / $100,000 burn rate = 10 months of runway).
* *Note:* If these three numbers are not at the top of an investor update, investors will assume the founder is hiding something.

## 5. Retention & The "Layer Cake" Model
* **Defining Retention:** If you sign up 100 paying customers in January, the percentage still paying in subsequent months (February, March, April) is your retention rate.
* **The Layer Cake of Sticky Cohorts:** Stacking monthly user cohorts on a graph demonstrates how sticky a business is.
  * High retention (e.g., GoCardless, Stripe) builds a fat "layer cake" where users implement the solution and rarely leave. The business continually grows as layers compound.
  * Low retention results in a "leaky bucket," where users churn off rapidly. You reach a plateau where you are scrambling just to replace the churned customers from previous months.
* **Retention Flattening:** It is vital that retention curves flatten out at *some* percentage over time, rather than steadily declining to zero.

## 6. Net Dollar Retention (NDR)
* **Definition:** A calculation crucial for B2B SaaS companies tracking cohort revenue over time.
* **Calculation Example:**
  * You sign 10 customers in January at $10k/month ($100k MRR).
  * Fast forward 12 months: 2 customers cancel (loss of $20k).
  * 3 customers are upsold to $20k/month (gain of $30k).
  * Net change: -$20k + $30k = +$10k.
  * The cohort now generates $110k/month. This is **110% Net Dollar Retention**.
* **The Benchmarks:**
  * **>100%:** Your cohorts are growing organically over time (exponential growth curve).
  * **125% - 150%:** Excellent for early-stage B2B SaaS (due to underpricing initial products, adding new features, and improving upsell capabilities).
  * **110% - 120%:** Good benchmark for mature enterprise B2B SaaS companies.
  * **<100%:** A massive warning sign for Enterprise B2B SaaS. It means you are losing customers. Stop trying to scale and fix the product by talking to users.

## 7. Gross Margin & Unit Economics
* **Definition:** Revenue minus Cost of Goods Sold (COGS). For a software company, COGS is any cost that varies directly per incremental customer (e.g., AWS bills, bandwidth, or API credits).
* **The AI Margin Shift:** Historically, pure SaaS had ~95% gross margins. Today, AI companies pay heavily for foundation models (OpenAI, Anthropic), making COGS significant. *Warning:* Do not hide behind free startup API credits; you must factor in what the real cost will be.
* **Operational Businesses:** Businesses with human operations (delivery, installations) typically have very low margins (5-15%). They require significantly more scale and revenue to cover head office and engineering fixed costs compared to software.
* **The Danger of Negative Margins:**
  * Selling a $10 service for $9 (negative gross margin) to capture market share was common in the ZIRP (Zero Interest Rate Policy) era (e.g., Uber, 10-minute grocery delivery).
  * In the current high-interest-rate environment, capital is expensive, and investors despise negative margin businesses.
  * If you launch with negative unit economics (like Monzo did initially, losing £30-£40 per user), you must have a clear roadmap to flip them to profitability (bringing tech in-house, adding paid features) *before* trying to scale rapidly.

## Summary Checklist
- [ ] Have 4-5 key metrics tracked before launch.
- [ ] Ensure strict, company-wide definitions for each metric.
- [ ] Focus on Revenue over vanity metrics (GMV/GTV).
- [ ] Put Revenue, Net Burn, and Runway at the top of every investor update.
- [ ] Target Net Dollar Retention of 120%+ for B2B SaaS.
- [ ] Fix negative gross margins before attempting to scale.
- [ ] Never stop talking to customers.
