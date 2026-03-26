# SQL Challenges for `football_club` and `player` — Solutions

These are example SQL solutions for the challenge file.

> Notes:
> - These queries are written for SQLite.
> - Your table uses the column name `mananger` exactly as defined in your schema.
> - `founded` is stored as `TEXT`, so these solutions cast it to `INT` when comparing years.

---

# Part 1: Solutions Using `football_club` Only

## Challenge 1
```sql
SELECT * FROM football_club;
```

## Challenge 2
```sql
SELECT team_name, city
FROM football_club;
```

## Challenge 3
```sql
SELECT *
FROM football_club
WHERE city = 'London';
```

## Challenge 4
```sql
SELECT COUNT(*) AS london_clubs
FROM football_club
WHERE city = 'London';
```

## Challenge 5
```sql
SELECT *
FROM football_club
WHERE home_kit_colour LIKE '%Red%';
```

## Challenge 6
```sql
SELECT COUNT(*) AS red_teams
FROM football_club
WHERE home_kit_colour LIKE '%Red%';
```

## Challenge 7
```sql
SELECT *
FROM football_club
ORDER BY CAST(founded AS INT) ASC
LIMIT 1;
```

## Challenge 8
```sql
SELECT *
FROM football_club
ORDER BY CAST(founded AS INT) DESC
LIMIT 1;
```

## Challenge 9
```sql
SELECT *
FROM football_club
ORDER BY team_name;
```

## Challenge 10
```sql
SELECT *
FROM football_club
ORDER BY CAST(founded AS INT);
```

## Challenge 11
```sql
SELECT DISTINCT city
FROM football_club;
```

## Challenge 12
```sql
SELECT COUNT(DISTINCT city) AS city_count
FROM football_club;
```

## Challenge 13
```sql
SELECT *
FROM football_club
WHERE home_kit_colour LIKE '%Blue%';
```

## Challenge 14
```sql
SELECT COUNT(*) AS white_kit_teams
FROM football_club
WHERE home_kit_colour LIKE '%White%';
```

## Challenge 15
```sql
SELECT mananger
FROM football_club;
```

## Challenge 16
```sql
SELECT *
FROM football_club
WHERE CAST(founded AS INT) < 1900;
```

## Challenge 17
```sql
SELECT team_name, city, mananger
FROM football_club
WHERE city = 'London';
```

## Challenge 18
```sql
SELECT city, COUNT(*) AS club_count
FROM football_club
GROUP BY city;
```

## Challenge 19
```sql
SELECT *
FROM football_club
ORDER BY CAST(founded AS INT)
LIMIT 5;
```

## Challenge 20
```sql
SELECT *
FROM football_club
ORDER BY CAST(founded AS INT) DESC
LIMIT 5;
```

---

# Part 2: Solutions Using `player` Only

## Challenge 21
```sql
SELECT * FROM player;
```

## Challenge 22
```sql
SELECT player_name, position, team_name
FROM player;
```

## Challenge 23
```sql
SELECT *
FROM player
WHERE position = 'Goalkeeper';
```

## Challenge 24
```sql
SELECT *
FROM player
WHERE nationality = 'England';
```

## Challenge 25
```sql
SELECT COUNT(*) AS english_players
FROM player
WHERE nationality = 'England';
```

## Challenge 26
```sql
SELECT *
FROM player
WHERE predominant_foot = 'Left';
```

## Challenge 27
```sql
SELECT COUNT(*) AS right_footed_players
FROM player
WHERE predominant_foot = 'Right';
```

## Challenge 28
```sql
SELECT *
FROM player
ORDER BY age DESC;
```

## Challenge 29
```sql
SELECT *
FROM player
ORDER BY age ASC;
```

## Challenge 30
```sql
SELECT *
FROM player
ORDER BY age DESC
LIMIT 1;
```

## Challenge 31
```sql
SELECT *
FROM player
ORDER BY age ASC
LIMIT 1;
```

## Challenge 32
```sql
SELECT COUNT(*) AS total_players
FROM player;
```

## Challenge 33
```sql
SELECT position, COUNT(*) AS player_count
FROM player
GROUP BY position;
```

## Challenge 34
```sql
SELECT nationality, COUNT(*) AS player_count
FROM player
GROUP BY nationality
ORDER BY player_count DESC;
```

## Challenge 35
```sql
SELECT *
FROM player
WHERE player_name LIKE 'A%';
```

## Challenge 36
```sql
SELECT *
FROM player
WHERE year_of_birth > 2000;
```

## Challenge 37
```sql
SELECT *
FROM player
WHERE age BETWEEN 20 AND 25;
```

## Challenge 38
```sql
SELECT DISTINCT nationality
FROM player;
```

## Challenge 39
```sql
SELECT COUNT(DISTINCT nationality) AS nationality_count
FROM player;
```

## Challenge 40
```sql
SELECT team_name, COUNT(*) AS player_count
FROM player
GROUP BY team_name;
```

---

# Part 3: Join Solutions Using Both Tables

## Challenge 41
```sql
SELECT p.player_name, p.team_name, f.city
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name;
```

