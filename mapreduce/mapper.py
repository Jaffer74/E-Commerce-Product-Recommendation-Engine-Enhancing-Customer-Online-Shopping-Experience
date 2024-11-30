#!/usr/bin/env python3
import sys

# Process each line of input from stdin
for line in sys.stdin:
    line = line.strip()  # Remove extra spaces or newline characters
    fields = line.split(",")  # Split line by comma delimiter

    # Ensure the line has at least 3 fields: UserID, ProductID, Rating
    if len(fields) >= 3:
        product_id = fields[1].strip()  # Extract and clean ProductID
        rating = fields[2].strip()  # Extract and clean Rating
        try:
            # Emit ProductID and Rating
            print(f"{product_id}\t{rating}")
        except ValueError:
            # Skip invalid entries
            continue
