defmodule Day10 do
  def points_or_stack(line, stack \\ [], return_stack \\ false) do
    if String.length(line) == 0 do
      if return_stack do
        stack
        |> Enum.join()
      else
        0
      end
    else
      remainder = line |> String.slice(1..-1)

      case String.at(line, 0) do
        "(" ->
          Day10.points_or_stack(remainder, [")"] ++ stack, return_stack)

        "[" ->
          Day10.points_or_stack(remainder, ["]"] ++ stack, return_stack)

        "{" ->
          Day10.points_or_stack(remainder, ["}"] ++ stack, return_stack)

        "<" ->
          Day10.points_or_stack(remainder, [">"] ++ stack, return_stack)

        other ->
          if Enum.at(stack, 0) == other do
            Day10.points_or_stack(remainder, Enum.slice(stack, 1..-1), return_stack)
          else
            Map.get(%{")" => 3, "]" => 57, "}" => 1197, ">" => 25137}, other)
          end
      end
    end
  end

  def remainder_score(remainder, score \\ 0) do
    if String.length(remainder) == 0 do
      score
    else
      new_score =
        5 * score + Map.get(%{")" => 1, "]" => 2, "}" => 3, ">" => 4}, String.at(remainder, 0))

      remainder_score(String.slice(remainder, 1..-1), new_score)
    end
  end
end

{:ok, file} = File.read("inputs/day10.in")

lines =
  file
  |> String.split("\n", trim: true)

lines
|> Enum.map(&Day10.points_or_stack/1)
|> Enum.sum()
|> IO.inspect(label: "Part 1")

remainder_scores =
  lines
  |> Enum.filter(fn x -> Day10.points_or_stack(x) == 0 end)
  |> Enum.map(fn x -> Day10.points_or_stack(x, [], true) end)
  |> Enum.map(&Day10.remainder_score/1)
  |> Enum.sort()

remainder_scores
|> Enum.at(div(Enum.count(remainder_scores), 2))
|> IO.inspect(label: "Part 2")
