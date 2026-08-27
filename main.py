from src import auth, parcels, ledger, index

def main():
    parcels_data = ledger.load_ledger()
    by_code, by_city = index.build_indexes(parcels_data)

    print("=" * 50)
    print("SWIFT ARROW COURIERS - TRACKING WINDOW".center(50))
    print("=" * 50 + "\n")
    print("--- THE GRILLE (sign in first) ---\n")

    username = input("Username: ")
    password = input("Password: ")
    code, reply = auth.sign_in(username, password)
    print(code, reply)
    if code != 200:
        return
    token = reply.split(":")[-1].strip()

    while True:
        print("\n--------- WINDOW MENU ---------")
        print("1. GET parcel <code>")
        print("2. GET parcels to <city>")
        print("3. POST parcel")
        print("4. PUT parcel <code>")
        print("5. DELETE parcel <code>")
        print("6. Sign out")
        print("7. Close window")
        print("--------------------------------")

        choice = input("Choose an option (1-7): ")

        # Shortcuts: build the full slip automatically
        if choice == "1":
            code = input("Enter tracking code: ")
            choice = f"GET parcel {code}"
        elif choice == "2":
            city = input("Enter destination city: ")
            choice = f"GET parcels to {city}"
        elif choice == "3":
            choice = "POST parcel"
        elif choice == "4":
            code = input("Enter tracking code: ")
            choice = f"PUT parcel {code}"
        elif choice == "5":
            code = input("Enter tracking code: ")
            choice = f"DELETE parcel {code}"
        elif choice == "6":
            choice = "sign_out"
        elif choice == "7":
            choice = "close"

        info, status = auth.validate_pass(token)
        if status != 200:
            print("401 — Your day pass has expired. Please sign in again at the grille.")
            break

        if choice.startswith("GET parcel"):
            code = choice.split()[-1]
            _, r = parcels.get_parcel(code, parcels_data, by_code)
            print(r)

        elif choice.startswith("GET parcels to"):
            city = choice[len("GET parcels to"):].strip()
            _, r = parcels.get_city(city, parcels_data, by_city)
            print(r)

        elif choice.startswith("POST parcel"):
            new = {
                "tracking_code": input("Tracking code: "),
                "sender": input("Sender: "),
                "receiver": input("Receiver: "),
                "origin": input("Origin city: "),
                "destination": input("Destination city: "),
                "status": "registered",
                "weight_kg": float(input("Weight (kg): ")),
                "date_shipped": input("Date shipped (YYYY-MM-DD): ")
            }
            _, r = parcels.post_parcel(new, parcels_data)
            by_code[new["tracking_code"]] = new
            by_city.setdefault(new["destination"], []).append(new)
            print(r)

        elif choice.startswith("PUT parcel"):
            code = choice.split()[-1]
            update = {"status": input("New status: ")}
            _, r = parcels.put_parcel(code, update, parcels_data, by_code)
            print(r)

        elif choice.startswith("DELETE parcel"):
            code = choice.split()[-1]
            _, r = parcels.delete_parcel(code, parcels_data, by_code, info["role"])
            print(r)

        elif choice == "sign_out":
            c, r = auth.sign_out(token)
            print(r)
            break

        elif choice == "close":
            print("Window closed.")
            break

        else:
            print("400 — I cannot read this slip. The verbs are GET, POST, PUT, DELETE.")

if __name__ == "__main__":
    main()