## Challenge 42
```sql
SELECT p.player_name, p.team_name, f.mananger
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name;
```

## Challenge 43
```sql
SELECT p.*
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
WHERE f.city = 'London';
```

## Challenge 44
```sql
SELECT COUNT(*) AS london_players
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
WHERE f.city = 'London';
```

## Challenge 45
```sql
SELECT p.player_name, p.team_name
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
WHERE f.home_kit_colour LIKE '%Red%';
```

## Challenge 46
```sql
SELECT f.city, COUNT(*) AS player_count
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
GROUP BY f.city;
```

## Challenge 47
```sql
SELECT p.player_name, p.age, p.position, p.team_name, f.city
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name;
```

## Challenge 48
```sql
SELECT p.player_name, p.age, p.team_name
FROM player p
ORDER BY p.age DESC
LIMIT 1;
```

## Challenge 49
```sql
SELECT p.player_name, p.age, p.team_name
FROM player p
ORDER BY p.age ASC
LIMIT 1;
```

## Challenge 50
```sql
SELECT p.player_name, p.team_name, f.city
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
WHERE p.position = 'Goalkeeper';
```

## Challenge 51
```sql
SELECT p.player_name, p.team_name, f.mananger
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
WHERE p.nationality = 'England';
```

## Challenge 52
```sql
SELECT f.team_name, COUNT(p.player_id) AS player_count
FROM football_club f
LEFT JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.team_name;
```

## Challenge 53
```sql
SELECT f.team_name, AVG(p.age) AS average_age
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.team_name;
```

## Challenge 54
```sql
SELECT f.team_name, AVG(p.age) AS average_age
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.team_name
ORDER BY average_age DESC
LIMIT 1;
```

## Challenge 55
```sql
SELECT f.team_name, AVG(p.age) AS average_age
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.team_name
ORDER BY average_age ASC
LIMIT 1;
```

## Challenge 56
```sql
SELECT p.team_name, p.position, COUNT(*) AS player_count
FROM player p
GROUP BY p.team_name, p.position
ORDER BY p.team_name, p.position;
```

## Challenge 57
```sql
SELECT f.team_name, p.player_name
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
WHERE f.city = 'London'
ORDER BY f.team_name, p.player_name;
```

## Challenge 58
```sql
SELECT f.city, COUNT(*) AS total_players
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.city;
```

## Challenge 59
```sql
SELECT p.player_name, p.team_name
FROM player p
JOIN football_club f
  ON p.team_name = f.team_name
WHERE CAST(f.founded AS INT) < 1900;
```

## Challenge 60
```sql
SELECT f.mananger, COUNT(p.player_id) AS squad_size
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.mananger;
```

---

# Part 4: Aggregation and Filtering Solutions

## Challenge 61
```sql
SELECT nationality, COUNT(*) AS player_count
FROM player
GROUP BY nationality
ORDER BY player_count DESC
LIMIT 1;
```

## Challenge 62
```sql
SELECT position, COUNT(*) AS player_count
FROM player
GROUP BY position
ORDER BY player_count DESC
LIMIT 1;
```

## Challenge 63
```sql
SELECT city, COUNT(*) AS club_count
FROM football_club
GROUP BY city
ORDER BY club_count DESC
LIMIT 1;
```

## Challenge 64
```sql
SELECT f.city, COUNT(*) AS player_count
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.city
ORDER BY player_count DESC
LIMIT 1;
```

## Challenge 65
```sql
SELECT team_name, COUNT(*) AS goalkeeper_count
FROM player
WHERE position = 'Goalkeeper'
GROUP BY team_name
HAVING COUNT(*) > 2;
```

## Challenge 66
```sql
SELECT team_name, COUNT(*) AS defender_count
FROM player
WHERE position LIKE '%Back%' OR position = 'Centre-Back'
GROUP BY team_name
HAVING COUNT(*) >= 3;
```

## Challenge 67
```sql
SELECT nationality, AVG(age) AS average_age
FROM player
GROUP BY nationality
ORDER BY average_age DESC;
```

## Challenge 68
```sql
SELECT team_name, AVG(age) AS average_age
FROM player
GROUP BY team_name
HAVING AVG(age) > (SELECT AVG(age) FROM player);
```

## Challenge 69
```sql
SELECT p.player_name, p.team_name, p.age
FROM player p
WHERE p.age > (
    SELECT AVG(p2.age)
    FROM player p2
    WHERE p2.team_name = p.team_name
);
```

## Challenge 70
```sql
SELECT p.player_name, p.team_name, p.age
FROM player p
WHERE p.age < (
    SELECT AVG(p2.age)
    FROM player p2
    WHERE p2.team_name = p.team_name
);
```

---

# Part 5: `GROUP BY`, `HAVING`, and Subquery Solutions

## Challenge 71
```sql
SELECT nationality, COUNT(*) AS player_count
FROM player
GROUP BY nationality
HAVING COUNT(*) > 5;
```

