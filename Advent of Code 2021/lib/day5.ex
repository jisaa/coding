defmodule Day5 do
end

{:ok, file} = File.read("inputs/day5.in")

lines =
  file
  |> String.split("\n", trim: true)
  |> Enum.map(fn x ->
    String.split(x, [",", " -> "])
    |> Enum.map(&String.to_integer/1)
  end)

lines
|> Enum.map(fn [x1, y1, x2, y2] ->
  if x1 == x2 do
    y1..y2
    |> Enum.map(fn y -> 1000 * x1 + y end)
  else
    if y1 == y2 do
      x1..x2
      |> Enum.map(fn x -> 1000 * x + y1 end)
    else
      []
    end
  end
end)
|> Enum.flat_map(& &1)
|> Enum.frequencies()
|> Enum.filter(fn x -> elem(x, 1) > 1 end)
|> Enum.count()
|> IO.inspect(label: "Part 1")

lines
|> Enum.map(fn [x1, y1, x2, y2] ->
  if x1 == x2 do
    y1..y2
    |> Enum.map(fn y -> 1000 * x1 + y end)
  else
    if y1 == y2 do
      x1..x2
      |> Enum.map(fn x -> 1000 * x + y1 end)
    else
      dy =
        if y1 < y2 do
          1
        else
          -1
        end

      x1..x2
      |> Enum.with_index()
      |> Enum.map(fn {x, i} ->
        1000 * x + y1 + i * dy
      end)
    end
  end
end)
|> Enum.flat_map(& &1)
|> Enum.frequencies()
|> Enum.filter(fn x -> elem(x, 1) > 1 end)
|> Enum.count()
|> IO.inspect(label: "Part 2")
