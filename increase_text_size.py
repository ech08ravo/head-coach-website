import json

def increase_text_size(filename, min_size=11):
    """Increase all text/typography to minimum size"""
    with open(filename, 'r') as f:
        data = json.load(f)

    changes = 0

    def process_element(elem):
        nonlocal changes
        settings = elem.get('settings', {})

        # Check typography font size
        if 'typography_font_size' in settings:
            font_size = settings['typography_font_size']
            if isinstance(font_size, dict) and 'size' in font_size:
                try:
                    current = int(font_size['size'])
                    if current < min_size:
                        font_size['size'] = min_size
                        changes += 1
                except:
                    pass

        # Check direct font_size
        if 'font_size' in settings:
            font_size = settings['font_size']
            if isinstance(font_size, dict) and 'size' in font_size:
                try:
                    current = int(font_size['size'])
                    if current < min_size:
                        font_size['size'] = min_size
                        changes += 1
                except:
                    pass

        # Process children
        for child in elem.get('elements', []):
            process_element(child)

    for elem in data['content']:
        process_element(elem)

    # Write back
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ {filename}: Updated {changes} text elements to minimum {min_size}px")

MIN_SIZE = 11

print("=" * 60)
print(f"INCREASING TEXT SIZE TO MINIMUM {MIN_SIZE}PX")
print("=" * 60)

increase_text_size('headcoach-home.json', MIN_SIZE)
increase_text_size('mental-skills-framework.json', MIN_SIZE)
increase_text_size('integral-plus-advantage.json', MIN_SIZE)

print("\n" + "=" * 60)
print("COMPLETE - Text sizes increased for readability")
print("=" * 60)
