# ============ Function OR Machine ==============

def calculate_total_amount(input, age):
    items = {
        "pencil" : 10,
        "notebook" : 40,
        "eraser" : 20,
        "bag" : 100,
    }

    output = 0

    for item_name in input:
        output = output + items[item_name]

    if age < 18:
        output = 0.5 * output
    else:
        output = 0.75 * output

    return output

# ==========================


input = ["pencil", "notebook"]

output  = calculate_total_amount(input, 14)

print("Alex's bill amount:", output)
