# Триангуляция протыканий
Осуществляется подсчёт числа протыканий триангуляций выпуклого многоугольника

## Вход
Вход состоит из `n` строк которые задают триангуляцию `n`-угольника. Каждая строка содержит:
1. Индекс вершины
2. Индексы смежных в триангуляции вершины

Строки следуют в порядке обхода вершин - сначала описывается 0, затем 1-ая и т.д.

Требования к индексам:
+ индексация начинается с `0`
+ последний индекс - `n-1`
+ вершины индексируются против часовой стрелки

**Пример.** Четырёхугольник с диагональю 0-2:
```
0 2
1
2 0
3
```
Пятиугольник с диагоналями 0-2 и 0-3:
```
0 2 3
1
2 0
3 0
4
```

## Выход
Одно челое число - число протыканий.

**Пример.**
0
