import os

with open('/home/rom4ik/loadIndic/morphing_svg_b64.txt') as f:
    svg_b64 = f.read().strip()

css_template = f"""/* ==UserStyle==
@name         ChatGPT MD3 Morphing Loader
@namespace    github.com/openstyles/stylus
@version      1.1.0
@description  Replaces ChatGPT loading/thinking animations with MD3 morphing spinner
@author       Antigravity
@license      MIT
==/UserStyle== */

@-moz-document domain("chatgpt.com"), domain("chat.openai.com") {{

  /* --- ChatGPT loading and typing indicators --- */
  [data-testid="typing-indicator"],
  [class*="loading-spinner"],
  [class*="spinner-icon"],
  svg[class*="animate-spin"],
  .result-streaming.pulse {{
    background-color: currentColor !important;
    mask-image: url("data:image/svg+xml;base64,{svg_b64}") !important;
    -webkit-mask-image: url("data:image/svg+xml;base64,{svg_b64}") !important;
    mask-size: contain !important;
    -webkit-mask-size: contain !important;
    mask-position: center center !important;
    -webkit-mask-position: center center !important;
    mask-repeat: no-repeat !important;
    -webkit-mask-repeat: no-repeat !important;
    
    /* Sizing for the spinner */
    display: inline-block !important;
    width: 24px !important;
    height: 24px !important;
  }}

  /* Hide original internal dots/circles/paths inside loaders */
  [data-testid="typing-indicator"] > *,
  [class*="loading-spinner"] > *,
  [class*="spinner-icon"] > *,
  svg[class*="animate-spin"] > *,
  .result-streaming.pulse > * {{
    display: none !important;
  }}

}}
"""

with open('/home/rom4ik/loadIndic/chatgpt-md3.user.css', 'w') as f:
    f.write(css_template)

print("Generated ChatGPT UserStyle CSS successfully!")
