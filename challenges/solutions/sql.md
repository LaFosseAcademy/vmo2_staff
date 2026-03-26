# SQL Challenges for `football_club` and `player`

These SQL challenges are based on the two tables in your database:

## Table: `football_club`

```sql
team_name TEXT PRIMARY KEY
city TEXT NOT NULL
home_kit_colour TEXT NOT NULL
founded TEXT NOT NULL
mananger TEXT NOT NULL
```

## Table: `player`

```sql
player_id TEXT PRIMARY KEY
player_name TEXT NOT NULL
year_of_birth INT NOT NULL
predominant_foot TEXT NOT NULL
position TEXT NOT NULL
nationality TEXT NOT NULL
age INT NOT NULL
team_name TEXT NOT NULL
```

---

# Part 1: Challenges Using `football_club` Only

## Challenge 1
Select all columns from the `football_club` table.

---

## Challenge 2
Show only the `team_name` and `city` columns for every club.

---

## Challenge 3
Find all clubs based in **London**.

---

## Challenge 4
Count how many clubs are based in **London**.

---

## Challenge 5
Find all clubs whose `home_kit_colour` contains the word **Red**.

### Tip

Use `LIKE`: https://www.w3schools.com/sql/sql_like.asp

---

## Challenge 6
Count how many clubs play in **Red**.

---

## Challenge 7
Find the **oldest team** using the `founded` column.

### Tip

Use `CAST`: https://www.w3schools.com/sql/func_sqlserver_cast.asp

---

## Challenge 8
Find the **newest team** using the `founded` column.

---

## Challenge 9
List all clubs in alphabetical order by `team_name`.

---

## Challenge 10
List all clubs ordered by founding year from oldest to newest.

---

## Challenge 11
Show all different cities that clubs come from.

---

## Challenge 12
Count how many different cities are represented in the table.

### Tip

Use `DISTINCT`: https://www.w3schools.com/sql/sql_distinct.asp

---

## Challenge 13
Find all clubs whose `home_kit_colour` contains **Blue**.

---

## Challenge 14
Count how many clubs have **White** somewhere in their home kit colour.

---

## Challenge 15
Return the manager names for all clubs.

---

## Challenge 16
Find all clubs founded before **1900**.

---

## Challenge 17
Find all clubs founded in **London** and show their manager names too.

---

## Challenge 18
Show the number of clubs in each city.

---

## Challenge 19
Show the oldest 5 clubs.

---

## Challenge 20
Show the newest 5 clubs.

---

# Part 2: Challenges Using `player` Only

## Challenge 21
Select all columns from the `player` table.

---

## Challenge 22
Show only `player_name`, `position`, and `team_name`.

---

## Challenge 23
Find all players who are **Goalkeepers**.

---

## Challenge 24
Find all players whose nationality is **England**.

---

## Challenge 25
Count how many players are from **England**.

---

## Challenge 26
Find all players who are **Left** footed.

---

## Challenge 27
Count how many players are **Right** footed.

---

## Challenge 28
Show all players ordered from oldest to youngest using `age`.

---

## Challenge 29
Show all players ordered from youngest to oldest.

---

## Challenge 30
Find the oldest player in the table.

---

## Challenge 31
Find the youngest player in the table.

---

## Challenge 32
Count how many players there are in total.

---

## Challenge 33
Show how many players play in each position.

---

## Challenge 34
Show how many players each nationality has in the table.

---

## Challenge 35
Find all players whose `player_name` starts with the letter **A**.

---

## Challenge 36
Find all players born after **2000**.

---

## Challenge 37
Find all players aged between **20 and 25**.

### Tip

Use `BETWEEN`: https://www.w3schools.com/sql/sql_between.asp

---

## Challenge 38
Find all distinct player nationalities.

---

## Challenge 39
Count how many distinct nationalities are in the player table.

---

## Challenge 40
Show how many players each team has.

---

# Part 3: Join Challenges Using Both Tables

## Challenge 41
Join `player` and `football_club` and show:

- `player_name`
- `team_name`
- `city`

---

## Challenge 42
Show every player and their club manager.

---

## Challenge 43
Show all players who play for clubs in **London**.

---

## Challenge 44
Count how many players play for clubs in **London**.

---

## Challenge 45
Show all players who play for clubs whose home kit colour contains **Red**.

