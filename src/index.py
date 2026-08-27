def build_indexes(parcels):
    by_code = {p["code"]: p for p in parcels}
    by_city = {}
    for p in parcels:
        city = p["to"]
        by_city.setdefault(city, []).append(p)
    return by_code, by_city