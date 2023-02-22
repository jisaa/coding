defmodule Day9 do
  def missing_or_higher(map, i, j, h) do
    if i < 0 or i >= Enum.count(map) or j < 0 or j >= Enum.count(Enum.at(map, 0)) do
      # missing
      true
    else
      x =
        map
        |> Enum.at(i)
        |> Enum.at(j)

      x > h
    end
  end

  def is_low(map, i, j) do
    h =
      map
      |> Enum.at(i)
      |> Enum.at(j)

    if Day9.missing_or_higher(map, i - 1, j, h) and Day9.missing_or_higher(map, i + 1, j, h) and
         Day9.missing_or_higher(map, i, j - 1, h) and Day9.missing_or_higher(map, i, j + 1, h) do
      h + 1
    else
      0
    end
  end

  def get_basin_index(map) do
    rows_with_basins =
      map
      |> Enum.with_index()
      |> Enum.filter(fn {row, _index} ->
        row
        |> Enum.any?(fn x -> x < 9 end)
      end)

    if Enum.count(rows_with_basins) do
      {row, row_index} =
        rows_with_basins
        |> Enum.at(0)

      {row_index, Enum.find_index(row, fn x -> x < 9 end)}
    else
      nil
    end
  end

  def is_part_of_the_same_basin(map, i, j) do
    if i < 0 or i >= Enum.count(map) or j < 0 or j >= Enum.count(Enum.at(map, 0)) do
      false
    else
      Enum.at(Enum.at(map, i), j) < 9
    end
  end

  def fill_space(map, a, b) do
    rows = Enum.count(map)
    cols = Enum.count(Enum.at(map, 0))

    0..(rows - 1)
    |> Enum.map(fn i ->
      0..(cols - 1)
      |> Enum.map(fn j ->
        if i == a and j == b do
          9
        else
          Enum.at(Enum.at(map, i), j)
        end
      end)
    end)
  end

  def fill_basin(map, q, size \\ 0) do
    if Enum.count(q) == 0 do
      {map, size}
    else
      {i, j} = Enum.at(q, 0)
      new_q = Enum.slice(q, 1..-1)
      map = Day9.fill_space(map, i, j)

      {map, size} =
        if Day9.is_part_of_the_same_basin(map, i + 1, j) do
          fill_basin(map, new_q ++ [{i + 1, j}], size + 1)
        else
          {map, size}
        end

      {map, size} =
        if Day9.is_part_of_the_same_basin(map, i, j + 1) do
          fill_basin(map, new_q ++ [{i, j + 1}], size + 1)
        else
          {map, size}
        end

      {map, size} =
        if Day9.is_part_of_the_same_basin(map, i - 1, j) do
          fill_basin(map, new_q ++ [{i - 1, j}], size + 1)
        else
          {map, size}
        end

      {map, size} =
        if Day9.is_part_of_the_same_basin(map, i, j - 1) do
          fill_basin(map, new_q ++ [{i, j - 1}], size + 1)
        else
          {map, size}
        end

      {map, size + 1}
    end
  end

  # get size of a random basin
  def get_basin_size(map) do
    case Day9.get_basin_index(map) do
      nil ->
        0

      coords ->
        fill_basin(map, [coords])
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

rows = Enum.count(map)
cols = Enum.count(Enum.at(map, 0))

0..(rows - 1)
|> Enum.map(fn i ->
  0..(cols - 1)
  |> Enum.map(fn j ->
    Day9.is_low(map, i, j)
  end)
end)
|> Enum.flat_map(fn x -> x end)
|> Enum.sum()
|> IO.inspect(label: "Part 1")

map
|> Day9.get_basin_size()
|> IO.inspect(label: "Part 2")
