import itertools

def tile (top, bottom) :
    return [top, bottom]

def isAMatch (seqTiles) :
    join = lambda l, i : "".join ([e [i] for e in l])
    totalTop = join (seqTiles, 0)
    totalBottom = join (seqTiles, 1)
    return totalTop == totalBottom

def repeated_tiles (tiles, occ):
    l = []
    for i in range (len (tiles)) :
        l = l + ([tiles [i]] * occ [i])
    return l

def verify_PCP_aux (tiles) :
    combs = list (itertools.permutations (tiles))
    r = False
    for c in combs :
        if isAMatch (c) :
            r = True
    return r

def verify_PCP (tiles, MAX) :
    aux = verify_PCP_aux (tiles)
    if (aux) :
        return aux
    else :
        for r in range (MAX) :
            for i in range (len (tiles)) :
                t = tiles + [tiles [i]] * r
                if (verify_PCP_aux (t)) :
                    return True
    return None

t = tile
tiles = [t ("abc", "c"), t ("b", "ca"), t ("a", "ab"), t ("ca", "a")]
#tiles = [t ("0", "0"), t ("1", "1")]

print (verify_PCP (tiles, 5))
