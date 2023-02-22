defmodule Day17 do
  def move_x(x, dx) do
    n = x + dx

    if dx > 0 do
      [n, dx - 1]
    else
      if n < 0 do
        [n, dx + 1]
      else
        [n, dx]
      end
    end
  end

  def move_x_n_steps(x, dx, n) do
    if n == 0 or dx == 0 do
      x
    else
      new_dx =
        if dx > 0 do
          dx - 1
        else
          dx + 1
        end

      move_x_n_steps(x + dx, new_dx, n - 1)
    end
  end

  def move_y(y, dy) do
    [y + dy, dy - 1]
  end

  def move_all_y(y, dy, min_y..max_y) do
    [y, dy] = Day17.move_y(y, dy)

    if min_y <= y and y <= max_y do
      true
    else
      if min_y > y do
        false
      else
        Day17.move_all_y(y, dy, min_y..max_y)
      end
    end
  end

  def find_n_steps(y, dy, min_y..max_y, steps \\ 0) do
    [y, dy] = Day17.move_y(y, dy)

    if min_y <= y and y <= max_y do
      steps
    else
      Day17.find_n_steps(y, dy, min_y..max_y, steps + 1)
    end
  end

  def find_max_y(dy, y \\ 0) do
    [ny, ndy] = move_y(y, dy)

    if ny > y do
      find_max_y(ndy, ny)
    else
      y
    end
  end

  def find_all_dx(steps) do
    0..94
    |> Enum.map(fn dx ->
      [dx, Day17.move_x_n_steps(0, dx, steps)]
    end)
    |> Enum.filter(fn [_dx, final_x] -> 60 <= final_x and final_x <= 94 end)
    |> Enum.count()
  end
end

# target area: x=60..94, y=-171..-136

Day17.find_max_y(170)
|> IO.inspect(label: "Part 1")

-170..170
|> Enum.map(fn dy ->
  [dy, Day17.move_all_y(0, dy, -171..-136)]
end)
|> Enum.filter(fn [_dy, valid] -> valid end)
|> Enum.map(fn [dy, _valid] ->
  [dy, Day17.find_n_steps(0, dy, -171..-136)]
end)
|> Enum.map(fn [_dy, steps] ->
  Day17.find_all_dx(steps)
end)
|> Enum.sum()
|> IO.inspect(label: "Part 2")
