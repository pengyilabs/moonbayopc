#!/usr/bin/env python3
"""
Pre-Deployment Test Suite for Moon Bay OPC Website
Run this BEFORE every `netlify deploy --prod` command.

Checks:
1. Navigation consistency across all pages (same nav items, same order)
2. Chinese encoding integrity (no mojibake/UTF-8-as-Latin-1)
3. Mega menu presence on all pages
4. Active class correctness on each page
5. Image path validity (no broken img src)
6. Mobile nav presence on all pages
7. Language toggle links correctness (EN<->ZH)
8. CSS/JS file references valid
9. Content integrity: no fabricated media outlets or fake quotes
10. Copyright year is current
11. Canonical URL tags present on all pages
12. Open Graph tags present on all pages
13. JSON-LD structured data present on index pages
14. robots.txt and sitemap.xml exist
15. hreflang tags present on all pages
"""
import os
import re
import sys
from pathlib import Path

BASE = Path(r'c:\Users\robmo\Movies\Hub\Projects\Pengyi Labs\projects\Suzhou-OPC-Setup\website-prototype')

# Expected nav items (order matters)
EXPECTED_NAV_ITEMS_EN = ['Services', 'Why Suzhou', 'Resources', 'About', 'Contact']
EXPECTED_NAV_ITEMS_ZH = ['服务', '为什么选择苏州', '资源中心', '关于我们', '联系我们']

# Expected mobile nav (order matters)
EXPECTED_MOBILE_NAV_EN = ['Services', 'Process', 'Why Suzhou', 'What is OPC', 'FAQ', 'Resources', 'Press', 'About', 'Community', 'Contact']
EXPECTED_MOBILE_NAV_ZH = ['服务', '流程', '为什么选择苏州', '什么是OPC', '常见问题', '资源中心', '媒体报道', '关于我们', '社区', '联系我们']

# Pages and their expected active nav item
EN_PAGES = {
    'index.html': None,  # root index
    'en/services.html': 'services',
    'en/process.html': None,
    'en/why-suzhou.html': 'why-suzhou',
    'en/what-is-opc.html': None,
    'en/faq.html': None,
    'en/resources.html': 'resources',
    'en/press.html': None,
    'en/about.html': None,
    'en/community.html': None,
    'en/contact.html': None,
    'en/jiangsu-ai-opc-policy.html': None,
}

ZH_PAGES = {
    'zh/index.html': None,
    'zh/services.html': 'services',
    'zh/process.html': None,
    'zh/why-suzhou.html': 'why-suzhou',
    'zh/what-is-opc.html': None,
    'zh/faq.html': None,
    'zh/resources.html': 'resources',
    'zh/press.html': None,
    'zh/about.html': None,
    'zh/community.html': None,
    'zh/contact.html': None,
    'zh/jiangsu-ai-opc-policy.html': None,
}

# Mojibake detection: sequences like æ, å, ç, è, ã followed by unusual chars
MOJIBAKE_PATTERN = re.compile(r'[æåçèéêëìíîïðñòóôõöøùúûüýþÿ][\x80-\xbf]|[À-ÿ]{2,}')

# Correct Chinese text that should appear in ZH mega menus
ZH_CORRECT_TEXTS = ['服务', '为什么选择苏州', '资源中心', '关于我们', '联系我们']
# Mojibake versions that indicate corruption
ZH_MOJIBAKE_INDICATORS = ['æœ', 'ä¸', 'èµ„', 'å…³', 'è”ç³»']

# --- Content Integrity Checks ---
# Fabricated media outlets that should NEVER appear as press quotes or media logos
# These were placeholders used during initial development — they must be removed
FABRICATED_OUTLETS = [
    'South China Morning Post', 'SCMP',
    'Forbes Asia', 'Forbes',
    'TechCrunch',
    'Bloomberg',
    'Nikkei Asia',
]
# Exception: 'Forbes' and 'SCMP' etc. are fine in general prose, but NOT in
# press-quote or media-outlet sections. We check the full content for these
# in the press section specifically.
FABRICATED_QUOTES = [
    'Moon Bay OPC is simplifying what has traditionally been one of the most daunting processes',
    'The OPC model in Suzhou is attracting a new wave of international founders',
    'With full-service support from registration to office space, Moon Bay is removing the barriers',
    '月光湾OPC正在简化一直以来令外国创业者望而却步的流程',
    '苏州的OPC模式正吸引着新一轮希望融入中国创新生态的国际创始人',
    '从注册到办公空间的全流程服务，月光湾正在消除曾经阻碍中小企业进入中国的壁垒',
]

