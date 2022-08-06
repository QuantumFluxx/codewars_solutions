def descending_order(n)
  return n.to_s.split("").sort_by {|x| x}.join("").reverse.to_i
end