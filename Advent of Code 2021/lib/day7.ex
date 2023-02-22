defmodule Day7 do
end

{:ok, file} = File.read("inputs/day7.in")

crabs =
  file
  |> String.split(",", trim: true)
  |> Enum.map(&String.to_integer/1)

a = Enum.min(crabs)
b = Enum.max(crabs)

a..b
|> Enum.map(fn x ->
  crabs
  |> Enum.map(fn c -> abs(x - c) end)
  |> Enum.sum()
end)
|> Enum.min()
|> IO.inspect(label: "Part 1")

a..b
|> Enum.map(fn x ->
  crabs
  |> Enum.map(fn c ->
    d = abs(x - c)
    d * (d + 1) / 2
  end)
  |> Enum.sum()
end)
|> Enum.min()
|> IO.inspect(label: "Part 2")
