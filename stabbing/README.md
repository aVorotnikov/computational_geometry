# Триангуляция протыканий
Осуществляется подсчёт числа протыканий триангуляций выпуклого многоугольника

## Вход
Вход состоит из `n-2` строк которые задают триангуляцию `n`-угольника. Каждая строка содержит три индекса вершин.
Требования к индексам:
+ индексация начинается с `0`
+ последний индекс - `n-1`
+ вершины индексируются против часовой стрелки

**Пример.** Четырёхугольник с диагональю 0-2:
```
0 1 2
0 2 3
```

## Выход
Одно челое число - число протыканий.

**Пример.**
0