# python-object_relational_mapping

Scripts that talk to a MySQL server on `localhost:3306`, first with
`MySQLdb` (tasks 0-5) and then with the `SQLAlchemy` ORM (tasks 6-14).

| File | Description |
| ---- | ----------- |
| `0-select_states.py` | List all states (MySQLdb) |
| `1-filter_states.py` | States whose name starts with `N` |
| `2-my_filter_states.py` | States matching an argument (uses `format`, injectable) |
| `3-my_safe_filter_states.py` | Same, safe from SQL injection |
| `4-cities_by_state.py` | All cities with their state name |
| `5-filter_cities.py` | Cities of a given state |
| `model_state.py` | `State` model and `Base` |
| `6-model_state.py` | Creates the `states` table |
| `7-` to `13-model_state_*.py` | Fetch, filter, insert, update and delete states |
| `model_city.py` | `City` model |
| `14-model_city_fetch_by_state.py` | All cities with their state |

Usage: `./0-select_states.py <mysql user> <mysql password> <database>`
(scripts 2, 3, 5 and 10 take a fourth argument: the name to search).
Requires `mysqlclient` 2.0.x and `SQLAlchemy` 1.4.x.
