# Startup Metrics Planner Agent - Responsibilities and Tasks

Based on the Startup Metrics playbook, this document outlines the high-level strategies and granular actions that a Metrics Planner Agent would be responsible for scheduling, managing, and guiding a founder through, depending on the current stage of their startup and metrics progress.

## High-Level Phases

*   **Phase 1: Pre-Launch Tooling & Definition**
    *   Build basic metrics into the product before launching.
    *   Avoid the "too many metrics" trap; focus on testing big decisions.
    *   Maintain direct contact with customers instead of hiding behind dashboards.
    *   Select and strictly define a small set of key metrics using simple tooling.
*   **Phase 2: Investor Reporting & Fundamentals**
    *   Focus on Revenue as the primary key metric rather than vanity metrics (e.g., GMV, page views).
    *   Consistently report honest numbers to investors, even if revenue is zero.
    *   Prioritize tracking Revenue, Net Burn Rate, and Runway for investor updates.
*   **Phase 3: Retention & Cohort Analysis**
    *   Track customer retention to build sticky monthly cohorts (the "layer cake").
    *   Ensure retention curves flatten out over time instead of declining to zero.
    *   Calculate and monitor Net Dollar Retention (NDR) to track cohort revenue growth.
*   **Phase 4: Unit Economics Optimization**
    *   Calculate Gross Margin by determining Revenue minus Cost of Goods Sold (COGS).
    *   Factor in real costs of foundation models for AI companies, avoiding the trap of free API credits.
    *   Develop a clear roadmap to profitability if launching with negative unit economics.
    *   Fix negative gross margins before attempting to scale rapidly.

---

## Granular Actions & Tasks

### Pre-Launch Tooling & Definition
*   [ ] Implement basic metrics tracking into the product before launch.
*   [ ] Limit pre-launch tracking to testing big decisions rather than minor details like button colors.
*   [ ] Schedule regular times to get out of the building and talk directly to customers.
*   [ ] Pick exactly 4 or 5 key metrics to track accurately at the beginning.
*   [ ] Set up straightforward analytics solutions (e.g., simple SQL queries or tools like PostHog).
*   [ ] Write down precise, company-wide definitions for the 4 or 5 key metrics and stick to them.
*   [ ] Establish a rule to never change metric definitions just to make numbers look better.

### Investor Reporting & Fundamentals
*   [ ] Set Revenue as the primary key metric for tracking success.
*   [ ] Remove vanity metrics (like page views, unique visitors, GMV, or GTV) from key performance dashboards.
*   [ ] Calculate and report actual revenue accurately, avoiding the GMV trap involving rebates or cashback.
*   [ ] Structure investor updates to prominently feature Revenue, Net Burn Rate, and Runway at the top.
*   [ ] Calculate Net Burn Rate (monthly costs minus revenues).
*   [ ] Calculate Runway (total bank balance divided by net burn rate).

### Retention & Cohort Analysis
*   [ ] Calculate monthly retention rates for paying customer cohorts.
*   [ ] Graph monthly user cohorts to visualize the "layer cake" and verify the business is sticky.
*   [ ] Check retention curves to verify they flatten out at a certain percentage over time.
*   [ ] Calculate Net Dollar Retention (NDR) for the past 12 months.
*   [ ] Compare current NDR against benchmarks (>100% for organic growth, 110-120% for mature B2B SaaS, 125-150% for early-stage B2B SaaS).
*   [ ] Schedule customer interviews to identify and fix product issues if NDR is below 100%.

### Unit Economics Optimization
*   [ ] Calculate Cost of Goods Sold (COGS), including AWS bills, bandwidth, and API credits.
*   [ ] Calculate Gross Margin (Revenue minus COGS).
*   [ ] Calculate the true future cost of AI foundation models without relying on free startup API credits.
*   [ ] Identify any negative unit economics currently present in the business model.
*   [ ] Draft a clear roadmap to flip negative unit economics to profitability (e.g., bringing tech in-house, adding paid features).
*   [ ] Halt rapid scaling efforts until negative gross margins are fixed.
