def make_params(ll, mode, zoom, pt=False, pt_cords=None):
    params = {"ll": ",".join(ll), "z": zoom, "l": mode, "size": "450,450"}
    if pt:
        params["pt"] = {','.join(list(map(str, pt_cords)))}
    return params
