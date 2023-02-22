defmodule Day9B do
  def replace(map, a, b, new_value) do
    rows = Enum.count(map)
    cols = Enum.count(Enum.at(map, 0))

    0..(rows - 1)
    |> Enum.map(fn i ->
      0..(cols - 1)
      |> Enum.map(fn j ->
        if i == a and j == b do
          new_value
        else
          Enum.at(Enum.at(map, i), j)
        end
      end)
    end)
  end

  def fill_basin(map, a, b, fill_value) do
    rows = Enum.count(map)
    cols = Enum.count(Enum.at(map, 0))

    map = replace(map, a, b, fill_value)

    map =
      if a > 0 and Enum.at(Enum.at(map, a - 1), b) < 9 do
        fill_basin(map, a - 1, b, fill_value)
      else
        map
      end

    map =
      if a < rows - 1 and Enum.at(Enum.at(map, a + 1), b) < 9 do
        fill_basin(map, a + 1, b, fill_value)
      else
        map
      end

    map =
      if b > 0 and Enum.at(Enum.at(map, a), b - 1) < 9 do
        fill_basin(map, a, b - 1, fill_value)
      else
        map
      end

    map =
      if b < cols - 1 and Enum.at(Enum.at(map, a), b + 1) < 9 do
        fill_basin(map, a, b + 1, fill_value)
      else
        map
      end

    map
  end

  def rename_basins(map, a \\ 0, b \\ 0, current_basin \\ 10) do
    rows = Enum.count(map)
    cols = Enum.count(Enum.at(map, 0))
    # check if we found a basin
    map =
      if Enum.at(Enum.at(map, a), b) < 9 do
        Day9B.fill_basin(map, a, b, current_basin)
      else
        map
      end

    # check if there is a new position and continue
    next_b = b + 1

    next_a =
      if next_b < cols do
        a
      else
        a + 1
      end

    next_b = rem(next_b, cols)

    if next_a < rows do
      rename_basins(map, next_a, next_b, current_basin + 1)
    else
      map
    end
  end
end

{:ok, file} = File.read("inputs/day9.in")

map =
  file
  |> String.split("\n", trim: true)
  |> Enum.map(fn x ->
    String.split(x, "", trim: true)
    |> Enum.map(&String.to_integer/1)
  end)

map
|> Day9B.rename_basins()
|> Enum.flat_map(& &1)
|> Enum.filter(fn x -> x > 9 end)
|> Enum.frequencies()
|> Map.values()
|> Enum.sort()
|> Enum.slice(-3..-1)
|> Enum.reduce(fn x, acc -> x * acc end)
|> IO.inspect(label: "Part 2")
