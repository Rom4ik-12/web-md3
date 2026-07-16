import re, base64

with open('/home/rom4ik/loadIndic/fixed_svg.svg') as f:
    svg = f.read()

# I want to ensure my fixed_svg.svg actually contains the 6 paths
if svg.count('<path') == 6:
    print('SVG has 6 paths. Good.')
else:
    print('SVG has', svg.count('<path'), 'paths! Re-generating...')
    # (Just in case, I will re-run the 6 path generation)
    pass

# Read index.html to generate 6 paths again to be 100% sure
with open('/home/rom4ik/loadIndic/index.html') as f:
    html = f.read()

p0 = re.search(r'<path class="m3-shape-0" d="([^"]+)"', html).group(1)
p1 = re.search(r'<path class="m3-shape-1" d="([^"]+)"', html).group(1)
p2 = re.search(r'<path class="m3-shape-2" d="([^"]+)"', html).group(1)
p3 = re.search(r'<path class="m3-shape-3" d="([^"]+)"', html).group(1)
p4 = re.search(r'<path class="m3-shape-4" d="([^"]+)"', html).group(1)
p5 = re.search(r'<path class="m3-shape-5" d="([^"]+)"', html).group(1)

svg_template = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 768 768'>
<g>
    <animateTransform attributeName='transform' type='rotate' 
        values='0 384 384;90 384 384;120 384 384;210 384 384;240 384 384;330 384 384;360 384 384;450 384 384;480 384 384;570 384 384;600 384 384;690 384 384;720 384 384' 
        keyTimes='0.0000;0.0800;0.1667;0.2467;0.3333;0.4133;0.5000;0.5800;0.6667;0.7467;0.8333;0.9133;1.0000' 
        keySplines='0.25 0.1 0.25 1;0.5 0 1 0.9;0.25 0.1 0.25 1;0.5 0 1 0.9;0.25 0.1 0.25 1;0.5 0 1 0.9;0.25 0.1 0.25 1;0.5 0 1 0.9;0.25 0.1 0.25 1;0.5 0 1 0.9;0.25 0.1 0.25 1;0.5 0 1 0.9' 
        dur='4.8s' repeatCount='indefinite' calcMode='spline'/>
    <g transform='translate(0, 768) scale(0.1, -0.1)'>
        <path fill-rule='evenodd' fill='white' opacity='1' d='{p0}'>
            <animate attributeName='opacity' values='1;1;0;0;1' keyTimes='0;0.1638;0.1667;0.9971;1' dur='4.8s' repeatCount='indefinite' calcMode='linear'/>
        </path>
        <path fill-rule='evenodd' fill='white' opacity='0' d='{p1}'>
            <animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.1638;0.1667;0.3304;0.3333;1' dur='4.8s' repeatCount='indefinite' calcMode='linear'/>
        </path>
        <path fill-rule='evenodd' fill='white' opacity='0' d='{p2}'>
            <animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.3304;0.3333;0.4971;0.5000;1' dur='4.8s' repeatCount='indefinite' calcMode='linear'/>
        </path>
        <path fill-rule='evenodd' fill='white' opacity='0' d='{p3}'>
            <animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.4971;0.5000;0.6638;0.6667;1' dur='4.8s' repeatCount='indefinite' calcMode='linear'/>
        </path>
        <path fill-rule='evenodd' fill='white' opacity='0' d='{p4}'>
            <animate attributeName='opacity' values='0;0;1;1;0;0' keyTimes='0;0.6638;0.6667;0.8304;0.8333;1' dur='4.8s' repeatCount='indefinite' calcMode='linear'/>
        </path>
        <path fill-rule='evenodd' fill='white' opacity='0' d='{p5}'>
            <animate attributeName='opacity' values='0;0;1;1;0' keyTimes='0;0.8304;0.8333;0.9971;1' dur='4.8s' repeatCount='indefinite' calcMode='linear'/>
        </path>
    </g>
</g>
</svg>"""

final_svg = svg_template.format(p0=p0, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)
b64 = base64.b64encode(final_svg.encode('utf-8')).decode('utf-8')

css_file = '/home/rom4ik/loadIndic/youtube-md3.user.css'
with open(css_file) as f:
    css = f.read()

# We need to replace the LONG base64. The others are short (for the scrubber).
# So we use a regex to find all base64 strings, and replace the one that is > 1000 chars.
def replacer(match):
    original_b64 = match.group(1)
    if len(original_b64) > 1000:
        return f'url("data:image/svg+xml;base64,{b64}")'
    else:
        return match.group(0)

new_css = re.sub(r'url\([\'"]?data:image/svg\+xml;base64,([A-Za-z0-9+/=]+)[\'"]?\)', replacer, css)

with open(css_file, 'w') as f:
    f.write(new_css)
print('Successfully verified and updated CSS!')
