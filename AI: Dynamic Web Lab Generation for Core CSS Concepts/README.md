# AI: Dynamic Web Lab Generation for Core CSS Concepts

## Overview
This task demonstrates sequential and contextual AI prompting to generate
interactive, single-file HTML/CSS/JS tools for visualizing core CSS
concepts: the Box Model and modern layout systems (Flexbox/Grid).

## AI tool used
Gemini (with Canvas)

## Files in this folder

### `1-box-model-lab.html`
The initial Box Model & Display lab. Shows two boxes ("Box 1" and "Box 2"),
with Box 1 using `background-clip: content-box` to visually separate the
content area from the padding area, plus a solid border. A control panel
with sliders (padding, margin, border-width, width) and a dropdown (display:
block / inline-block / inline) updates Box 1's CSS live via JavaScript.

### `2-box-model-lab-refined.html`
The refined version, generated from a follow-up prompt building on the
first. Adds independent top/right/bottom/left sliders for padding, border
width, and margin, plus a corner-radius slider — instead of one shared
value per property.

### `3-flexbox-grid-playground.html`
A separate playground for Flexbox and Grid. A container with 5 items and
dropdowns to change `display` (block/flex/grid), `flex-direction`,
`justify-content`, `align-items`, and `grid-template-columns`, all applied
live via JavaScript.

## Prompts used

**1. Initial Box Model prompt:**
> Act as a frontend web developer. Using your Canvas tool, Generate an
> interactive website that can be used for understanding the CSS Box Model
> and its relationship with the display property. The page must have two
> div elements, 'Box 1' and 'Box 2'... [full prompt as provided in the
> assignment]

**2. Refinement prompt:**
> Implement sliders to adjust the margin, padding, and border for each side
> (top, right, bottom, left) individually, and add a separate slider for
> the corner radius.

**3. Flexbox/Grid prompt:**
> Act as a frontend web developer. Using your Canvas tool, generate an
> interactive website that can be used as a playground for CSS Flexbox and
> Grid... [full prompt as provided in the assignment]
