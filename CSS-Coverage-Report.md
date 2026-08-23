# CSS Coverage Report: Subpages vs. style.css

**Project:** Suzhou OPC Website Prototype  
**Date:** 2026-07-08  
**CSS File:** `css/style.css` (192 class selectors defined)  
**HTML Files Analyzed:** 9 subpages under `en/`

---

## Executive Summary

There are **114 CSS classes used in the 9 English subpages that have NO matching rules in `style.css`**. This means approximately 45% of all unique classes used across the subpages are unstyled. The CSS file was likely written for the homepage first, and the subpage-specific components were never added to it.

---

## 1. All Unique CSS Classes Used Across Subpages

**Total: 201 unique classes** across 9 files.

| File | Class Count |
|------|-------------|
| about.html | 67 |
| community.html | 70 |
| contact.html | 63 |
| faq.html | 47 |
| press.html | 55 |
| process.html | 76 |
| services.html | 62 |
| what-is-opc.html | 71 |
| why-suzhou.html | 70 |

### Shared classes (used across ALL 9 subpages):
`btn`, `btn--white`, `container`, `cta-band`, `cta-band__desc`, `cta-band__title`, `footer`, `footer__address`, `footer__bottom`, `footer__brand`, `footer__contact`, `footer__grid`, `footer__link`, `footer__logo`, `footer__logo-accent`, `footer__nav`, `footer__nav-list`, `footer__nav-title`, `footer__social`, `footer__social-label`, `footer__social-list`, `footer__social-value`, `footer__tagline`, `footer__tagline-sub`, `nav`, `nav__actions`, `nav__container`, `nav__hamburger`, `nav__hamburger-line`, `nav__lang`, `nav__lang-active`, `nav__lang-divider`, `nav__lang-link`, `nav__link`, `nav__links`, `nav__logo`, `nav__logo-accent`, `page-hero`, `page-hero__breadcrumb`, `page-hero__container`, `page-hero__subtitle`, `page-hero__title`, `section`, `section--light`, `section-label`, `section__header`, `section__title`

---

## 2. Classes MISSING from style.css (used in HTML but not defined in CSS)

**Total: 114 missing classes** -- These will have NO styling applied.

### 2A. Page-Specific Component Classes (no rules at all)

#### benefit-card / benefits__grid (3 files: why-suzhou.html, community.html, what-is-opc.html)
- `.benefit-card`
- `.benefit-card__desc`
- `.benefit-card__icon`
- `.benefit-card__title`
- `.benefits__grid`

#### callout (5 files: services.html, about.html, press.html, community.html, what-is-opc.html)
- `.callout`
- `.callout__text`

#### comparison (3 files: process.html, why-suzhou.html, what-is-opc.html)
- `.comparison`
- `.comparison__header`
- `.comparison__subtitle`
- `.comparison__table`
- `.comparison__table--col-highlight`
- `.comparison__table--highlight`
- `.comparison__table-wrap`
- `.comparison__title`

#### contact form (1 file: contact.html)
- `.contact__field`
- `.contact__form-card`
- `.contact__form-title`
- `.contact__grid`
- `.contact__info`
- `.contact__info-card`
- `.contact__info-content`
- `.contact__info-icon`
- `.contact__info-label`
- `.contact__info-note`
- `.contact__info-sub`
- `.contact__info-value`
- `.contact__input`
- `.contact__map`
- `.contact__map-icon`
- `.contact__map-sub`
- `.contact__map-text`
- `.contact__optional`
- `.contact__required`
- `.contact__select`
- `.contact__submit`
- `.contact__textarea`

#### content-platform (3 files: about.html, community.html, press.html)
- `.content-platform`
- `.content-platform__body`
- `.content-platform__card`
- `.content-platform__desc`
- `.content-platform__icon`
- `.content-platform__stat`
- `.content-platform__title`

#### credential-card (2 files: about.html, community.html)
- `.credential-card`
- `.credential-card__badge`
- `.credential-card__text`
- `.credentials__grid`

#### myth-card (1 file: what-is-opc.html)
- `.myth-card`
- `.myth-card__fact`
- `.myth-card__icon`
- `.myth-card__myth`
- `.myths__grid`

