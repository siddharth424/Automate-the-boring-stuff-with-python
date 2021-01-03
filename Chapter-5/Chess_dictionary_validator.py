def isValidChessBoard(chess_elements):
    black_piece=0
    white_piece=0
    b=0
    w=0
    if ('wking' and 'bking' ) not in chess_elements.values():
        return False
    
    for piece in chess_elements.values():
        if piece[0]=='b':
            black_piece += 1
        elif piece[0]== 'w':
            white_piece += 1
        else:
            return False
        if piece == 'wpawn': w+=1
        if piece == 'bpawn': b+=1
        
    if b>8 or w>8:
        return False
    
    for piece in chess_elements.keys():
        if piece[0] not in ['1','2','3','4','5','6','7','8']:
            return False
        if piece[1] not in ['a','b','c','d','e','f','g','h']:
            return False
        
    if black_piece>16 or white_piece>16:
        return False
    return True
chess_elements= {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess_elements))
