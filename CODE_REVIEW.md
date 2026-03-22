# Code Review — DataCamp Real World Projects

Reviewed by: Claude Code
Date: 2026-03-22

---

## Overall Ratings

| Project | Rating | Top Issue |
|---|---|---|
| Avocado Toast Supply Chain | Fair | Path handling, redundant `file.close()` |
| COVID Workout Analysis | Poor | Hardcodes answers instead of computing them |
| Crime in Los Angeles | Fair | Commented-out debug code left in |
| Customer Purchase Analysis | Fair | Hardcoded correlation value |
| Debugging Sales (Buggy) | Good | Intentional bugs for learning |
| Debugging Sales (Fixed) | Good | Well-corrected bugs |
| Electric Vehicle Charging | Poor | Unused variables, hardcoded values |
| Generating Keywords | Good | Clean and functional |
| Netflix Movies | Poor | Hardcoded `duration = 100`, useless `else` |
| Online Sports Revenue | Fair | Variable name reused, `inplace=True` |
| Sleep Health | Fair | Repetitive code, verbose conditionals |
| Students' Mental Health (SQL) | Good | Clean query |

---

## Recurring Issues

These patterns appear across multiple projects. Fixing them consistently will raise the quality of the whole portfolio.

---

### 1. Hardcoding results instead of computing them

This is the most important issue. Several projects assign the answer as a hardcoded value instead of deriving it from the data. This defeats the purpose of the analysis — if the data changes, the answer stays wrong.

**Affected:** `covid_workout`, `netflix_movies`, `electric_vehicle_charging_trends`

```python
# Bad — hardcoded
duration = 100
top_country = "United States"
trend = 'same'

# Good — derived from data
duration = filtered_df['duration'].value_counts().idxmax()
top_country = df_workout_geo.sum(axis=1).idxmax()
```

---

### 2. Commented-out code left in

Debug `.head()` calls and commented-out analysis are left in several scripts. Remove them before sharing or submitting.

**Affected:** `crime_in_los_angeles`, `netflix_movies`, `online_sports_revenue`

```python
# Remove these kinds of leftovers
#crimes.loc[crimes["Vict Age"] < 0, "Vict Age"] = np.nan
#print((crimes["Vict Age"] < 0).sum())
#sports_df.head()
```

---

### 3. Useless `else` and verbose conditionals

**Affected:** `netflix_movies`, `sleep_health`

```python
# Bad — useless else branch does nothing
for label, row in action_df.iterrows():
    if row['duration'] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count  # this line does nothing

# Bad — verbose boolean assignment
if lowest_sleep_occ == lowest_sleep_quality_occ:
    same_occ = True
else:
    same_occ = False

# Good
same_occ = lowest_sleep_occ == lowest_sleep_quality_occ
```

---

### 4. Using loops instead of pandas vectorized operations

Iterating over rows with `iterrows()` is slow and unpythonic. Pandas has built-in ways to do this.

**Affected:** `netflix_movies`

```python
# Bad — slow manual loop
for label, row in action_df.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1

# Good — vectorized, faster, cleaner
short_movie_count = (action_df['duration'] < 90).sum()
```

---

### 5. `inplace=True` is discouraged

Modern pandas discourages `inplace=True` as it can cause confusing behavior. Reassign instead.

**Affected:** `online_sports_revenue`, `debugging_sales_data_workflow` (buggy version)

```python
# Avoid
sports_df.dropna(inplace=True)
data['Condition_1'].fillna(False, inplace=True)

# Prefer
sports_df = sports_df.dropna()
data['Condition_1'] = data['Condition_1'].fillna(False)
```

---

### 6. Redundant `file.close()` inside `with` blocks

The `with` statement automatically closes the file when the block exits. Calling `.close()` manually inside it is redundant.

**Affected:** `avocado_toast_supply_chain`

```python
# Bad
with open("data/relevant_avocado_categories.txt", "r") as file:
    data = file.read().splitlines()
    file.close()  # unnecessary

# Good
with open("data/relevant_avocado_categories.txt", "r") as file:
    data = file.read().splitlines()
```

---

### 7. Reusing variable names

Using the same variable name for different things in the same script makes the code harder to follow and can introduce subtle bugs.

**Affected:** `online_sports_revenue`

```python
# Bad — labels is overwritten later in the same script
labels = ['Budget', 'Average', 'Expensive', 'Elite']
...
labels = ['100', '200', '300', '400', '500', '600', '700']

# Good — use distinct names
price_labels = ['Budget', 'Average', 'Expensive', 'Elite']
...
desc_labels = ['100', '200', '300', '400', '500', '600', '700']
```

---

## Project-Specific Notes

---

### Avocado Toast Supply Chain

**File:** `avocado_toast_supply_chain_analysis/script/avocado_toast_supply_chain.py`

