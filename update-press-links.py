"""Update press card links to point to internal pages instead of external URLs."""
import os

base = r"C:\Users\robmo\Movies\Hub\Projects\Pengyi Labs\projects\Suzhou-OPC-Setup\website-prototype"

# Map of external URLs to internal press page paths
replacements = {
    "https://weixin.qq.com/sph/AkXkd91JH0": "press/moroccan-entrepreneur-suzhou.html",
    "https://weixin.qq.com/sph/APe5dhPNV2": "press/enterprise-ai-transformation.html",
    "https://mp.weixin.qq.com/s/XounXneaBx5by04bTBezSQ": "press/sip-opc-community-video.html",
    "https://mp.weixin.qq.com/s/LJxwTHCC1Q_ButEXcc6TBw": "press/founder-philosophy-choosing-small.html",
    "https://weixin.qq.com/sph/Ah27dyShnD": "press/hengtai-zero-space-opc.html",
    "https://weixin.qq.com/sph/AE8FmmUgOw": "press/opc-talent-apartment-signing.html",
    "https://weixin.qq.com/sph/AoYrYT6Pw8": "press/signing-ceremony-coverage.html",
    "https://mp.weixin.qq.com/s/uIEOTHA2O7X8d0piRodyjw": "press/hengtai-zero-space-agreement.html",
    "https://mp.weixin.qq.com/s/wwwgP5_-auCb_a1-JSrrTQ": "press/opc-entrepreneurship-philosophy.html",
    "https://mp.weixin.qq.com/s/uhWDEFIVGnqsOyx4vMMPCQ": "press/moon-bay-joins-dpa.html",
    "https://mp.weixin.qq.com/s/GUzPifvWmg16Jh3vomCXUg": "press/mia-opc-license.html",
    "https://mp.weixin.qq.com/s/D567fNyB5U1c2dthL88Yuw": "press/suzhou-news-first-foreigner-opc.html",
    "https://mp.weixin.qq.com/s/gIVqPiId-cSUV_bXJNepWg": "press/first-foreigner-opc-license.html",
    "https://weixin.qq.com/sph/AahddTKwrO": "press/china-vs-us-ai-documentary.html",
}

# Also update the featured story link
featured_replacements = {
    "https://mp.weixin.qq.com/s/gIVqPiId-cSUV_bXJNepWg": "press/first-foreigner-opc-license.html",
}

files = [
    os.path.join(base, "en", "press.html"),
    os.path.join(base, "zh", "press.html"),
]

for filepath in files:
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {filepath}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    for old_url, new_path in replacements.items():
        # Replace various patterns
        patterns = [
            f'href="{old_url}" class="press-link" target="_blank" rel="noopener">',
            f'href="{old_url}" class="press-link">',
        ]
        for pat in patterns:
            # Replace with different label texts
            for label in ["Watch Video", "Watch on WeChat", "Read Article", "Watch on WeChat Channels"]:
                old = f"{pat}\n            {label}\n"
                if old in content:
                    new = f'href="{new_path}" class="press-link">\n            Read More\n'
                    content = content.replace(old, new)
                    count += 1
                    break

    # Also update featured story link
    for old_url, new_path in featured_replacements.items():
        old = f'href="{old_url}" class="press-link" target="_blank" rel="noopener"'
        new = f'href="{new_path}" class="press-link"'
        content = content.replace(old, new)
        count += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  Updated {count} links in {os.path.basename(filepath)}")

print("Done!")