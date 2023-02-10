defmodule Day24 do
  defp get_value(registers, arg) do
    case Integer.parse(arg) do
      :error ->
        Map.get(registers, arg)

      {val, _rem} ->
        val
    end
  end

  def process(instructions, input, registers \\ %{"w" => 0, "x" => 0, "y" => 0, "z" => 0}) do
    if Enum.count(instructions) == 0 do
      registers
    else
      [command, args] =
        instructions
        |> Enum.at(0)
        |> String.split(" ", parts: 2)

      new_instructions = Enum.slice(instructions, 1..-1)

      case command do
        "inp" ->
          val =
            input
            |> String.at(0)
            |> String.to_integer()

          new_registers = Map.merge(registers, %{args => val})
          process(new_instructions, String.slice(input, 1..-1), new_registers)

        "add" ->
          [a, b] = String.split(args, " ")
          b = get_value(registers, b)
          new_registers = Map.merge(registers, %{a => Map.get(registers, a) + b})
          process(new_instructions, input, new_registers)

        "mul" ->
          [a, b] = String.split(args, " ")
          b = get_value(registers, b)
          new_registers = Map.merge(registers, %{a => Map.get(registers, a) * b})
          process(new_instructions, input, new_registers)

        "div" ->
          [a, b] = String.split(args, " ")
          b = get_value(registers, b)
          new_registers = Map.merge(registers, %{a => div(Map.get(registers, a), b)})
          process(new_instructions, input, new_registers)

        "mod" ->
          [a, b] = String.split(args, " ")
          b = get_value(registers, b)
          new_registers = Map.merge(registers, %{a => rem(Map.get(registers, a), b)})
          process(new_instructions, input, new_registers)

        "eql" ->
          [a, b] = String.split(args, " ")
          b = get_value(registers, b)

          eq =
            if Map.get(registers, a) == b do
              1
            else
              0
            end

          new_registers = Map.merge(registers, %{a => eq})
          process(new_instructions, input, new_registers)
      end
    end
  end

  def is_bad(number) do
    number
    |> Integer.to_string()
    |> String.contains?("0")
  end

  def find_largest(instructions, n \\ 99_998_939_690_000) do
    if rem(n, 10000) == 0 do
      IO.inspect(n, label: :Current)
    end

    if is_bad(n) do
      find_largest(instructions, n - 1)
    else
      if instructions
         |> process(Integer.to_string(n))
         |> Map.get("z") == 0 do
        n
      else
        find_largest(instructions, n - 1)
      end
    end
  end
end

{:ok, file} = File.read("inputs/day24.in")

instructions =
  file
  |> String.split("\n", trim: true)

instructions
|> Day24.find_largest()
|> IO.inspect(label: "Part 1")
