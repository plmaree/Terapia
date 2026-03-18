import os
import re

def update_emojis():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the script section with arrays
    script_pattern = r'<script>(.*?)</script>'
    script_match = re.search(script_pattern, content, re.DOTALL)
    if not script_match:
        print("Script section not found")
        return

    script_content = script_match.group(1)

    # Function to update a single array
    def update_array(array_name, array_content):
        # Parse products
        products = []
        product_pattern = r'\{[^}]*\}'
        for match in re.finditer(product_pattern, array_content):
            product_str = match.group(0)
            products.append(product_str)

        updated_products = []
        for product in products:
            # Check if emoji is already an img
            if '"emoji": "<img' in product:
                updated_products.append(product)
                continue

            # Extract name
            name_match = re.search(r'"name": "([^"]*)"', product)
            if not name_match:
                updated_products.append(product)
                continue

            name = name_match.group(1)

            # Check for image file
            extensions = ['.jpg', '.png', '.webp', '.jpeg']
            image_path = None
            for ext in extensions:
                candidate = f'img/gor/{name}{ext}'
                if os.path.exists(candidate):
                    image_path = candidate
                    break

            if image_path:
                # Replace emoji
                emoji_pattern = r'"emoji": "[^"]*"'
                new_emoji = f'"emoji": "<img src=\\"{image_path}\\" alt=\\"{name}\\" class=\\"product-actual-img\\">"'
                updated_product = re.sub(emoji_pattern, new_emoji, product)
                updated_products.append(updated_product)
                print(f"Updated: {name}")
            else:
                updated_products.append(product)

        # Reconstruct array
        updated_array = f'const {array_name} = [\n {",\n ".join(updated_products)},\n];'
        return updated_array

    # Update each array
    arrays = ['bestProducts', 'panicleVarieties', 'macrophyllaVarieties']
    for array_name in arrays:
        array_pattern = rf'const {array_name} = \[(.*?)\];'
        array_match = re.search(array_pattern, script_content, re.DOTALL)
        if array_match:
            updated_array = update_array(array_name, array_match.group(1))
            script_content = script_content.replace(array_match.group(0), updated_array)

    # Update the content
    updated_content = content.replace(script_match.group(1), script_content)

    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("Update complete")

if __name__ == "__main__":
    update_emojis()