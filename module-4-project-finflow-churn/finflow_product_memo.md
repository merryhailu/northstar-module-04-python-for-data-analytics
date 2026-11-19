FinFlow Customer Churn Analysis

Prepared for: Lina, VP of Product, and Product Directors
Date: November 19, 2026

1. Executive Summary

FinFlow's biggest customer retention challenge is the Basic tier, where churn reaches 25.08%, compared with just 4.96% for Enterprise customers. This means Basic customers leave at approximately five times the rate of Enterprise customers, creating a clear opportunity to improve retention through a stronger upgrade experience and targeted product engagement. Product leadership should prioritize Basic-tier retention while investigating differences across signup cohorts.

2. Findings

1. Basic customers have the highest churn risk. Basic customers have a 25.08% churn rate, compared with 14.86% for Pro and 4.96% for Enterprise. The gap between Basic and Enterprise is approximately 20 percentage points. This identifies Basic as the highest-priority tier for retention improvements.

1. Enterprise customers demonstrate the strongest retention. Approximately 95.04% of Enterprise customers remain active, compared with 85.14% of Pro customers and 74.92% of Basic customers. The Enterprise retention pattern suggests that understanding what keeps higher-tier customers engaged could help inform improvements to the lower-tier experience.

1. Churn across signup cohorts is generally consistent. Most monthly cohorts show observed churn rates of approximately 19%–21%. However, customers who signed up earlier have had more time to leave than recent customers. These figures therefore do not establish whether retention is improving or declining over time.

1. Recommendations

1. Prioritize Basic-tier retention. Review the Basic customer journey and identify friction points, particularly during onboarding and early product use. Test improvements to engagement and the Basic-to-Pro upgrade experience. A reduction from 25% to 20% churn would mean five additional customers retained for every 100 Basic customers, assuming the same customer base and measurement period.

1. Identify what drives Enterprise retention. Compare Enterprise and Basic experiences, including onboarding, feature adoption, support interactions, and product engagement. Use the findings to identify improvements that can be introduced to lower-tier customers.

1. Establish equal-age cohort monitoring. Track churn at consistent milestones, such as three and six months after signup. Investigate unusual cohort patterns once customers have had equal time to experience the product.

1. Data Caveats and Limitations

This analysis was prototyped using a Faker-generated synthetic dataset modeled after the FinFlow schema, not actual FinFlow production data. The findings are illustrative and should not be treated as confirmed business performance. Before making operational decisions, the analysis must be rerun using approved production warehouse access, confirmed table and column definitions, validated churn logic, and a sufficiently large, representative customer sample.

5. AI Use Note

I used Claude throughout this project as a supporting tool for learning, understanding unfamiliar concepts, and debugging code. I asked for guidance on creating the cohort-by-tier heatmap, as reshaping the data with pivot() and understanding how to structure the heatmap were new concepts for me. I also used Claude to troubleshoot errors encountered while building the notebook and combining the six visualizations into one interactive dashboard. I reviewed the suggested code, tested the solutions, and made sure I understood how they worked before applying them. I independently verified the key findings in the memo by recalculating the headline numbers against the enriched CSV dataset.