#### notes (1 file: process.html)
- `.notes`
- `.notes__list`
- `.notes__title`

#### profile-card (1 file: about.html)
- `.profile-card`
- `.profile-card__avatar`
- `.profile-card__bio`
- `.profile-card__body`
- `.profile-card__content-brand`
- `.profile-card__content-brand-icon`
- `.profile-card__name`
- `.profile-card__name-alt`

#### qualify-item (2 files: community.html, what-is-opc.html)
- `.qualify-item`
- `.qualify-item__icon`
- `.qualify-list`

#### service-detail (2 files: services.html, press.html)
- `.service-detail`
- `.service-detail__card`
- `.service-detail__card--full`
- `.service-detail__desc`
- `.service-detail__grid`
- `.service-detail__icon`
- `.service-detail__includes`
- `.service-detail__includes-title`
- `.service-detail__title`
- `.services__cta`

#### timeline (1 file: why-suzhou.html)
- `.timeline`
- `.timeline__content`
- `.timeline__desc`
- `.timeline__header`
- `.timeline__item`
- `.timeline__marker`
- `.timeline__title`

#### timeline-detail (1 file: process.html)
- `.timeline-detail`
- `.timeline-detail__col`
- `.timeline-detail__col--we`
- `.timeline-detail__col-title`
- `.timeline-detail__col-title--we`
- `.timeline-detail__col-title--you`
- `.timeline-detail__col-title-icon`
- `.timeline-detail__columns`
- `.timeline-detail__content`
- `.timeline-detail__duration`
- `.timeline-detail__header`
- `.timeline-detail__item`
- `.timeline-detail__list`
- `.timeline-detail__list--we`
- `.timeline-detail__list--you`
- `.timeline-detail__marker`
- `.timeline-detail__number`
- `.timeline-detail__title`

### 2B. Shared Component Classes Missing from CSS

These are used across multiple subpages but still have no CSS rule:

- `.page-hero__breadcrumb` -- used in ALL 9 subpages
- `.footer__lang-active` -- used in 5 files (about, contact, press, community, faq)
- `.footer__lang-link` -- used in 5 files (about, contact, press, community, faq)
- `.footer__nav` -- used in 9 files (all subpages)
- `.footer__services` -- used in 5 files (about, contact, press, community, faq)
- `.btn--amber` -- used in 1 file (contact.html)

### 2C. FAQ-Specific Naming Pattern Issue

The faq.html uses a DIFFERENT naming convention from what the CSS defines:

| HTML uses (faq.html) | CSS defines | Status |
|---------------------|-------------|--------|
| `.faq-item__answer` | `.faq-answer` / `.faq__answer` | **Naming mismatch** |
| `.faq-item__answer-inner` | *(nothing)* | **Missing entirely** |
| `.faq-item__icon` | `.faq__icon` | **Naming mismatch** |
| `.faq-item__question` | `.faq-question` / `.faq__question` | **Naming mismatch** |

The HTML uses `faq-item__*` (BEM with `faq-item` as block), but the CSS uses `faq__*` (BEM with `faq` as block) and `faq-*` (non-BEM fallback). These will NOT match.

---

## 3. Classes in CSS But Not Used in Subpages

**Total: 128 classes** in CSS that do not appear in any of the 9 subpages.

Many of these are legitimate -- they are used by the homepage (`index.html`) or are utility/state classes:

### Likely used by homepage:
`.hero`, `.hero__bg`, `.hero__container`, `.hero__headline`, `.hero__subheadline`, `.hero__ctas`, `.hero__trust-badges`, `.hero__badge`, `.hero__badge-icon`, `.hero__overlay`, `.hero__scroll`, `.hero__scroll-icon`, `.bento-grid`, `.bento-grid__item`, `.bento-grid__item--large`, `.trust-bar`, `.trust-bar__container`, `.trust-bar__item`, `.trust-bar__icon`, `.city-showcase` (and sub-parts), `.feature-split` (and sub-parts), `.feature-stat`, `.feature-stats`, `.steps` (and sub-parts), `.media-logos`, `.media-logo`, `.marquee` (and sub-parts)

