# Early-Stage Founder Sales AI Agent: System Design

## 1. System Overview
**Architecture:** LangChain Deep Agents
**Design Pattern:** Central Orchestrator with Specialized Agent Skills
**Target Audience:** Early-stage technical founders navigating B2B/Enterprise sales.
**Core Philosophy:** The agent acts as an internal advisor, assisting the founder with strategy, copywriting, pricing, and pipeline management. It is heavily grounded in Y Combinator and MIT B2B sales methodologies (e.g., the "Sales Facilitator" method, Off-ramping, Value Equation pricing).

## 2. Core Architecture: The Deep Agents Pattern

Using the LangChain Deep Agents framework, the system is designed to avoid a monolithic prompt. Instead, it utilizes a modular "Agent Skills" architecture:

### 2.1. The Central Orchestrator Agent
* **Role:** The "Director of Sales Strategy." It acts as the primary interface for the founder.
* **Responsibilities:**
  * Understands the founder's current context and intent (e.g., "I have a call tomorrow," "Help me price this," "I need to reach out to this CEO").
  * Maintains cross-thread memory of the product, the startup's stage, and the active sales pipeline.
  * Routes complex tasks to the appropriate specialized **Sub-Agent Skills**.
  * Synthesizes the outputs from the sub-agents into actionable advice for the founder.

### 2.2. The Sub-Agent Skills
Each skill is an independent Deep Agent with a highly specific persona, system prompt containing distinct domain knowledge, and a focused objective.

---

## 3. Agent Skills Definitions

### Skill 1: Strategy & Prospecting Agent
* **Purpose:** Helps the founder figure out who to sell to and defines the initial wedge strategy.
* **Domain Knowledge:**
  * Top-Down (Executives) vs. Bottoms-Up (End-users) frameworks.
  * The Customer Profile concentric rings (Company -> Buyer Role -> Decision-Making Unit).
  * Wedge Strategy (solving a narrow, burning problem in 48 hours).
* **Inputs:** Product description, current hypotheses, feature lists.
* **Outputs:** Target customer profiles, recommended sales motion, and actionable criteria for building lead lists (e.g., "Find companies using technology X with team size Y").

### Skill 2: Outreach & Copywriting Agent
* **Purpose:** Crafts highly effective, human-sounding cold outreach and strategizes warm introductions.
* **Domain Knowledge:**
  * The 7 Principles of Effective Email Copy (Focused goal, human tone, deep personalization, short length, credibility, reader-focused, clear CTA).
  * The "Uncommon Commonality" concept for deep personalization.
  * Avoidance of "I/We" language in favor of "You" language.
* **Inputs:** Prospect's LinkedIn/background, founder's background, specific product value.
* **Outputs:** Personalized email drafts, follow-up cadence strategies, and advice on leveraging network connections for warm intros.

### Skill 3: Qualification & Discovery Agent
* **Purpose:** Prepares the founder for initial calls and heavily focuses on disqualifying bad leads.
* **Domain Knowledge:**
  * The "Sales Facilitator" persona (helping prospects opt-out).
  * "Off-ramping" techniques (Ghosting off-ramp, Competitor off-ramp, ROI off-ramp).
  * Listening > Pitching; "Great Movie Script" demo structure.
* **Inputs:** Prospect notes, upcoming meeting context, stalled deal behavior (e.g., "They asked for a pilot but won't give me data").
* **Outputs:** Scripted discovery questions, tailored off-ramps to test buying intent, and blunt diagnoses of whether a lead should be disqualified.

### Skill 4: Pricing Agent
* **Purpose:** Helps founders overcome the fear of pricing, calculates value, and prevents cost-plus pricing traps.
* **Domain Knowledge:**
  * The Value Equation (Direct cost savings, time savings, revenue increase).
  * The 1/3 Rule (Charge 25-33% of the total value delivered).
  * The "50% iteration rule" for early experimental pricing.
  * Gating enterprise features (SOC2, SSO) behind "Contact Sales".
* **Inputs:** Customer's operational costs, product impact metrics, competitor pricing, champion's signing authority limit.
* **Outputs:** A calculated Value Equation document, recommended annual contract price, and strategic pilot pricing (e.g., pricing just below the champion's credit card limit).

### Skill 5: Closing & Pilot Structuring Agent
* **Purpose:** Navigates the transition from free pilots to paid contracts and manages the procurement maze.
* **Domain Knowledge:**
  * The "Pro Move" (Recurring revenue contracts with 30-day opt-outs).
  * Shortening Proof of Concept (POC) time-to-value (doing "janky stuff" to prove value in hours, not months).
  * Identifying the internal champion and mapping the buying process (Legal, InfoSec, Economic Buyer).
* **Inputs:** Deal stage, champion interactions, procurement hurdles.
* **Outputs:** Structuring terms for paid pilots, negotiation tactics for legal redlines (only fighting "company-ending" clauses), and implementation roadmaps.

### Skill 6: Pipeline & Forecasting Agent
* **Purpose:** Helps the founder manage their funnel, forecast revenue accurately, and understand sales economics.
* **Domain Knowledge:**
  * The Weighted Pipeline Method (assigning % probabilities based on historical funnel conversions).
  * COCA (Cost of Customer Acquisition) calculated by stage.
  * The Refrigerator Model for Timing (Counter, Refrigerator, Freezer).
* **Inputs:** Current lead statuses, marketing/ads spend, conversion rates, deal sizes.
* **Outputs:** Quarterly revenue forecasts, funnel drop-off analysis, COCA calculations, and triage recommendations (e.g., "Move these 5 deals to the freezer").

---

## 4. Workflows & Interaction Pattern

1. **User Input:** Founder: *"I had a great call with a VP at a pharma company. They want a 3-month free trial to test the AI. How should I respond?"*
2. **Orchestrator Routing:** The Orchestrator Agent recognizes this involves both **Qualification** and **Closing/Pilots**.
3. **Skill Invocation:**
   * It queries the **Closing & Pilot Structuring Agent** regarding the 3-month free trial. (Skill responds: *Reject the 3-month free trial. Propose a 14-day paid pilot or a recurring contract with a 30-day opt-out.*)
   * It queries the **Qualification & Discovery Agent**. (Skill responds: *Test their intent. Offer a 'Competitor Off-ramp' or ask what specific metrics they are trying to prove in 3 months.*)
4. **Synthesis:** The Orchestrator combines these insights and presents the founder with a clear, firm response strategy, explaining *why* a 3-month free trial is a trap and providing exact phrasing to push back and secure a paid commitment.
