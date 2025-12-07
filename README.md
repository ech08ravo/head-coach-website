# Head-Coach Mental Skills Website

A complete website for Head-Coach Mental Skills, built with clean HTML/CSS for easy WordPress integration.

## Folder Structure

```
head-coach-website/
├── css/
│   └── style.css          # Main stylesheet with all design tokens
├── pages/
│   ├── home.html          # Homepage
│   ├── services.html      # Services overview
│   ├── athlete-coaching.html    # 1-on-1 Athlete Coaching
│   ├── team-coaching.html       # Team Mental Skills Coaching
│   ├── staff-coaching.html      # Staff Mental Skills Coaching
│   ├── head-coach-development.html  # Head Coach Development
│   ├── our-approach.html        # The Integral+ Model
│   ├── results.html             # Results & Case Studies
│   ├── about.html               # About Jay Hedley
│   ├── testimonials.html        # Client Testimonials
│   ├── contact.html             # Contact & Booking Form
│   └── faq.html                 # Frequently Asked Questions
└── README.md
```

## WordPress Integration Guide

### Option 1: Copy Content to Gutenberg

1. Open each HTML file
2. Copy the content between `<section>` tags
3. In WordPress, create a new page
4. Use the "Custom HTML" block to paste sections
5. Style with the CSS below

### Option 2: Add CSS to Theme

Add the contents of `css/style.css` to your theme:

**Method A: Theme Customizer**
1. Go to Appearance → Customize → Additional CSS
2. Paste the CSS (note: there may be character limits)

**Method B: Child Theme**
1. Create a child theme if you haven't
2. Add to your child theme's `style.css`

**Method C: Plugin**
1. Use a plugin like "Simple Custom CSS and JS"
2. Add the CSS there

### Option 3: Full HTML Pages

If you want to use these as standalone HTML pages:
1. Upload the entire folder to your web server
2. Rename `home.html` to `index.html`
3. Update all navigation links if needed

## Images Required

The templates reference the following images. You'll need to add these:

```
images/
├── logo.png                 # Main logo (dark version)
├── logo-white.png           # Logo for dark backgrounds
├── jay-hedley.jpg           # Jay's photo for About page
├── testimonial-alana.jpg    # Alana Thomas testimonial photo
├── athlete-coaching.jpg     # Hero image for athlete page
├── team-coaching.jpg        # Hero image for team page
├── staff-coaching.jpg       # Hero image for staff page
├── head-coach-dev.jpg       # Hero image for head coach page
├── fiji-rugby.jpg           # Fiji Rugby case study
├── f1-racing.jpg            # F1 case study
├── boxing.jpg               # Boxing case study
└── nswis.jpg                # NSWIS case study
```

## Design System

### Colors
- **Navy**: #1a3a5c (primary brand color)
- **Teal**: #2a7d7d (accent, links, highlights)
- **Gold**: #d4a84b (headings, emphasis)
- **Coral**: #f4845f (secondary accent)
- **Green**: #28a078 (stats, success indicators)

### Typography
- **Headings**: Cormorant Garamond (Google Fonts)
- **Body**: Source Sans Pro (Google Fonts)

### Font Loading
Add this to your `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Source+Sans+Pro:wght@300;400;600;700&display=swap" rel="stylesheet">
```

## Page-by-Page Notes

### Homepage (home.html)
- Hero with main value proposition
- Service cards with links to detail pages
- Testimonial feature
- Stats section
- Champions/clients section
- CTA to contact

### Service Pages
Each service page includes:
- Hero with service-specific messaging
- Overview section
- "Who it's for" section
- "What we work on" features
- Process/delivery section
- CTA to contact

### Our Approach (our-approach.html)
- Detailed explanation of Integral+ model
- Five mental dimensions with parallels
- Methodology foundations
- Application process

### Results (results.html)
- Stats section
- Case studies for major clients
- Testimonial preview

### About (about.html)
- Jay's bio and credentials
- Journey/timeline
- Philosophy quotes

### Contact (contact.html)
- Contact form
- Process expectations
- Direct contact info

### FAQ (faq.html)
- Organized by category
- Common questions answered

## Customization

### Changing Colors
Update CSS variables at the top of `style.css`:
```css
:root {
    --navy: #1a3a5c;
    --teal: #2a7d7d;
    /* etc */
}
```

### Changing Fonts
Update the Google Fonts link and CSS variables:
```css
:root {
    --font-heading: 'Your Font', serif;
    --font-body: 'Your Font', sans-serif;
}
```

## Form Integration

The contact form needs a backend. Options:
1. **WordPress**: Use Contact Form 7 or WPForms
2. **Formspree**: Add `action="https://formspree.io/f/YOUR_ID"`
3. **Netlify**: Add `data-netlify="true"` attribute

## Questions?

This website was created by Claude for Head-Coach Mental Skills. Adjust paths, images, and content as needed for your specific setup.
