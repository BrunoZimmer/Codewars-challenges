def sqInRect(lng, width):
    resp = []
    if lng != width:
        while lng != width:
            if lng > width: 
                lng -=width
                resp.append(width)
            else: 
                width -=lng
                resp.append(lng)
        resp.append(lng)
        return resp

def sqInRect_Recurs(lng, width):
    if lng == width: return [lng]
    elif lng > width: return [width] + sqInRect_Recurs(lng-width, width) 
    elif lng < width: return [lng] + sqInRect_Recurs(lng, width-lng) 


l = 5
w = 3
resp = sqInRect_Recurs(l, w)
print(resp)