## Challenge 72
```sql
SELECT city, COUNT(*) AS club_count
FROM football_club
GROUP BY city
HAVING COUNT(*) > 1;
```

## Challenge 73
```sql
SELECT team_name, COUNT(*) AS squad_size
FROM player
GROUP BY team_name
HAVING COUNT(*) = 10;
```

## Challenge 74
```sql
SELECT team_name, AVG(age) AS average_age
FROM player
GROUP BY team_name
HAVING AVG(age) > 27;
```

## Challenge 75
```sql
SELECT position
FROM player
GROUP BY position
HAVING COUNT(DISTINCT team_name) = (SELECT COUNT(*) FROM football_club);
```

## Challenge 76
```sql
SELECT p.player_name, p.team_name, p.age
FROM player p
WHERE p.age = (
    SELECT MAX(p2.age)
    FROM player p2
    WHERE p2.team_name = p.team_name
);
```

## Challenge 77
```sql
SELECT p.player_name, p.team_name, p.age
FROM player p
WHERE p.age = (
    SELECT MIN(p2.age)
    FROM player p2
    WHERE p2.team_name = p.team_name
);
```

## Challenge 78
```sql
SELECT mananger
FROM football_club
WHERE CAST(founded AS INT) = (
    SELECT MIN(CAST(founded AS INT))
    FROM football_club
);
```

## Challenge 79
```sql
SELECT mananger
FROM football_club
WHERE CAST(founded AS INT) = (
    SELECT MAX(CAST(founded AS INT))
    FROM football_club
);
```

## Challenge 80
```sql
SELECT DISTINCT f.city
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
WHERE p.nationality = 'Brazil';
```

---

# Part 6: Update, Insert, and Delete Practice Solutions

## Challenge 81
```sql
INSERT INTO football_club (team_name, city, home_kit_colour, founded, mananger)
VALUES ('Sample FC', 'Sample City', 'Green', '2000', 'Sample Manager');
```

## Challenge 82
```sql
INSERT INTO player (
    player_id, player_name, year_of_birth, predominant_foot, position,
    nationality, age, team_name
) VALUES (
    'SMP_01', 'Sample Player', 2001, 'Right', 'Midfielder',
    'England', 25, 'Sample FC'
);
```

## Challenge 83
```sql
UPDATE football_club
SET home_kit_colour = 'Dark Blue'
WHERE team_name = 'Chelsea';
```

## Challenge 84
```sql
UPDATE player
SET predominant_foot = 'Right'
WHERE predominant_foot = 'Unknown';
```

## Challenge 85
```sql
UPDATE player
SET age = age + 1;
```

## Challenge 86
```sql
DELETE FROM player
WHERE player_id = 'SMP_01';
```

## Challenge 87
```sql
DELETE FROM player
WHERE team_name = 'Sample FC';
```

## Challenge 88
```sql
UPDATE football_club
SET mananger = 'New Manager Name'
WHERE team_name = 'West Ham United';
```

## Challenge 89
```sql
UPDATE football_club
SET city = 'New City'
WHERE team_name = 'Sample FC';
```

## Challenge 90
```sql
SELECT *
FROM player
WHERE team_name = 'Sample FC';
```

---

# Part 7: Plain English Question Solutions

## Challenge 91
```sql
SELECT team_name
FROM football_club
ORDER BY CAST(founded AS INT)
LIMIT 1;
```

## Challenge 92
```sql
SELECT team_name
FROM football_club
ORDER BY CAST(founded AS INT) DESC
LIMIT 1;
```

## Challenge 93
```sql
SELECT COUNT(*) AS red_teams
FROM football_club
WHERE home_kit_colour LIKE '%Red%';
```

## Challenge 94
```sql
SELECT COUNT(*) AS london_teams
FROM football_club
WHERE city = 'London';
```

## Challenge 95
```sql
SELECT COUNT(*) AS goalkeeper_count
FROM player
WHERE position = 'Goalkeeper';
```

## Challenge 96
```sql
SELECT COUNT(*) AS english_player_count
FROM player
WHERE nationality = 'England';
```

## Challenge 97
```sql
SELECT team_name, AVG(age) AS average_age
FROM player
GROUP BY team_name
ORDER BY average_age DESC
LIMIT 1;
```

## Challenge 98
```sql
SELECT team_name, AVG(age) AS average_age
FROM player
GROUP BY team_name
ORDER BY average_age ASC
LIMIT 1;
```

## Challenge 99
```sql
SELECT nationality, COUNT(*) AS player_count
FROM player
GROUP BY nationality
ORDER BY player_count DESC
LIMIT 1;
```

## Challenge 100
```sql
SELECT f.mananger, COUNT(p.player_id) AS squad_size
FROM football_club f
JOIN player p
  ON f.team_name = p.team_name
GROUP BY f.mananger
ORDER BY squad_size DESC
LIMIT 1;
```

---

# Optional Tip

To test queries safely:
- start with `SELECT`
- preview rows before `UPDATE` or `DELETE`
- use `LIMIT` while experimenting

Good luck — this set covers selection, filtering, sorting, joins, grouping, subqueries, and data modification.