- Whitespace inconsistency: `df =df[subset_columns]` — should be `df = df[subset_columns]`
- Use `os.path.join()` or `pathlib.Path` instead of string concatenation for file paths:

```python
# Instead of
df = pd.read_csv('data/' + filename, ...)

# Prefer
from pathlib import Path
df = pd.read_csv(Path('data') / filename, ...)
```

---

### COVID Workout Analysis

**File:** `covid_workout/script/covid_workout_analysis.py`

- Almost all "answers" are hardcoded strings. The visualizations are generated but the actual analysis conclusions are just typed in.
- The value of this script should come from computing answers, not stating them.
- Example fix:

```python
# Instead of
top_country = "United States"

# Compute it
top_country = df_workout_geo.sum(axis=1).idxmax()
```

---

### Crime in Los Angeles

**File:** `crime_in_los_angeles/script/crime_in_los_angeles.py`

- Good visualization work — the plots are well-labeled.
- Remove commented-out lines before sharing.
- The time conversion (`str.zfill(4).str[:2]`) is clever but add a comment explaining the logic:

```python
# TIME OCC is stored as an integer like 1430 (meaning 14:30)
# Zero-pad to 4 digits, then take first 2 as the hour
crimes["hour"] = crimes["TIME OCC"].astype(str).str.zfill(4).str[:2].astype(int)
```

---

### Customer Purchase Analysis

**File:** `customer_purchase/script/customer_purchase_analysis.py`

- The correlation pair is hardcoded:

```python
# Bad
top_correlation = {'pair': ('Administrative_Duration', 'ProductRelated_Duration'), 'correlation': 0.389855}

# Good — compute it
corr_matrix = shopping_Nov_Dec[['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration']].corr()
# then extract the highest off-diagonal value programmatically
```

- The magic number `0.08` in `plt.vlines(100, 0, 0.08, ...)` should either be a named variable or derived from the data.

---

### Electric Vehicle Charging Trends

**File:** `electric_vehicle_charging_trends/script/electric_vehicles.py`

- `ev_sales_2018 = 361315.0` is assigned but never used.
- `trend = 'same'` at the end is a hardcoded string assigned but never used.
- Remove unused variables, or better yet, compute the trend from the data.

---

### Netflix Movies

**File:** `netflix_movies/script/investigating_netflix_movies.py`

This script needs the most attention:

1. `duration = 100` is hardcoded. The commented-out line above it was the correct approach:
```python
# This was right — just uncomment and use it
duration = filtered_df['duration'].value_counts().idxmax()
```

2. The `for` loop has a useless `else` branch and should be replaced with:
```python
short_movie_count = (action_df['duration'] < 90).sum()
```

---

### Online Sports Revenue

**File:** `online_sports_revenue/script/online_sports_revenue_analysis.py`

- Strong use of `.groupby().agg()` — good pandas practice.
- Rename the second `labels` variable to avoid shadowing the first.
- Avoid `inplace=True` (see recurring issues).

---

### Sleep Health

**File:** `sleep_health/script/sleep_health_data_analysis.py`

The three BMI blocks are nearly identical. Extract into a function:

```python
# Instead of three separate blocks for Normal, Overweight, Obese
def insomnia_ratio(df, bmi_category):
    group = df[df['BMI Category'] == bmi_category]
    return round((group['Sleep Disorder'] == 'Insomnia').sum() / len(group), 2)

bmi_insomnia_ratios = {cat: insomnia_ratio(sleep, cat) for cat in ['Normal', 'Overweight', 'Obese']}
```

---

### Students' Mental Health (SQL)

**File:** `students'_mental_health/script/mental_health_analysis.sql`

- Well-written query. `CAST(stay AS INTEGER)` for correct numeric ordering is a good touch.
- Consider formatting across multiple lines for readability:

```sql
SELECT
    stay,
    COUNT(*) AS count_int,
    ROUND(AVG(todep), 2) AS average_phq,
    ROUND(AVG(tosc), 2) AS average_scs,
    ROUND(AVG(toas), 2) AS average_as
FROM students
WHERE inter_dom = 'Inter'
GROUP BY stay
ORDER BY CAST(stay AS INTEGER) DESC
LIMIT 9;
```

---

## What You're Doing Well

- Appropriate library choices (pandas, matplotlib, seaborn, scipy, SQL)
- Good use of `.groupby()`, `.agg()`, and `.merge()`
- Visualizations are properly labeled with titles and axis labels
- The debugging project shows you can identify and fix bugs systematically
- The keywords generator is clean, minimal, and correct

---

## Top 3 Priorities

1. **Never hardcode analysis results.** Always derive answers from the data. If you hardcode, the code breaks on new data and defeats the whole point.
2. **Clean up before sharing.** Remove commented-out code and unused variables before committing or submitting.
3. **Replace `for` loops over rows with pandas operations.** It's faster, shorter, and the idiomatic way to use pandas.