---

## Challenge 46
Count how many players belong to each city.

---

## Challenge 47
Show each player with:

- player name
- age
- position
- club name
- club city

---

## Challenge 48
Find the oldest player and also show the club they play for.

---

## Challenge 49
Find the youngest player and also show the club they play for.

---

## Challenge 50
Show all goalkeepers and the city of the club they play for.

---

## Challenge 51
Show all English players and the managers of their clubs.

---

## Challenge 52
Show all clubs and how many players they have, using a `JOIN`.

---

## Challenge 53
Show the average player age for each club.

---

## Challenge 54
Find the club with the oldest average squad age.

---

## Challenge 55
Find the club with the youngest average squad age.

---

## Challenge 56
Show the number of players in each position for each club.

---

## Challenge 57
Show all clubs in London and list the players in those clubs.

---

## Challenge 58
Show each city and the total number of players playing for clubs in that city.

---

## Challenge 59
Find all players who play for clubs founded before **1900**.

---

## Challenge 60
Show all managers and how many players are in their squad.

---

# Part 4: Slightly Harder Aggregation and Filtering Challenges

## Challenge 61
Find the nationality with the highest number of players.

---

## Challenge 62
Find the most common player position.

---

## Challenge 63
Find which city has the most clubs.

---

## Challenge 64
Find which city has the most players.

---

## Challenge 65
Show clubs that have more than 2 goalkeepers.

---

## Challenge 66
Show clubs that have at least 3 defenders.

---

## Challenge 67
Find the average age of players by nationality.

---

## Challenge 68
Find all clubs whose average player age is above the overall average player age.

---

## Challenge 69
Find players older than the average age of players in their own team.

---

## Challenge 70
Find players younger than the average age of players in their own team.

---

# Part 5: Challenge Ideas with `GROUP BY`, `HAVING`, and Subqueries

## Challenge 71
Show all nationalities that have more than 5 players.

---

## Challenge 72
Show all cities with more than 1 club.

---

## Challenge 73
Find the clubs whose squad size is exactly 10 players.

---

## Challenge 74
Find clubs with an average age greater than 27.

---

## Challenge 75
Find positions that appear in every club.

---

## Challenge 76
Find all players who are the oldest in their team.

### Tip

Use `MAX`: https://www.w3schools.com/SQl/sql_max.asp

---

## Challenge 77
Find all players who are the youngest in their team.

### Tip

Use `MIN`: https://www.w3schools.com/sql/sql_min_max.asp

---

## Challenge 78
Find the manager of the oldest club.

---

## Challenge 79
Find the manager of the newest club.

---

## Challenge 80
Find the cities of clubs that have at least one player from Brazil.

---

# Part 6: Update, Insert, and Delete Practice

Only run these if you are happy to modify your database.

## Challenge 81
Insert a new club into `football_club`.

---

## Challenge 82
Insert a new player into `player`.

---

## Challenge 83
Update the `home_kit_colour` of one club.

---

## Challenge 84
Update the `predominant_foot` of all players where it is `'Unknown'`.

---

## Challenge 85
Increase the `age` of every player by 1.

---

## Challenge 86
Delete one player by `player_id`.

---

## Challenge 87
Delete all players from one team.

---

## Challenge 88
Rename one manager in the `football_club` table.

---

## Challenge 89
Change the city for one club.

---

## Challenge 90
Set up a query to safely preview rows before deleting them.

---

# Part 7: Challenge Questions in Plain English

Try writing SQL for these without looking at any answers.

## Challenge 91
Which team is the oldest?

## Challenge 92
Which team is the newest?

## Challenge 93
How many teams play in red?

## Challenge 94
How many teams are based in London?

## Challenge 95
How many players are goalkeepers?

## Challenge 96
How many players are English?

## Challenge 97
Which club has the oldest squad on average?

## Challenge 98
Which club has the youngest squad on average?

## Challenge 99
Which nationality appears most often?

## Challenge 100
Which manager has the largest squad?

---

# Optional Extension

After completing the challenges, try writing your own:

- one `SELECT` challenge
- one `JOIN` challenge
- one `GROUP BY` challenge
- one `subquery` challenge
- one `UPDATE` challenge

---

Good luck — these exercises cover filtering, sorting, grouping, joins, aggregation, and real database practice.

