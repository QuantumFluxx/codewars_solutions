def is_palindrome str
  if str.downcase == str.downcase.reverse
    return true
  else
    return false
  end
end