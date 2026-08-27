import time
from src import ledger, cache

tray = cache.Cache()

def format_parcel(p):
    return (
        f"{p['tracking_code']} | {p['sender']} -> {p['receiver']}\n"
        f"{p['origin']} -> {p['destination']} | {p['status']} | {p['weight_kg']} kg | shipped {p['date_shipped']}"
    )

def get_parcel(code, parcels, by_code):
    start = time.perf_counter()
    cached = tray.get(f"parcel:{code}")
    if cached:
        return 200, f"{cached} (from the tray)\n(same answer, straight off the tray)"
    if code not in by_code:
        return 404, f"404 — There is no parcel {code}."
    parcel = by_code[code]
    elapsed = (time.perf_counter() - start) * 1000
    reply = f"200 — Found in {elapsed:.3f} ms\n{format_parcel(parcel)}"
    tray.put(f"parcel:{code}", reply)
    return 200, reply

def get_city(city, parcels, by_city):
    start = time.perf_counter()
    cached = tray.get(f"city:{city}")
    if cached:
        return 200, f"{cached} (from the tray)\n(same answer, straight off the tray)"
    if city not in by_city:
        return 404, f"404 — No parcels to {city}."
    found = by_city[city]
    elapsed = (time.perf_counter() - start) * 1000
    reply = f"200 — {len(found)} parcels found in {elapsed:.3f} ms\n"
    reply += "\n".join(format_parcel(p) for p in found[:2]) + f"\n... ({len(found)-2} more)"
    tray.put(f"city:{city}", reply)
    return 200, reply

def post_parcel(parcel, parcels):
    parcels.append(parcel)
    ledger.save_ledger(parcels)
    tray.invalidate("city:")
    return 201, "201 — Created — a new parcel now exists."

def put_parcel(code, update, parcels, by_code):
    if code not in by_code:
        return 404, f"404 — There is no parcel {code}."
    by_code[code].update(update)
    ledger.save_ledger(parcels)
    tray.invalidate(f"parcel:{code}")
    return 200, "200 — Done, here you are."

def delete_parcel(code, parcels, by_code, role):
    if role != "Station Master":
        return 403, "403 — Clerks may not delete parcels. Speak to the Station Master."
    if code not in by_code:
        return 404, f"404 — There is no parcel {code}."
    parcels.remove(by_code[code])
    ledger.save_ledger(parcels)
    tray.invalidate(f"parcel:{code}")
    return 200, "200 — Done, here you are."
