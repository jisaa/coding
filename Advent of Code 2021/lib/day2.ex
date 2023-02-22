defmodule Day2 do
end

{:ok, file} = File.read("inputs/day2.in")

instructions = String.split(file, "\n", trim: true)

coords =
  instructions
  |> Enum.reduce({0, 0}, fn x, acc ->
    # acc = {x, y}
    [direction, n] = String.split(x)

    case direction do
      "forward" ->
        {elem(acc, 0) + String.to_integer(n), elem(acc, 1)}

      "up" ->
        {elem(acc, 0), elem(acc, 1) - String.to_integer(n)}

      "down" ->
        {elem(acc, 0), elem(acc, 1) + String.to_integer(n)}
    end
  end)

IO.inspect(elem(coords, 0) * elem(coords, 1), label: "Part 1")

coords =
  instructions
  |> Enum.reduce({0, 0, 0}, fn x, acc ->
    # acc = {x, y, aim}
    [direction, n] = String.split(x)

    case direction do
      "forward" ->
        {elem(acc, 0) + String.to_integer(n), elem(acc, 1) + String.to_integer(n) * elem(acc, 2),
         elem(acc, 2)}

      "up" ->
        {elem(acc, 0), elem(acc, 1), elem(acc, 2) - String.to_integer(n)}

      "down" ->
        {elem(acc, 0), elem(acc, 1), elem(acc, 2) + String.to_integer(n)}
    end
  end)

IO.inspect(elem(coords, 0) * elem(coords, 1), label: "Part 2")
