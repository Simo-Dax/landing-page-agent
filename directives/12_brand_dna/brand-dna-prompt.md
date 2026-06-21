# Brand DNA Research Prompt

This is the exact prompt to run (with web search enabled) when the user provides a brand name and URL. Replace `[Brand]` and `[Target URL]` with the user's inputs.

---

Target Brand Name: [BRAND]
Target URL: [TARGET URL]

Role: Act as a Senior Brand Strategist conducting a full reverse-engineering of the target brand's visual and verbal identity.

Objective: Create a comprehensive Brand DNA document that will be used to write highly specific AI image generation prompts. Every detail matters because the output will be fed into an image model that needs exact specifications.

PHASE 1: EXTERNAL RESEARCH

Use web search to find the source of truth for this brand:
1. Design credits: Search for "who designed [Brand] branding", "[Brand] design agency case study", "[Brand] rebrand"
2. Public brand assets: Search for "[Brand] brand guidelines pdf", "[Brand] press kit", "[Brand] media kit", "[Brand] style guide"
3. Typography: Search for "[Brand] font", "[Brand] typeface", "what font does [Brand] use"
4. Colors: Search for "[Brand] brand colors", "[Brand] hex codes", "[Brand] color palette"
5. Packaging: Search for "[Brand] packaging design", "[Brand] unboxing", "[Brand] product photography"
6. Advertising: Search "[Brand]" in Meta Ad Library (facebook.com/ads/library) for current ad creative styles
7. Press and positioning: Search for "[Brand] brand story", "[Brand] founding story", "[Brand] mission"

PHASE 2: ON-SITE ANALYSIS

Visit the Target URL and analyze:
1. Voice and Tone: Read hero copy, About page, and product descriptions. Give me 5 distinct adjectives.
2. Photography Style: Describe lighting, color grading, composition, and subject matter.
3. Typography on site: Headline weight, body weight, letter-spacing, distinctive treatments.
4. Color application: Primary vs accent usage. Background colors. CTA color.
5. Layout density: Airy or dense? Grid-based or organic?
6. Packaging details: Physical appearance (materials, colors, shape, label placement, textures, translucency, matte vs gloss).

PHASE 3: COMPETITIVE CONTEXT

Search for 2-3 direct competitors and note visual differentiation.

PHASE 4: OUTPUT

Combine into this format:

BRAND DNA DOCUMENT

BRAND OVERVIEW
Name / Tagline / Design Agency / Voice Adjectives [5] / Positioning / Competitive Differentiation

VISUAL SYSTEM
Primary Font / Secondary Font / Primary Color [hex] / Secondary Color [hex] / Accent Color [hex] / Background Colors / CTA Color and Style

PHOTOGRAPHY DIRECTION
Lighting / Color Grading / Composition / Subject Matter / Props and Surfaces / Mood

PRODUCT DETAILS
Physical Description / Label-Logo Placement / Distinctive Features / Packaging System

AD CREATIVE STYLE
Typical formats / Text overlay style / Photo vs illustration / UGC usage / Offer presentation

IMAGE GENERATION PROMPT MODIFIER
Write a single 50-75 word paragraph to prepend to any image prompt to match this brand's visual identity. Include exact colors, font descriptions, photography direction, and mood.

DELIVERABLE FORMAT

Once the Brand DNA content is complete, output the entire document as a downloadable HTML file. The design should use the brand's own color palette, typography style, and visual mood as identified in the research ,  so the document itself looks and feels like the brand. Use clean professional layout with clear section headers, generous spacing, and a design quality that could be shown to a client or creative team. The file should be immediately downloadable and visually impressive on its own.
