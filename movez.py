import keyboard

def draw(l):
    for r in range(50):
        print("\n")
    for i in range(3):
        for j in range(3):
            print(l[i][j], end=" ")
        print()
    print("\n")

end = [[1,2,3],[4,5,6],[7,8,0]]
nl = [[1,2,3],[4,6,8],[7,5,0]]
zp = [2,2]
draw(nl)

while True:
    if keyboard.is_pressed('w'):
        if zp[0] > 0:
            nl[zp[0]][zp[1]], nl[zp[0]-1][zp[1]] = nl[zp[0]-1][zp[1]], nl[zp[0]][zp[1]]
            zp[0] -= 1
            draw(nl)
            
    elif keyboard.is_pressed('a'):
        if zp[1] > 0:
            nl[zp[0]][zp[1]], nl[zp[0]][zp[1]-1] = nl[zp[0]][zp[1]-1], nl[zp[0]][zp[1]]
            zp[1] -= 1
            draw(nl)
            
    elif keyboard.is_pressed('s'):
        if zp[0] < 2:
            nl[zp[0]][zp[1]], nl[zp[0]+1][zp[1]] = nl[zp[0]+1][zp[1]], nl[zp[0]][zp[1]]
            zp[0] += 1
            draw(nl)
            
    elif keyboard.is_pressed('d'):
        if zp[1] < 2:
            nl[zp[0]][zp[1]], nl[zp[0]][zp[1]+1] = nl[zp[0]][zp[1]+1], nl[zp[0]][zp[1]]
            zp[1] += 1
            draw(nl)

    if end == nl:
        break
