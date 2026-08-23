"""Update remaining Chinese press page links - handles multi-line href patterns."""
import re

filepath = r"C:\Users\robmo\Movies\Hub\Projects\Pengyi Labs\projects\Suzhou-OPC-Setup\website-prototype\zh\press.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Map external URLs to internal paths
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

count = 0
for old_url, new_path in replacements.items():
    # Handle: href="url"\nclass="press-link" target="_blank" rel="noopener">
    # (href on one line, class on next)
    escaped_url = re.escape(old_url)
    
    # Pattern 1: href="url"\nclass="press-link" target="_blank" rel="noopener">
    pattern = re.compile(
        r'href="' + escaped_url + r'"\s*\n\s*class="press-link" target="_blank" rel="noopener">'
    )
    replacement = 'href="' + new_path + '" class="press-link">'
    content = pattern.sub(replacement, content)
    
    # Pattern 2: href="url" class="press-link" target="_blank" rel="noopener">
    pattern2 = re.compile(
        r'href="' + escaped_url + r'" class="press-link" target="_blank" rel="noopener">'
    )
    content = pattern2.sub('href="' + new_path + '" class="press-link">', content)
    
    # Count matches
    if pattern.search(content) or pattern2.search(content):
        count += 1

# Update labels: replace "观看视频", "在微信观看", "阅读文章" with "阅读更多"
labels = ["观看视频", "在微信观看", "阅读文章", "在微信阅读"]
for label in labels:
    content = content.replace(f"            {label}\n", "            阅读更多\n")
    content = content.replace(f"              {label}\n", "              阅读更多\n")

# Fix the bottom section play button
content = content.replace(
    'href="https://weixin.qq.com/sph/AahddTKwrO"\ntarget="_blank" rel="noopener" style="display: inline-block; text-decoration: none;"',
    'href="press/china-vs-us-ai-documentary.html"'
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated links in zh/press.html")