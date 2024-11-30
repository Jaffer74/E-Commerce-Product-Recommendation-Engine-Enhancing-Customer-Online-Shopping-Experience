#!/usr/bin/env python3
import sys

# Initialize variables to keep track of the current product and its stats
current_product = None
current_sum = 0
current_count = 0

# Process each line of input from stdin
for line in sys.stdin:
    line = line.strip()  # Remove extra spaces or newline characters
    try:
        product_id, rating = line.split("\t")
        rating = float(rating)  # Convert rating to float
    except ValueError:
        # Skip lines with invalid or malformed data
        continue

    if current_product == product_id:
        # Accumulate rating and count for the same product
        current_sum += rating
        current_count += 1
    else:
        if current_product:
            # Calculate and emit the average rating for the previous product
            average_rating = current_sum / current_count
            print(f"{current_product}\t{average_rating:.2f}")
        # Reset stats for the new product
        current_product = product_id
        current_sum = rating
        current_count = 1

# Emit the last product's average rating
if current_product:
    average_rating = current_sum / current_count
    print(f"{current_product}\t{average_rating:.2f}")
