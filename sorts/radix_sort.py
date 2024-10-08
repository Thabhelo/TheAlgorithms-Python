def radixsort(lst):
    RADIX = 10
    placement = 1

    # get the maximum number
    max_digit = max(lst)

    while placement < max_digit:
      # declare and initialize buckets
      buckets = [[] for _ in range( RADIX )]

      # split lst between lists
      for i in lst:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)

      # empty lists into lst array
      a = 0
      for b in range( RADIX ):
        for i in buckets[b]:
          lst[a] = i
          a += 1

      # move to next
      placement *= RADIX
