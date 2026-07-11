# Chronological Notes: Dot Plots and User Behavior

## Introduction to the Problem
- Founders often make the mistake of relying solely on aggregate user metrics (like Daily Active Users - DAU graphs) rather than understanding how individual users actually interact with the product.

## The Dot Plot Solution
- Dot plots visualize individual user behavior on a 2D grid (usually users on the Y-axis and days/time on the X-axis).
- This visualization allows you to see patterns that aggregate data obscures, such as:
  - Weekday power users versus weekend-only users.
  - Early churn (users who try the app once and never return), pointing to potential onboarding issues.

## Enhancing Granularity
- **Symbols for Specific Actions:** Instead of just marking that a user was active, you can use different symbols to denote specific actions (e.g., 'S' for using search, 'P' for joining a playlist, or distinguishing between sharing a photo vs. sharing contact info).
- **Encoding User State/Demographics:** Use colors or shading to represent user attributes, such as device type (iOS vs. Android), geography, or demographic information (e.g., income level, student status).
- **Sorting and Filtering:** You can sort rows based on these attributes to isolate patterns (e.g., looking only at iOS users or users who first signed up on a Monday).

## Historical Precedent and the Power of Visual Pattern Recognition
- The core concept traces back to PayPal's early days, where founders like Max Levchin used visual graphs of transactions to detect fraud patterns. Even when the underlying causes weren't immediately known, human visual intuition could spot anomalies.
- Dot plots allow founders to spot emerging patterns and then dig deeper to understand the "why."

## Comparing Dot Plots to DAU Graphs
- A DAU graph might show flat or stagnant growth (e.g., holding steady at 2-3 users per day).
- A dot plot for the exact same data can reveal a rich narrative, such as a core group of users consistently engaging every workday, indicating clear value for a specific use case (e.g., workplace listening).
- This can lead to hypotheses about causality, such as observing that users who join public playlists tend to have long streaks of consecutive daily usage.

## Scalability
- For early-stage startups with few users, you can plot every single user.
- As the user base grows to thousands, millions, or billions, dot plots scale via **sampling**.
- You can create specific segments (e.g., "iOS users in France" or "high-income web users in the US") and print out sample dot plots for team members to analyze and draw conclusions.

## Applicability to B2B
- Dot plots are not just for consumer apps; they are highly valuable for B2B SaaS.
- **Example:** A startup landed an $80k contract for 10 seats, but a dot plot would have shown that only 3 seats were activated, with very sporadic usage (never more than 2 days a week). The champion left, and the customer churned. A dot plot would have served as an early warning sign that the contract was in jeopardy.

## Common Mistakes and Misuses
1. **Charting the Wrong Event:** Do not use vanity metrics like "opened app" or "signed in." You must plot events that represent real value being created for the user (e.g., "listened to a song," "shared a photo").
2. **Time Periods Too Wide:** Grouping data by week obscures the necessary detail. Stick to daily or even sub-daily granularity to see true behavioral patterns.

## Final Recommendations
- Until you have hundreds of users, a dot plot should arguably be your primary or only dashboard.
- It is a straightforward log visualization tool that requires no complex computation—just parsing logs into a grid.
- **Synergy:** Use dot plots in conjunction with cohort retention curves. Cohort retention shows *if* users are sticking around in aggregate, while dot plots show *how* they are using the product, giving you the necessary context to ask the right questions, build better features, and fix broken experiences.