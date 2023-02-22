defmodule Day1 do
end

{:ok, file} = File.read("inputs/day1.in")

depths =
  String.split(file)
  |> Enum.map(&String.to_integer/1)

depths
|> Enum.reduce({0, Enum.at(depths, 0)}, fn x, acc ->
  # acc = {n_increases, prev_depth}
  if elem(acc, 1) < x do
    {elem(acc, 0) + 1, x}
  else
    {elem(acc, 0), x}
  end
end)
|> elem(0)
|> IO.inspect(label: 'Part 1')

depths
|> Enum.reduce({0, Enum.at(depths, 0), Enum.at(depths, 0), Enum.at(depths, 0)}, fn x, acc ->
  # acc = {n_increases, prev_depth, prev_depth, prev_depth}
  if elem(acc, 1) + elem(acc, 2) + elem(acc, 3) < elem(acc, 2) + elem(acc, 3) + x do
    {elem(acc, 0) + 1, elem(acc, 2), elem(acc, 3), x}
  else
    {elem(acc, 0), elem(acc, 2), elem(acc, 3), x}
  end
end)
|> elem(0)
|> IO.inspect(label: 'Part 2')
