# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a static cybersecurity portfolio website for Zayets, a cybersecurity consultant and penetration tester. The site showcases professional experience, projects, and cybersecurity expertise through a clean, professional web presence.

**Repository**: 7a6179657473.github.io
**Domain**: Hosted on GitHub Pages at https://7a6179657473.github.io/

## Architecture & Structure

### File Organization
- **`index.html`** - Main landing page with professional summary, experience, education, and contact information
- **`about_me.html`** - Detailed personal and professional background
- **`phishthefish.html`** - Educational resource on phishing attacks and prevention
- **`wpa.html`** - Project showcase for WPA security auditing
- **`Sec-audits.html`** - Security audit methodologies and case studies
- **`DRP-planning.html`** - Disaster recovery planning documentation
- **`desktop-laptop.html`** - Hardware installation and maintenance guides
- **`contact-me.html`** - Contact form and information
- **`testskill2.html`** - Skills assessment or testing page
- **`under-construction.html`** - Placeholder for pages in development
- **`styles.css`** - Main stylesheet with responsive design and consistent theming

### Visual Assets
- **`zayets.jpg`** - Primary profile photo
- **`zayets_circular.png`** - Circular profile image for various layouts
- **`github-logo.png`** - GitHub social link icon
- **`twitter-logo.png`** - Twitter social link icon

### Design System

The site uses a consistent design language with:
- **Color Scheme**: Brown/rust theme (`#694d48` primary, `#a27d76` accents)
- **Layout**: Centered container design (800px max-width) with consistent navbar
- **Typography**: Arial sans-serif with clear hierarchy
- **Components**: 
  - Responsive navbar with dropdown navigation
  - Skills section with interactive dropdown boxes
  - Experience cards with structured information
  - Contact section with social media integration

### Navigation Structure
```
Home (index.html)
├── About (about_me.html)
├── Projects
│   ├── WPA audit (wpa.html)
│   └── Phish the Fish (phishthefish.html)
└── Skills (dropdown sections)
    ├── Desktop & Laptop (desktop-laptop.html)
    ├── Auditing (Sec-audits.html, DRP-planning.html)
    └── Administration (under development)
```

## Development Commands

This is a static HTML/CSS website with no build process. Development workflow:

### Local Development
```powershell
# Serve locally using Python (if available)
python -m http.server 8000

# Or using PHP (if available)  
php -S localhost:8000

# Or use any local web server to serve static files
```

### File Operations
```powershell
# View all HTML files
Get-ChildItem *.html

# Check for broken links (manual process - no automated tooling)
# Verify all href attributes point to existing files or valid URLs

# Validate HTML (requires external tool)
# No built-in validation - use online validators or browser dev tools
```

### Content Updates
- **Profile Updates**: Modify experience sections in `index.html` and `about_me.html`
- **New Projects**: Create new HTML files and add navigation links to navbar across all pages
- **Styling Changes**: Update `styles.css` - changes affect all pages globally

## Key Patterns & Conventions

### HTML Structure
- All pages follow consistent structure: navbar → container → sections → footer
- External links use full GitHub Pages URLs (`https://7a6179657473.github.io/`)
- Internal navigation uses relative paths (`index.html`, `about_me.html`)
- Each page includes consistent navbar with same structure

### CSS Architecture
- **Global styles**: Typography, colors, and base layout in main stylesheet
- **Component-specific styles**: Navbar, dropdowns, contact forms, skills sections
- **Responsive design**: Flexible layouts that work on desktop and mobile
- **Consistent spacing**: 20px margins for sections, 10px for components

### Content Management
- **Version control**: Document Control Version footer on each page
- **Professional tone**: Formal, security-focused language throughout
- **Educational content**: Technical explanations balanced with accessibility

### Social Links & External References
- GitHub: https://github.com/7a6179657473
- Twitter: https://twitter.com/zayets8
- All external links open in new tabs (`target="_blank"`)

## Cybersecurity Focus Areas

The site emphasizes expertise in:
- **Penetration Testing**: Network security assessments and vulnerability analysis
- **Security Auditing**: Comprehensive security control evaluations
- **Disaster Recovery Planning**: Business continuity and recovery strategies
- **NIST Standards Compliance**: Framework implementation and assessment
- **Bug Bounty Programs**: Vulnerability research and responsible disclosure
- **Hardware Security**: Desktop/laptop security and maintenance

## Content Guidelines

When updating content:
- Maintain professional, consultant-level expertise tone
- Include specific, measurable achievements (e.g., "$9 million in transactions", "300+ personnel")
- Balance technical depth with accessibility for non-technical audiences
- Ensure all security advice follows current best practices
- Update Document Control Version numbers when making changes

## Dependencies

**Runtime Dependencies**: None - pure HTML/CSS/JavaScript
**Development Dependencies**: 
- `requirements.txt` contains `beautifulsoup4` (likely for web scraping/content parsing)
- No package.json, build tools, or frameworks

**Browser Compatibility**: Designed for modern browsers with CSS3 and HTML5 support