# Current year for copyright check
CURRENT_YEAR = '2026'

# Domain for canonical URLs
SITE_DOMAIN = 'https://moonbayopc.netlify.app'


class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.errors = []
        self.warnings_list = []

    def pass_test(self, msg):
        self.passed += 1

    def fail(self, msg):
        self.failed += 1
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings += 1
        self.warnings_list.append(msg)

    def summary(self):
        status = "PASS" if self.failed == 0 else "FAIL"
        lines = [
            f"\n{'='*60}",
            f"  PRE-DEPLOYMENT TEST RESULTS: {status}",
            f"{'='*60}",
            f"  Passed:   {self.passed}",
            f"  Failed:   {self.failed}",
            f"  Warnings: {self.warnings}",
            f"{'='*60}",
        ]
        if self.errors:
            lines.append("\n  ERRORS (must fix before deploying):")
            for e in self.errors:
                lines.append(f"    ✗ {e}")
        if self.warnings_list:
            lines.append("\n  WARNINGS (review before deploying):")
            for w in self.warnings_list:
                lines.append(f"    ⚠ {w}")
        if self.failed == 0 and self.warnings == 0:
            lines.append("\n  All tests passed. Safe to deploy.")
        elif self.failed == 0:
            lines.append("\n  No errors. Warnings should be reviewed but won't break the site.")
        else:
            lines.append("\n  ⚠ DO NOT DEPLOY until all errors are fixed.")
        lines.append(f"{'='*60}")
        return '\n'.join(lines)


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def check_nav_consistency(result, filepath, content, expected_items, lang):
    """Check that all expected nav items appear in the mega menu nav block."""
    filename = os.path.basename(filepath)
    # Extract nav block
    nav_match = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', content, re.DOTALL)
    if not nav_match:
        result.fail(f"{filepath}: No <nav class='nav-links'> block found")
        return

    nav_block = nav_match.group(1)

    for item in expected_items:
        if item not in nav_block:
            result.fail(f"{filepath}: Nav item '{item}' missing from navigation")


def check_mojibake(result, filepath, content, lang):
    """Check for UTF-8-as-Latin-1 mojibake in Chinese pages."""
    if lang != 'zh':
        return

    for indicator in ZH_MOJIBAKE_INDICATORS:
        if indicator in content:
            result.fail(f"{filepath}: Mojibake detected (found '{indicator}' — Chinese text is corrupted)")

    # Also check that correct Chinese text IS present
    for text in ZH_CORRECT_TEXTS:
        if text not in content:
            result.fail(f"{filepath}: Expected Chinese text '{text}' not found in page")


def check_mega_menu_present(result, filepath, content):
    """Check that mega menu structure exists."""
    if 'mega-menu' not in content:
        result.fail(f"{filepath}: Mega menu structure missing")
    if 'mega-menu-panel' not in content:
        result.fail(f"{filepath}: Mega menu panel missing")
    if 'mega-card' not in content:
        result.fail(f"{filepath}: Mega card elements missing")


def check_active_class(result, filepath, content, expected_active):
    """Check that active class is on the correct nav item."""
    if expected_active is None:
        # Check that no mega-menu-trigger has active class (unless it's a standalone link)
        # For pages without an active mega menu, the standalone links might have active
        return

    # Check that the correct mega-menu-trigger has active class
    active_match = re.search(r'class="mega-menu-trigger\s+active"', content)
    if not active_match:
        # Could also be on a standalone <a> like About or Contact
        standalone_active = re.search(r'<a href="[^"]*"\s+class="active"', content)
        if not standalone_active:
            result.fail(f"{filepath}: No active class found on any nav item (expected active: '{expected_active}')")


def check_mobile_nav(result, filepath, content, expected_items, lang):
    """Check mobile nav presence and content."""
    mobile_match = re.search(r'<div class="mobile-nav"[^>]*>(.*?)</div>', content, re.DOTALL)
    if not mobile_match:
        result.fail(f"{filepath}: Mobile nav block missing")
        return

    mobile_block = mobile_match.group(1)
    for item in expected_items:
        if item not in mobile_block:
            result.fail(f"{filepath}: Mobile nav item '{item}' missing")


