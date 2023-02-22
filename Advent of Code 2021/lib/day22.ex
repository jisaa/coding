defmodule Day22 do
  def process([instruction, x1, x2, y1, y2, z1, z2], cubes_on \\ MapSet.new(), limit \\ true) do
    coords =
      if limit do
        x1 = max(-50, x1)
        x2 = min(50, x2)
        y1 = max(-50, y1)
        y2 = min(50, y2)
        z1 = max(-50, z1)
        z2 = min(50, z2)

        if x1 <= x2 and y1 <= y2 and z1 <= z2 do
          for x <- x1..x2 do
            for y <- y1..y2 do
              for z <- z1..z2 do
                [x, y, z]
              end
            end
          end
        else
          []
        end
      else
        for x <- x1..x2 do
          for y <- y1..y2 do
            for z <- z1..z2 do
              [x, y, z]
            end
          end
        end
      end
      |> Enum.flat_map(& &1)
      |> Enum.flat_map(& &1)

    if instruction == "on" do
      coords
      |> Enum.reduce(
        cubes_on,
        fn c, acc ->
          MapSet.put(acc, c)
        end
      )
    else
      coords
      |> Enum.reduce(
        cubes_on,
        fn c, acc ->
          MapSet.delete(acc, c)
        end
      )
    end
  end
end

{:ok, file} = File.read("inputs/day22.in")

instructions =
  file
  |> String.split("\n", trim: true)
  |> Enum.map(fn s ->
    numbers =
      s
      |> String.split(["x=", "..", ",y=", ",z="], trim: true)
      |> Enum.slice(1..-1)
      |> Enum.map(&String.to_integer/1)

    if String.at(s, 1) == "n" do
      ["on"] ++ numbers
    else
      ["off"] ++ numbers
    end
  end)

instructions
|> Enum.reduce(MapSet.new(), fn ins, acc ->
  Day22.process(ins, acc)
end)
|> Enum.count()
|> IO.inspect(label: "Part 1")

instructions
# |> Enum.reduce(MapSet.new(), fn ins, acc ->
#  IO.inspect(ins)
#  Day22.process(ins, acc, false)
# end)
# |> Enum.count()
|> IO.inspect(label: "Part 2")
