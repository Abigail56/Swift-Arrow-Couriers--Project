from argon2 import PasswordHasher
import secrets, time

ph = PasswordHasher()

# Staff register with consistent keys
staff = {
    "oga_musty": {
        "password": "stationmaster1",
        "role": "Station Master"
    },
    "kemi_dispatch": {
        "password": "parcels4kemi",
        "role": "Clerk"
    },
    "ibrahim_k": {
        "password": "fastdelivery",
        "role": "Clerk"
    },
    "ngozi_front": {
        "password": "desk2026",
        "role": "Clerk"
    }
}

# Hash staff passwords immediately with Argon2
for user in staff:
    staff[user]["password"] = ph.hash(staff[user]["password"])

active_passes = {}

def sign_in(username, password):
    if username in staff:
        try:
            if ph.verify(staff[username]["password"], password):
                token = secrets.token_hex(16)
                active_passes[token] = {
                    "user": username,
                    "role": staff[username]["role"],
                    "time": time.time()
                }
                return 200, f"Welcome, {username} ({staff[username]['role']}). Your day pass: {token}"
        except Exception:
            return 401, "Who are you? Sign in first."
    return 401, "Who are you? Sign in first."

def validate_pass(token):
    if token not in active_passes:
        return None, 401
    info = active_passes[token]
    if time.time() - info["time"] > 300:  # 5 minutes expiry
        del active_passes[token]
        return None, 401
    return info, 200

def sign_out(token):
    if token in active_passes:
        del active_passes[token]
        return 200, "Signed out. Pass destroyed."
    return 401, "No valid pass found."
