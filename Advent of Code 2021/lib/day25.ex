defmodule Day25 do
  def move_east(cucumbers) do
    0..(Enum.count(cucumbers) - 1)
    |> Enum.map(fn i ->
      0..(Enum.count(Enum.at(cucumbers, i)) - 1)
      |> Enum.map(fn j ->
        {direction, has_moved} =
          cucumbers
          |> Enum.at(i)
          |> Enum.at(j)

        if direction == ">" do
          {next_direction, _next_has_moved} =
            cucumbers
            |> Enum.at(i)
            |> Enum.at(rem(j + 1, Enum.count(Enum.at(cucumbers, i))))

          if next_direction == "." do
            {".", true}
          else
            {direction, has_moved}
          end
        else
          if direction == "." do
            {prev_direction, prev_has_moved} =
              cucumbers
              |> Enum.at(i)
              |> Enum.at(j - 1)

            if prev_direction == ">" or (prev_direction == "." and prev_has_moved) do
              {">", true}
            else
              {direction, has_moved}
            end
          else
            {direction, has_moved}
          end
        end
      end)
    end)
  end

  def move_south(cucumbers) do
    0..(Enum.count(cucumbers) - 1)
    |> Enum.map(fn i ->
      0..(Enum.count(Enum.at(cucumbers, i)) - 1)
      |> Enum.map(fn j ->
        {direction, has_moved} =
          cucumbers
          |> Enum.at(i)
          |> Enum.at(j)

        if direction == "v" do
          {next_direction, _next_has_moved} =
            cucumbers
            |> Enum.at(rem(i + 1, Enum.count(cucumbers)))
            |> Enum.at(j)

          if next_direction == "." do
            {".", true}
          else
            {direction, has_moved}
          end
        else
          if direction == "." do
            {prev_direction, prev_has_moved} =
              cucumbers
              |> Enum.at(i - 1)
              |> Enum.at(j)

            if prev_direction == "v" or (prev_direction == "." and prev_has_moved) do
              {"v", true}
            else
              {direction, has_moved}
            end
          else
            {direction, has_moved}
          end
        end
      end)
    end)
  end

  def has_anyone_moved(cucumbers) do
    cucumbers
    |> Enum.flat_map(& &1)
    |> Enum.any?(fn {_direction, has_moved} ->
      has_moved
    end)
  end

  def reset_movements(cucumbers) do
    0..(Enum.count(cucumbers) - 1)
    |> Enum.map(fn i ->
      0..(Enum.count(Enum.at(cucumbers, i)) - 1)
      |> Enum.map(fn j ->
        {direction, _has_moved} =
          cucumbers
          |> Enum.at(i)
          |> Enum.at(j)

        {direction, false}
      end)
    end)
  end

  def step(cucumbers) do
    after_east =
      cucumbers
      |> move_east()

    after_south =
      after_east
      |> reset_movements()
      |> move_south()

    final =
      after_south
      |> reset_movements()

    {final, after_east |> has_anyone_moved() or after_south |> has_anyone_moved}
  end

  def find_final_step(cucumbers, steps \\ 0) do
    {next_cucumbers, any_moved} =
      cucumbers
      |> step()

    if any_moved do
      find_final_step(next_cucumbers, steps + 1)
    else
      steps + 1
    end
  end

  def print(cucumbers) do
    0..(Enum.count(cucumbers) - 1)
    |> Enum.map(fn i ->
      0..(Enum.count(Enum.at(cucumbers, i)) - 1)
      |> Enum.map(fn j ->
        {direction, _has_moved} =
          cucumbers
          |> Enum.at(i)
          |> Enum.at(j)

        direction
      end)
      |> Enum.join()
      |> IO.inspect()
    end)
  end
end

{:ok, file} = File.read("inputs/day25.in")

cucumbers =
  file
  |> String.split("\n", trim: true)
  |> Enum.map(fn s ->
    s
    |> String.split("", trim: true)
    |> Enum.map(fn x ->
      # direction, has_moved
      {x, false}
    end)
  end)

cucumbers
|> Day25.find_final_step()
|> IO.inspect(label: "Part 1")
