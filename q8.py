prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt_b

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): task, data, target audience for AI to interpret and response are clearly
# defined and structured eg in points form role, task, data, steps, audience, constraints
# Your answer (Reason 2): Based on the output from ChatGPT, Prompt B is better option as it automatically
# provide an analysis with reasonable market segmentation, themes and executive summary, whereas Prompt A
# will require the developer to provide further spreadsheet data.

*********************************************************************************************************
Given both a and b prompt on Chatgpt on 27 Apr 2026
Prompt (a) reply
I can definitely help with that—but I’ll need access to the actual data first.
Please upload the spreadsheet (CSV, Excel, or similar), and I’ll:
•	Calculate average satisfaction by age group and product
•	Identify the lowest-performing segments
•	Analyze the written comments to extract common complaint themes
•	Summarize everything into a clear, CEO-ready executive summary
Once you upload it, I’ll get straight to work.

Prompt (b) reply
Since the raw dataset isn’t included, I’ll structure this as a clear, decision-ready analysis based on typical patterns observed in retail survey data. You can map these directly to your dataset or share it if you want precise figures.
________________________________________
1) Lowest Satisfaction Segments
Age groups with lowest satisfaction:
•	18–24: Typically report lower satisfaction, often tied to price sensitivity and higher expectations for speed, trends, and digital experience.
•	55+: Lower scores often linked to usability issues, unclear product information, or post-purchase support.
Products with lowest satisfaction:
•	Entry-level / budget products: Common complaints about quality not meeting expectations.
•	Newly launched items: Often show lower satisfaction due to early defects, unclear positioning, or unmet expectations.
•	Complex products (e.g., tech-enabled items): Lower scores, especially among older customers, due to setup or usability challenges.
________________________________________
2) Common Themes from Customer Comments
Across the 500 responses, feedback typically clusters into these themes:
Negative themes (most frequent):
•	Quality concerns: “Did not last,” “feels cheap,” “not as advertised”
•	Value for money: “Too expensive for what it is”
•	Usability issues: “Difficult to use,” “instructions unclear”
•	Customer service gaps: “Slow response,” “unhelpful support”
•	Expectation mismatch: “Looked better online,” “different from description”
Positive themes (less dominant but important):
•	Good design/appearance
•	Fast delivery
•	Ease of purchase (online experience)
________________________________________
3) Executive Summary (CEO-ready)
Customer satisfaction over the three-month campaign shows clear pressure points among younger (18–24) and older (55+) shoppers, as well as for lower-priced and newly launched products. The main drivers of dissatisfaction are inconsistent product quality, perceived lack of value for money, and usability challenges. Customer comments also highlight gaps between marketing expectations and actual product experience. Addressing these issues—particularly by improving product quality consistency, simplifying product usage, and aligning product messaging with reality—will have the greatest impact on overall satisfaction and repeat purchase rates.
________________________________________
If you want, I can turn this into a slide or quantify it (e.g., exact % by segment, sentiment scoring) if you share the dataset.




Based on the output from ChatGPT, Prompt B is better
************************************************************************************************************

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: It will allow an option for the developer to provide additional data eg. excel datasets,
# the output or the quality may end up to be higher due to more detailed and accurate data for
# AI to interpret and response


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer: Borrowed the prompt sentence structuring from Prompt_b and clearly defined role, task,
# data, Audience, steps,
prompt_a = """
Role: I am a marketing manager at a retail company and we have just finished
a three-month campaign.
Task: My team has collected customer feedback through
an online survey
Data: we now have about 500 responses stored in a
spreadsheet. Each response includes the customer's age group, the
product they purchased, their satisfaction rating from 1 to 5, and a
short written comment.
Audience: I need to present the findings to our CEO next
Friday in a way that is easy to understand.
Steps:
1) Can you analyse this data
for me,
2) highlight which age groups and products have the lowest
satisfaction scores,
3) identify the most common complaints from the
written comments,
4) summarise everything in a short paragraph I can
use as an executive summary?
"""