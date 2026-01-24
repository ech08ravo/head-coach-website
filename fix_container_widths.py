import json

def fix_container_widths(filename):
    """Set all containers to consistent boxed width"""
    with open(filename, 'r') as f:
        data = json.load(f)

    changes = 0

    for elem in data['content']:
        if elem.get('elType') == 'container' and not elem.get('isInner'):
            # Fix settings if it's a list
            if isinstance(elem.get('settings'), list):
                elem['settings'] = {}

            settings = elem.get('settings', {})

            # Set boxed width to 1200px
            if 'boxed_width' not in settings or settings.get('boxed_width') == 'none':
                settings['boxed_width'] = {
                    "unit": "px",
                    "size": 1200,
                    "sizes": []
                }
                changes += 1

            # Make sure content_width is set properly
            if settings.get('content_width') == 'full':
                settings['content_width'] = 'boxed'
                changes += 1

    # Write back
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ {filename}: Fixed {changes} container widths to 1200px boxed")

print("=" * 60)
print("FIXING CONTAINER WIDTHS TO CONSISTENT 1200PX")
print("=" * 60)

fix_container_widths('headcoach-home.json')
fix_container_widths('mental-skills-framework.json')
fix_container_widths('integral-plus-advantage.json')

print("\n" + "=" * 60)
print("COMPLETE - All containers set to 1200px boxed width")
print("=" * 60)