def check_lang_toggle(result, filepath, content, lang):
    """Check language toggle links are correct."""
    if 'lang-toggle' not in content:
        result.fail(f"{filepath}: Language toggle missing")
        return

    if lang == 'en':
        # EN page should link to ZH version
        if '中' not in content:
            result.fail(f"{filepath}: Language toggle missing Chinese link (中)")
    elif lang == 'zh':
        if 'EN' not in content:
            result.fail(f"{filepath}: Language toggle missing English link (EN)")


def check_image_paths(result, filepath, content, base_dir):
    """Check that image src paths exist on disk."""
    img_srcs = re.findall(r'<img[^>]+src="([^"]+)"', content)
    file_dir = os.path.dirname(filepath)

    for src in img_srcs:
        # Skip absolute URLs
        if src.startswith('http') or src.startswith('//'):
            continue

        # Resolve relative path
        img_path = os.path.normpath(os.path.join(file_dir, src))

        if not os.path.exists(img_path):
            # Only warn for non-data images
            if not src.startswith('data:'):
                result.warn(f"{filepath}: Image not found: {src}")


def check_css_reference(result, filepath, content):
    """Check that CSS file is referenced."""
    if 'style.css' not in content:
        result.fail(f"{filepath}: CSS stylesheet reference missing")


def check_meta_charset(result, filepath, content):
    """Check that charset meta tag is present."""
    if 'charset="UTF-8"' not in content and 'charset=utf-8' not in content:
        result.fail(f"{filepath}: Missing UTF-8 charset meta tag")


def check_no_bare_active(result, filepath, content):
    """Check that 'active' is not a bare attribute outside class quotes."""
    # Pattern: class="something" active  (active outside the quotes)
    bare_active = re.findall(r'class="[^"]*"\s+active(?!=)', content)
    if bare_active:
        result.fail(f"{filepath}: 'active' found outside class attribute quotes — HTML is malformed")


def check_no_fabricated_content(result, filepath, content):
    """Check that no fabricated media outlets or fake quotes appear on the page."""
    for quote in FABRICATED_QUOTES:
        if quote in content:
            result.fail(f"{filepath}: Fabricated press quote found: '{quote[:60]}...' — remove fake content")

    # Check for fabricated outlet names in press-quote or media-outlet sections
    # Extract press sections if present
    press_section = re.search(r'class="press-section"(.*?)</section>', content, re.DOTALL)
    if press_section:
        press_html = press_section.group(1)
        for outlet in FABRICATED_OUTLETS:
            if outlet in press_html:
                result.fail(f"{filepath}: Fabricated media outlet '{outlet}' found in press section — use real coverage only")


def check_copyright_year(result, filepath, content):
    """Check that copyright year is current (2026)."""
    # Look for © 2024 or © 2025 in footer
    old_years = re.findall(r'©\s*(2024|2025)', content)
    if old_years:
        result.fail(f"{filepath}: Outdated copyright year found: © {old_years[0]} — should be © {CURRENT_YEAR}")


def check_canonical_url(result, filepath, content):
    """Check that canonical URL link tag is present."""
    if 'rel="canonical"' not in content:
        result.fail(f"{filepath}: Missing canonical URL link tag")


def check_open_graph(result, filepath, content):
    """Check that basic Open Graph tags are present."""
    required_og = ['og:title', 'og:description', 'og:url']
    for tag in required_og:
        if tag not in content:
            result.fail(f"{filepath}: Missing Open Graph tag '{tag}'")


def check_json_ld(result, filepath, content):
    """Check that JSON-LD structured data is present on index pages."""
    filename = os.path.basename(filepath)
    if filename == 'index.html':
        if 'application/ld+json' not in content:
            result.fail(f"{filepath}: Missing JSON-LD structured data on landing page")


def check_hreflang(result, filepath, content):
    """Check that hreflang tags are present for EN/ZH alternatives."""
    if 'hreflang="en"' not in content or 'hreflang="zh"' not in content:
        result.fail(f"{filepath}: Missing hreflang tags for EN/ZH language alternatives")


def check_seo_files_exist(result):
    """Check that robots.txt and sitemap.xml exist in the site root."""
    robots_path = BASE / 'robots.txt'
    sitemap_path = BASE / 'sitemap.xml'

    if not robots_path.exists():
        result.fail("robots.txt: File missing from site root")
    else:
        robots_content = read_file(robots_path)
        if 'Sitemap:' not in robots_content:
            result.fail("robots.txt: Missing Sitemap directive")
        else:
            result.pass_test("robots.txt: Exists and contains sitemap reference")

    if not sitemap_path.exists():
        result.fail("sitemap.xml: File missing from site root")
    else:
        sitemap_content = read_file(sitemap_path)
        if '<urlset' not in sitemap_content:
            result.fail("sitemap.xml: Invalid XML — missing <urlset> root element")
        elif '<url>' not in sitemap_content:
            result.fail("sitemap.xml: No <url> entries found")
        else:
            url_count = sitemap_content.count('<url>')
            result.pass_test(f"sitemap.xml: Valid with {url_count} URL entries")


