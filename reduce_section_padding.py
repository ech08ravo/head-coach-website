import json

def reduce_padding(filename, target_padding=50):
    """Reduce section padding to specified value"""
    with open(filename, 'r') as f:
        data = json.load(f)

    changes = 0

    # Process top-level containers only (sections)
    for elem in data['content']:
        if elem.get('elType') == 'container' and not elem.get('isInner'):
            settings = elem.get('settings', {})

            if 'padding' in settings:
                pad = settings['padding']
                if isinstance(pad, dict):
                    # Reduce top/bottom padding
                    for key in ['top', 'bottom']:
                        if key in pad:
                            try:
                                current = int(pad[key])
                                if current > target_padding:
                                    pad[key] = str(target_padding)
                                    changes += 1
                            except:
                                pass

    # Write back
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ {filename}: Reduced {changes} section paddings to {target_padding}px")

# Set your desired padding (default 50px, adjust as needed)
TARGET = 50

print("=" * 60)
print(f"REDUCING SECTION PADDING TO {TARGET}PX")
print("=" * 60)

reduce_padding('headcoach-home.json', TARGET)
reduce_padding('mental-skills-framework.json', TARGET)
reduce_padding('integral-plus-advantage.json', TARGET)

print("\n" + "=" * 60)
print("COMPLETE - Section spacing tightened")
print("=" * 60)
