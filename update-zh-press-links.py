"""Update Chinese press page card links to internal pages."""
import os

base = r"C:\Users\robmo\Movies\Hub\Projects\Pengyi Labs\projects\Suzhou-OPC-Setup\website-prototype"
filepath = os.path.join(base, "zh", "press.html")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Map external URLs to internal paths
replacements = [
    ("https://weixin.qq.com/sph/AkXkd91JH0", "press/moroccan-entrepreneur-suzhou.html"),
    ("https://weixin.qq.com/sph/APe5dhPNV2", "press/enterprise-ai-transformation.html"),
    ("https://mp.weixin.qq.com/s/XounXneaBx5by04bTBezSQ", "press/sip-opc-community-video.html"),
    ("https://mp.weixin.qq.com/s/LJxwTHCC1Q_ButEXcc6TBw", "press/founder-philosophy-choosing-small.html"),
    ("https://weixin.qq.com/sph/Ah27dyShnD", "press/hengtai-zero-space-opc.html"),
    ("https://weixin.qq.com/sph/AE8FmmUgOw", "press/opc-talent-apartment-signing.html"),
    ("https://weixin.qq.com/sph/AoYrYT6Pw8", "press/signing-ceremony-coverage.html"),
    ("https://mp.weixin.qq.com/s/uIEOTHA2O7X8d0piRodyjw", "press/hengtai-zero-space-agreement.html"),
    ("https://mp.weixin.qq.com/s/wwwgP5_-auCb_a1-JSrrTQ", "press/opc-entrepreneurship-philosophy.html"),
    ("https://mp.weixin.qq.com/s/uhWDEFIVGnqsOyx4vMMPCQ", "press/moon-bay-joins-dpa.html"),
    ("https://mp.weixin.qq.com/s/GUzPifvWmg16Jh3vomCXUg", "press/mia-opc-license.html"),
    ("https://mp.weixin.qq.com/s/D567fNyB5U1c2dthL88Yuw", "press/suzhou-news-first-foreigner-opc.html"),
    ("https://mp.weixin.qq.com/s/gIVqPiId-cSUV_bXJNepWg", "press/first-foreigner-opc-license.html"),
    ("https://weixin.qq.com/sph/AahddTKwrO", "press/china-vs-us-ai-documentary.html"),
]

# Also update featured story
featured_replacements = [
    ("https://mp.weixin.qq.com/s/gIVqPiId-cSUV_bXJNepWg", "press/first-foreigner-opc-license.html"),
]

count = 0
for old_url, new_path in replacements:
    # Replace the full anchor tag with its content
    # Pattern: href="old_url" class="press-link" target="_blank" rel="noopener">\n              label\n
    for label in ["观看视频", "在微信观看", "阅读文章", "在微信阅读"]:
        old = f'href="{old_url}" class="press-link" target="_blank" rel="noopener">\n              {label}\n'
        new = f'href="{new_path}" class="press-link">\n              阅读更多\n'
        if old in content:
            content = content.replace(old, new)
            count += 1
            break

# Also try with 12-space indent
for old_url, new_path in replacements:
    for label in ["观看视频", "在微信观看", "阅读文章", "在微信阅读"]:
        old = f'href="{old_url}" class="press-link" target="_blank" rel="noopener">\n            {label}\n'
        new = f'href="{new_path}" class="press-link">\n            阅读更多\n'
        if old in content:
            content = content.replace(old, new)
            count += 1
            break

# Fix featured story
for old_url, new_path in featured_replacements:
    old = f'href="{old_url}" class="press-link" target="_blank" rel="noopener"'
    new = f'href="{new_path}" class="press-link"'
    content = content.replace(old, new)
    count += 1

# Fix featured story label
content = content.replace("阅读文章\n", "阅读更多\n")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated {count} links in zh/press.html")