# SQL - Introduction

Introductory MySQL 8.0 scripts: creating and removing databases and tables,
inserting, selecting, updating and deleting rows, and basic aggregation.

Run a script with, for example:

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

| File | Description |
| --- | --- |
| 0-list_databases.sql | Lists all databases |
| 1-create_database_if_missing.sql | Creates `hbtn_0c_0` if missing |
| 2-remove_database.sql | Drops `hbtn_0c_0` if it exists |
| 3-list_tables.sql | Lists tables of a database |
| 4-first_table.sql | Creates `first_table` |
| 5-full_table.sql | Prints full description of `first_table` |
| 6-list_values.sql | Lists all rows of `first_table` |
| 7-insert_value.sql | Inserts (89, Best School) |
| 8-count_89.sql | Counts rows with id = 89 |
| 9-full_creation.sql | Creates `second_table` with rows |
| 10-top_score.sql | Records ordered by score |
| 11-best_score.sql | Records with score >= 10 |
| 12-no_cheating.sql | Sets Bob's score to 10 |
| 13-change_class.sql | Deletes records with score <= 5 |
| 14-average.sql | Average score |
| 15-groups.sql | Number of records per score |
| 16-no_link.sql | Records with a name, by score |
