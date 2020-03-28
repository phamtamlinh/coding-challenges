def solution(S, P, Q):
  # remember last element array
  map_table = {
    "A": [0]*(len(S)+1),
    "C": [0]*(len(S)+1),
    "G": [0]*(len(S)+1),
    "T": [0]*(len(S)+1)
  }
  for i in range(1, len(S)+1):
    map_table["A"][i] = map_table["A"][i-1]
    map_table["C"][i] = map_table["C"][i-1]
    map_table["G"][i] = map_table["G"][i-1]
    map_table["T"][i] = map_table["T"][i-1]
    if S[i-1] == 'A':
      map_table["A"][i] += 1
    if S[i-1] == 'C':
      map_table["C"][i] += 1
    if S[i-1] == 'G':
      map_table["G"][i] += 1
    if S[i-1] == 'T':
      map_table["T"][i] += 1
  result = []
  for i in range(len(P)):
    if map_table["A"][Q[i]+1] - map_table["A"][P[i]] > 0:
      result.append(1)
      continue
    if map_table["C"][Q[i]+1] - map_table["C"][P[i]] > 0:
      result.append(2)
      continue
    if map_table["G"][Q[i]+1] - map_table["G"][P[i]] > 0:
      result.append(3)
      continue
    result.append(4)

  return result
