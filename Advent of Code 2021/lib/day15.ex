defmodule Day15 do
  def update_lower_row(danger) do
    lower = Enum.at(danger, -1)

    new_lower =
      0..(Enum.count(lower) - 1)
      |> Enum.map(fn i ->
        lower
        |> Enum.slice(i..-1)
        |> Enum.sum()
      end)

    Enum.slice(danger, 0..-2) ++ [new_lower]
  end

  def update_right_col(danger) do
    0..(Enum.count(danger) - 1)
    |> Enum.map(fn i ->
      row = Enum.at(danger, i)

      new_last =
        Enum.slice(danger, i..-1)
        |> Enum.map(fn x -> Enum.at(x, -1) end)
        |> Enum.sum()

      Enum.slice(row, 0..-2) ++ [new_last]
    end)
  end

  def update_rest(danger, i, j) do
    if i < 0 do
      danger
    else
      row = Enum.at(danger, i)

      new_val =
        Enum.at(Enum.at(danger, i), j) +
          Enum.min([
            Enum.at(Enum.at(danger, i + 1), j),
            Enum.at(Enum.at(danger, i), j + 1)
          ])

      new_row =
        if j > 0 do
          Enum.slice(row, 0..(j - 1)) ++ [new_val] ++ Enum.slice(row, (j + 1)..-1)
        else
          [new_val] ++ Enum.slice(row, (j + 1)..-1)
        end

      new_danger =
        if i > 0 do
          Enum.slice(danger, 0..(i - 1)) ++ [new_row] ++ Enum.slice(danger, (i + 1)..-1)
        else
          [new_row] ++ Enum.slice(danger, (i + 1)..-1)
        end

      if j == 0 do
        Day15.update_rest(new_danger, i - 1, Enum.count(Enum.at(danger, 0)) - 2)
      else
        Day15.update_rest(new_danger, i, j - 1)
      end
    end
  end
end

{:ok, file} = File.read("inputs/day15.in")

danger =
  file
  |> String.split("\n", trim: true)
  |> Enum.map(fn s ->
    s
    |> String.split("", trim: true)
    |> Enum.map(&String.to_integer/1)
  end)

# no danger at start
danger = [[0] ++ Enum.slice(Enum.at(danger, 0), 1..-1)] ++ Enum.slice(danger, 1..-1)

danger
|> Day15.update_lower_row()
|> Day15.update_right_col()
|> Day15.update_rest(Enum.count(danger) - 2, Enum.count(Enum.at(danger, 0)) - 2)
|> Enum.at(0)
|> Enum.at(0)
|> IO.inspect(label: "Part 1")

42
|> IO.inspect(label: "Part 2")
