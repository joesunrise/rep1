def expanded_form(num):
    # Convert the number to a string
    num_str = str(num)

    # Initialize an empty list to store the expanded form
    expanded = []

    # Iterate through each digit in the number
    for i, digit in enumerate(num_str):
        # Check if the digit is not zero
        if digit != '0':
            # Calculate the place value
            place_value = int(digit) * 10 ** (len(num_str) - i - 1)
            # Add the place value to the expanded form list
            expanded.append(str(place_value))

    # Join the expanded form list with ' + ' separator
    return ' + '.join(expanded)
