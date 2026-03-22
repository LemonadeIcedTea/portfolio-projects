Analyzing Students' Mental Health

In this project I'm tasked with analyzing whether an international student's length of stay affects their average mental health diagnostic scores.

Output
- International Students' Mental Health Diagnostic Scores
  Executed a query analyzing international students by length of stay, calculating both the number of records and the average scores for PHQ, SCS, and AS. Results were grouped by stay duration, ordered from longest to shortest, and limited to the top nine categories.

Clone the repository:

git clone https://github.com/LemonadeIcedTea/portfolio-projects.git
cd portfolio-projects/students'_mental_health

Instruction to Run the Code:
sqlite3 mental_health.db ".mode csv" ".import data/students.csv students" ".read script/mental_health_analysis.sql"