def rotate_array(A, K):
  
  tempArray = A
  for i in range(K):
    rotated_array = tempArray[-1:] + tempArray[:-1]
    tempArray = rotated_array

  return tempArray