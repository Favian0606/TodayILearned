# Combining Pandas Objects

## Topics
- Appending new rows to DataFrames
- Concatenating multiple DataFrames together
- Comparing President Trump's and Obama's approval ratings
- Understanding the difference between concat, join, and merge
- Connecting to SQL database

## Introduction
- 두 개 이상의 DataFrames 또는 Series를 combine 하는 방법은 다양하게 제공됨
- `append` 메소드는 새로운 rows를 DataFrame에 append
- `concat` 메소드는 다재다능하여 어떤 갯수의 DataFrame이나 Series를 어떤 axis로도 combine 할 수 있음
- `join` 메소드는 DataFrame의 column을 다른 DataFrame의 index에 맞춘 fast lookups을 제공
- `merge` 메소드는 두 개의 DataFrames를 join하는 SQL-like capabilities를 제공

## References
- Pandas official documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html