local t = {}
function t.twoOldestAges(ages)
     table.sort(ages, function (a,b)
      return (a > b)
    end)
    return {ages[2],ages[1]}
end
return t