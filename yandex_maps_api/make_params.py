def make_params(ll, mode, zoom, pt=False):
    params = {"ll": ll, "spn": f'{zoom},{zoom}', "l": mode}
    if pt:
        params["pt"] = pt  # доработать