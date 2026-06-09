import re

with open('/home/rom4ik/loadIndic/morphing_svg_b64.txt') as f:
    svg_b64 = f.read().strip()

css = f'''/* ==UserStyle==
@name         Gemini MD3 Morphing Loader
@namespace    github.com/openstyles/stylus
@version      1.1.0
@description  Replaces Gemini loading/thinking animations with MD3 morphing spinner
@author       Antigravity
@license      MIT
==/UserStyle== */

@-moz-document domain("gemini.google.com") {{

  /* =================================
     MD3 Morphing Loading Spinner
     Replaces loading indicators only
  ================================== */

  /* --- Material Design spinner components (precise tags) --- */
  mat-spinner,
  mat-progress-spinner,
  .mat-mdc-progress-spinner,
  .mat-progress-spinner,
  .gmat-mdc-progress-spinner {{
    background-color: #4285f4 !important;
    mask-image: url("data:image/svg+xml;base64,{svg_b64}") !important;
    -webkit-mask-image: url("data:image/svg+xml;base64,{svg_b64}") !important;
    mask-size: contain !important;
    -webkit-mask-size: contain !important;
    mask-position: center center !important;
    -webkit-mask-position: center center !important;
    mask-repeat: no-repeat !important;
    -webkit-mask-repeat: no-repeat !important;
  }}

  /* Hide SVG internals of Material spinners */
  mat-spinner svg,
  mat-progress-spinner svg,
  .mat-mdc-progress-spinner svg,
  .mat-progress-spinner svg,
  .gmat-mdc-progress-spinner svg {{
    display: none !important;
  }}

  /* --- Role-based progressbar (only circular, not text inputs) --- */
  [role="progressbar"]:not(input):not(textarea):not([contenteditable]) {{
    background-color: #4285f4 !important;
    mask-image: url("data:image/svg+xml;base64,{svg_b64}") !important;
    -webkit-mask-image: url("data:image/svg+xml;base64,{svg_b64}") !important;
    mask-size: contain !important;
    -webkit-mask-size: contain !important;
    mask-position: center center !important;
    -webkit-mask-position: center center !important;
    mask-repeat: no-repeat !important;
    -webkit-mask-repeat: no-repeat !important;
  }}

  [role="progressbar"]:not(input):not(textarea):not([contenteditable]) svg {{
    display: none !important;
  }}

}}
'''

with open('/home/rom4ik/loadIndic/gemini-md3.user.css', 'w') as f:
    f.write(css)

print(f'Created gemini-md3.user.css ({len(css)} bytes)')