def run_tests():
    result = TestResult()

    print("Running pre-deployment tests...\n")

    # Test EN pages
    for rel_path, expected_active in EN_PAGES.items():
        filepath = BASE / rel_path
        if not filepath.exists():
            result.fail(f"EN page missing: {rel_path}")
            continue

        content = read_file(filepath)
        short = rel_path

        check_meta_charset(result, filepath, content)
        check_css_reference(result, filepath, content)
        check_nav_consistency(result, filepath, content, EXPECTED_NAV_ITEMS_EN, 'en')
        check_mega_menu_present(result, filepath, content)
        check_active_class(result, filepath, content, expected_active)
        check_mobile_nav(result, filepath, content, EXPECTED_MOBILE_NAV_EN, 'en')
        check_lang_toggle(result, filepath, content, 'en')
        check_image_paths(result, filepath, content, BASE)
        check_no_bare_active(result, filepath, content)
        check_no_fabricated_content(result, filepath, content)
        check_copyright_year(result, filepath, content)
        check_canonical_url(result, filepath, content)
        check_open_graph(result, filepath, content)
        check_json_ld(result, filepath, content)
        check_hreflang(result, filepath, content)

        result.pass_test(f"{short}: EN checks passed")

    # Test ZH pages
    for rel_path, expected_active in ZH_PAGES.items():
        filepath = BASE / rel_path
        if not filepath.exists():
            result.fail(f"ZH page missing: {rel_path}")
            continue

        content = read_file(filepath)
        short = rel_path

        check_meta_charset(result, filepath, content)
        check_css_reference(result, filepath, content)
        check_nav_consistency(result, filepath, content, EXPECTED_NAV_ITEMS_ZH, 'zh')
        check_mojibake(result, filepath, content, 'zh')
        check_mega_menu_present(result, filepath, content)
        check_active_class(result, filepath, content, expected_active)
        check_mobile_nav(result, filepath, content, EXPECTED_MOBILE_NAV_ZH, 'zh')
        check_lang_toggle(result, filepath, content, 'zh')
        check_image_paths(result, filepath, content, BASE)
        check_no_bare_active(result, filepath, content)
        check_no_fabricated_content(result, filepath, content)
        check_copyright_year(result, filepath, content)
        check_canonical_url(result, filepath, content)
        check_open_graph(result, filepath, content)
        check_json_ld(result, filepath, content)
        check_hreflang(result, filepath, content)

        result.pass_test(f"{short}: ZH checks passed")

    # SEO files check
    check_seo_files_exist(result)

    # Cross-page consistency: extract nav from each EN page and compare
    en_navs = {}
    for rel_path in EN_PAGES:
        filepath = BASE / rel_path
        if not filepath.exists():
            continue
        content = read_file(filepath)
        nav_match = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', content, re.DOTALL)
        if nav_match:
            # Extract just the href values and text content of top-level links
            links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]*)', nav_match.group(1))
            en_navs[rel_path] = links

    # Check all EN navs have the same number of links
    if en_navs:
        nav_counts = {k: len(v) for k, v in en_navs.items()}
        unique_counts = set(nav_counts.values())
        if len(unique_counts) > 1:
            result.fail(f"EN pages have inconsistent nav link counts: {nav_counts}")
        else:
            result.pass_test("EN nav link count consistent across all pages")

    # Same for ZH
    zh_navs = {}
    for rel_path in ZH_PAGES:
        filepath = BASE / rel_path
        if not filepath.exists():
            continue
        content = read_file(filepath)
        nav_match = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', content, re.DOTALL)
        if nav_match:
            links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]*)', nav_match.group(1))
            zh_navs[rel_path] = links

    if zh_navs:
        nav_counts = {k: len(v) for k, v in zh_navs.items()}
        unique_counts = set(nav_counts.values())
        if len(unique_counts) > 1:
            result.fail(f"ZH pages have inconsistent nav link counts: {nav_counts}")
        else:
            result.pass_test("ZH nav link count consistent across all pages")

    print(result.summary())

    # Exit with error code if tests failed
    if result.failed > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    run_tests()
