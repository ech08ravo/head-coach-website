import json
import sys
import os
import shutil

PLACEHOLDER = {"unit": "%", "size": "", "sizes": []}
MOBILE_100_PCT = {"unit": "%", "size": 100, "sizes": []}
BOXED_80_PCT = {"unit": "%", "size": 80, "sizes": []}


def apply_mobile_formatting(filename, dry_run=False):
    """Apply homepage mobile formatting pattern to an Elementor JSON template."""
    with open(filename, 'r') as f:
        data = json.load(f)

    changes = 0

    def process_element(elem):
        nonlocal changes

        # Guard: settings can be [] instead of {} in some Elementor exports
        if isinstance(elem.get('settings'), list):
            elem['settings'] = {}

        settings = elem.get('settings', {})

        # --- Transformation 1: Convert boxed_width from 1200px to 80% ---
        bw = settings.get('boxed_width')
        if isinstance(bw, dict) and bw.get('unit') == 'px' and bw.get('size') == 1200:
            if dry_run:
                print(f"  [DRY] Convert boxed_width 1200px -> 80%")
            settings['boxed_width'] = dict(BOXED_80_PCT)
            changes += 1

        # --- Transformation 2: Add tablet/mobile placeholders ---
        bw = settings.get('boxed_width')
        if isinstance(bw, dict) and bw.get('unit') == '%':
            if 'boxed_width_tablet' not in settings:
                if dry_run:
                    print(f"  [DRY] Add boxed_width_tablet placeholder")
                settings['boxed_width_tablet'] = dict(PLACEHOLDER)
                changes += 1
            if 'boxed_width_mobile' not in settings:
                if dry_run:
                    print(f"  [DRY] Add boxed_width_mobile placeholder")
                settings['boxed_width_mobile'] = dict(PLACEHOLDER)
                changes += 1

        # --- Transformation 3: Mobile override for large inner containers ---
        cw = settings.get('_element_custom_width')
        if isinstance(cw, dict) and cw.get('unit') == 'px':
            try:
                size = int(cw.get('size', 0))
            except (ValueError, TypeError):
                size = 0
            if size >= 500:
                if '_element_custom_width_mobile' not in settings:
                    if dry_run:
                        print(f"  [DRY] Add _element_custom_width_mobile: 100% (was {size}px)")
                    settings['_element_custom_width_mobile'] = dict(MOBILE_100_PCT)
                    changes += 1
                if '_element_custom_width_tablet' not in settings:
                    if dry_run:
                        print(f"  [DRY] Add _element_custom_width_tablet placeholder")
                    settings['_element_custom_width_tablet'] = dict(PLACEHOLDER)
                    changes += 1

        # Recurse into children
        for child in elem.get('elements', []):
            process_element(child)

    for elem in data['content']:
        process_element(elem)

    if not dry_run:
        # Backup
        backup = filename + '.backup'
        if not os.path.exists(backup):
            shutil.copy2(filename, backup)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    print(f"{'[DRY RUN] ' if dry_run else ''}{filename}: {changes} changes")


dry_run = '--dry-run' in sys.argv

print("=" * 60)
print("APPLYING MOBILE FORMATTING (homepage pattern)")
if dry_run:
    print("  ** DRY RUN - no files will be modified **")
print("=" * 60)

apply_mobile_formatting('integral-plus-advantage.json', dry_run)
print()
apply_mobile_formatting('mental-skills-framework.json', dry_run)

print("\n" + "=" * 60)
print("COMPLETE" + (" (dry run)" if dry_run else ""))
print("=" * 60)
