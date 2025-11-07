

# Define a reusable function to update the file
def update_file(import_file, remove_list):
    """
    Reads an allow list file, removes specified IPs,
    and rewrites the cleaned list back to the file.
    """

    # --- Step 1: Read the file ---
    try:
        with open(import_file, "r") as file:
            ip_addresses = file.read().split()
        print(f"✅ Successfully read {len(ip_addresses)} IP addresses from {import_file}")
    except FileNotFoundError:
        print(f"❌ Error: The file '{import_file}' was not found.")
        return
    except Exception as e:
        print(f"⚠️ Unexpected error reading file: {e}")
        return

    # --- Step 2: Remove the unwanted IPs ---
    initial_count = len(ip_addresses)
    for ip in remove_list:
        if ip in ip_addresses:
            ip_addresses.remove(ip)
            print(f"🚫 Removed {ip} from allow list.")
        else:
            print(f"ℹ️ IP {ip} not found in the file.")

    final_count = len(ip_addresses)

    # --- Step 3: Rewrite the updated list back to the file ---
    try:
        with open(import_file, "w") as file:
            file.write("\n".join(ip_addresses))
        print(f"✅ Updated file saved successfully ({final_count}/{initial_count} IPs remain).")
    except Exception as e:
        print(f"⚠️ Error writing to file: {e}")
        return

    # --- Step 4: Display the updated contents ---
    print("\n📄 Updated Allow List:")
    print("-" * 30)
    for ip in ip_addresses:
        print(ip)
    print("-" * 30)


# --- Main program execution ---
if __name__ == "__main__":
    # Example allow list file (must exist in same directory)
    import_file = "allow_list.txt"

    # Example IPs to remove (these would be flagged or expired)
    remove_list = [
        "192.168.25.60",
        "192.168.140.81",
        "192.168.203.198"
    ]

    # Call the function
    update_file(import_file, remove_list)
