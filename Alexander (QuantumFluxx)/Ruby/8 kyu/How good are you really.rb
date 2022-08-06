def better_than_average(arr, points)
  if arr.sum/arr.length < points
    return true
  else
    return false
  end
end