### Button variants not used in subpages:
`.btn--cta`, `.btn--ghost`, `.btn--lg`, `.btn--orange`, `.btn--outline`, `.btn--outline-white`, `.btn--primary`, `.btn--secondary`, `.btn--sm`, `.btn-group`

### Card variants not used in subpages:
`.card`, `.card--featured`, `.card__icon`, `.card__link`, `.card__text`, `.card__title`

### State/utility classes:
`.is-open`, `.is-visible`, `.is-highlighted`, `.nav--scrolled`

### False positives from CSS parser (URL fragments, not real classes):
`.com`, `.googleapis`, `.org`, `.w3` -- these come from the `@import url(...)` Google Fonts line and are NOT actual CSS classes.

### Section variants not used in subpages:
`.section--alt`, `.section--cool`, `.section--lg`, `.section--purple`, `.section--sm`, `.section--white`

### Typography utilities not used in subpages:
`.text-center`, `.text-display`, `.text-label`, `.text-lead`, `.text-muted`, `.text-small`

### Layout utilities not used in subpages:
`.flex`, `.flex--between`, `.flex--center`, `.flex--wrap`, `.gap-4`, `.gap-6`, `.gap-8`, `.grid`, `.grid--2`, `.grid--3`, `.grid--4`

### Form classes not used in subpages:
`.form-group`, `.form-label`, `.form-input`, `.form-textarea`, `.form-select`, `.form-error`, `.form-hint`

### Image classes not used in subpages:
`.img-container`, `.img-container--aspect`, `.img-container--portrait`, `.img-container--square`

### Table classes not used in subpages:
`.table`, `.table-wrap`, `.table--comparison`

---

## 4. Naming Convention Issues

### 4A. `btn--amber` (contact.html)
The HTML uses `.btn--amber` but the CSS has no `--amber` modifier. The closest variants are:
- `.btn--cta` / `.btn--orange` (orange/CTA gradient)
- `.btn--primary` (same orange gradient)

**Recommendation:** Either add a `.btn--amber` rule or change HTML to use `.btn--cta` or `.btn--primary`.

### 4B. FAQ component naming (faq.html)
The HTML uses `faq-item__*` pattern but CSS defines `faq__*` pattern. This is a BEM block naming inconsistency:
- HTML: `.faq-item__question`, `.faq-item__answer`, `.faq-item__icon`
- CSS: `.faq__question`, `.faq__answer`, `.faq__icon`

**Recommendation:** Standardize to one convention. Either rename CSS selectors to `faq-item__*` or rename HTML classes to `faq__*`.

### 4C. `page-hero__breadcrumb` (all 9 subpages)
Used in every subpage but has zero CSS rules. This is a breadcrumb nav inside the page hero that is completely unstyled.

### 4D. Footer language switcher classes
`.footer__lang-active` and `.footer__lang-link` are used in 5 subpage footers but have no CSS rules. The nav has equivalent `.nav__lang-active` and `.nav__lang-link` which ARE styled -- the footer versions are likely intended to mirror those.

---

## 5. Impact Assessment

| Severity | Count | Description |
|----------|-------|-------------|
| **CRITICAL** | 114 | Classes with zero CSS rules -- elements render unstyled |
| **HIGH** | 4 | Naming mismatches in FAQ component (wrong selectors) |
| **MEDIUM** | 5 | Footer/breadcrumb classes missing but have nav equivalents to copy |
| **LOW** | 128 | CSS classes not used by subpages (homepage/utility classes) |

The most impactful missing component families are:
1. **contact__*** (22 classes) -- entire contact page form and info unstyled
2. **timeline-detail__*** (18 classes) -- entire process timeline unstyled
3. **timeline__*** (7 classes) -- why-suzhou timeline unstyled
4. **content-platform__*** (7 classes) -- about/community content cards unstyled
5. **profile-card__*** (8 classes) -- about page founder profile unstyled
6. **service-detail__*** (10 classes) -- services page detail cards unstyled
7. **benefit-card__*** (5 classes) -- feature cards in 3 pages unstyled
8. **comparison__*** (8 classes) -- comparison tables in 3 pages unstyled
