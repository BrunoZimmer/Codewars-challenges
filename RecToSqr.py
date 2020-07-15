def sqInRect(lng, wdth):
    resp = []
    if lng != wdth:
        while lng != wdth:
            if lng > wdth: 
                lng -=wdth
                resp.append(wdth)
            else: 
                wdth -=lng
                resp.append(lng)
        resp.append(lng)
        return resp

def sqInRect_Recurs(lng, wdth):
    if lng == wdth: return [lng]
    elif lng > wdth: return [wdth] + sqInRect_Recurs(lng-wdth, wdth) 
    elif lng < wdth: return [lng] + sqInRect_Recurs(lng, wdth-lng) 


l = 5
w = 3
resp = sqInRect_Recurs(l, w)
print(resp)