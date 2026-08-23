#!/usr/bin/env python3
"""Generate individual press detail pages for all media items."""

import os, shutil

# ── EN press items ──────────────────────────────────────────────
en_items = [
    {
        "slug": "moroccan-entrepreneur-suzhou",
        "title": "From Morocco to Suzhou: An Entrepreneur\u2019s Cross-Cultural Journey",
        "date": "August 23, 2026",
        "outlet": "\u6b64\u95f4\u521b (WeChat Channels)",
        "badge": "Video Interview",
        "image": "../assets/images/moroccan-entrepreneur-interview.png",
        "alt": "Founder Jessica Chang interviewing a Moroccan entrepreneur who moved to Suzhou to start a business",
        "summary": "Founder Jessica Chang interviews a Moroccan entrepreneur who stepped out of her comfort zone to start a business in Suzhou, exploring the collision and opportunities between Chinese and Moroccan business cultures.",
        "body": "<p>In this episode of \u6b64\u95f4\u521b, founder Jessica Chang sits down with a Moroccan entrepreneur who recently moved to Suzhou to start her own business. The conversation covers the cultural differences between Chinese and Moroccan business practices, the challenges of navigating a new regulatory environment, and the opportunities that Suzhou Industrial Park offers to international entrepreneurs.</p><p>The Moroccan entrepreneur shares her journey from first arriving in Suzhou with just an idea, to successfully registering her company with the help of Moon Bay OPC\u2019s full-service support. She discusses how the OPC (One Person Company) structure made it possible for her to launch independently, without needing a local partner or co-founder.</p><p>This cross-cultural dialogue highlights the growing trend of international entrepreneurs choosing Suzhou as their launchpad into the Chinese market, and the critical role that community support plays in their success.</p>",
        "external_url": "https://weixin.qq.com/sph/AkXkd91JH0",
        "external_label": "Watch on WeChat Channels",
        "featured_on_homepage": True,
    },
    {
        "slug": "enterprise-ai-transformation",
        "title": "Enterprise AI Transformation: Why the Boss Is Key",
        "date": "August 17, 2026",
        "outlet": "\u6b64\u95f4\u521b (WeChat Channels)",
        "badge": "Video Interview",
        "image": "../assets/images/mia-chang-hengtai-interview.jpg",
        "alt": "Founder Jessica Chang discussing enterprise AI transformation",
        "summary": "Founder Jessica Chang discusses why business owners are the critical factor in enterprise AI adoption \u2014 overcoming the fear of losing control by starting with hands-on experience.",
        "body": "<p>Founder Jessica Chang shares her insights on why enterprise AI transformation often stalls not because of technology, but because of leadership. She argues that the biggest barrier to AI adoption in traditional enterprises is the founder or CEO\u2019s fear of losing control.</p><p>Drawing from her own experience implementing AI tools across multiple business operations, Chang explains that the only way to overcome this fear is to start with hands-on experience. When business owners personally experiment with AI tools, they gain the confidence needed to lead their teams through digital transformation.</p><p>The conversation also touches on how AI is reshaping the entrepreneurial landscape in China, making it easier for solo founders to compete with larger organizations \u2014 and why OPC is the ideal company structure for the AI-powered entrepreneur.</p>",
        "external_url": "https://weixin.qq.com/sph/APe5dhPNV2",
        "external_label": "Watch on WeChat Channels",
        "featured_on_homepage": False,
    },
    {
        "slug": "sip-opc-community-video",
        "title": "Suzhou Industrial Park Features Moon Bay OPC Community",
        "date": "August 8, 2026",
        "outlet": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a (Official WeChat Channels)",
        "badge": "Official Government Video",
        "image": "../assets/images/sip-opc-video-rob-office.jpg",
        "alt": "Rob Moya at the Suzhou Industrial Park Overseas Talent OPC Community office",
        "summary": "The official Suzhou Industrial Park WeChat Channels account published a video showcasing the Overseas Talent OPC Community office and its first operational period (April\u2013August 2026).",
        "body": "<p>The official Suzhou Industrial Park WeChat Channels account featured the Moon Bay Overseas Talent OPC Community in a video showcase, highlighting the community\u2019s first operational period from April to August 2026. The video tours the community\u2019s display hub and workspace, demonstrating the premium environment available to international entrepreneurs.</p><p>This official recognition from SIP underscores the park\u2019s commitment to supporting foreign entrepreneurs through innovative programs like the OPC community. The video showcases the modern office facilities, collaborative spaces, and the supportive ecosystem that Moon Bay OPC provides to its members.</p><p>Since its launch, the community has served entrepreneurs from over 10 countries, helping them navigate the complexities of company registration, banking, and business operations in China.</p>",
        "external_url": "https://mp.weixin.qq.com/s/XounXneaBx5by04bTBezSQ",
        "external_label": "Watch on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "founder-philosophy-choosing-small",
        "title": "Founder\u2019s Philosophy: Why Choosing \u2018Small\u2019 Is the Smartest Long-Term Strategy",
        "date": "August 2026",
        "outlet": "\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a (Official WeChat)",
        "badge": "Featured Article",
        "image": "../assets/images/founder-philosophy-choosing-small.jpg",
        "alt": "Founder Jessica Chang on the philosophy of choosing small",
        "summary": "Founder Jessica Chang argues that deliberately choosing a lightweight business model is more sustainable than chasing scale for super-individual entrepreneurs.",
        "body": "<p>In a bold departure from conventional startup wisdom, founder Jessica Chang makes the case that \u201cchoosing small\u201d is not a limitation but a strategic advantage. Drawing on nearly 100 cases of overseas entrepreneurs in the Moon Bay OPC community, she argues that today\u2019s super-individual entrepreneurs should actively choose lightweight business structures over chasing scale.</p><p>Chang explains that the OPC structure is the ideal vehicle for this philosophy. It allows founders to validate their business model, establish operations, and generate revenue without the overhead and complexity of traditional company structures. The key insight: OPC is not a permanent state but a validation stage \u2014 a way to prove your business model before scaling.</p><p>The article also explores how AI tools are lowering the barrier to solo entrepreneurship, making it possible for one person to run a business that previously required a team of ten. The combination of OPC + AI creates a new paradigm for entrepreneurship that is more accessible, more sustainable, and ultimately more profitable.</p>",
        "external_url": "https://mp.weixin.qq.com/s/LJxwTHCC1Q_ButEXcc6TBw",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": True,
    },
    {
        "slug": "hengtai-zero-space-opc",
        "title": "Suzhou Hengtai Launches Zero-Space OPC Community at Dongyan Siji Apartments",
        "date": "July 28, 2026",
        "outlet": "\u82cf\u5dde\u6052\u6cf0\u96c6\u56e2 (WeChat Channels)",
        "badge": "WeChat Video",
        "image": "",
        "alt": "Suzhou Hengtai Zero-Space OPC Community opening",
        "summary": "Suzhou Hengtai Group officially opens the \u201cZero-Space OPC Community\u201d at Dongyan Siji Apartments \u2014 a new talent housing and OPC entrepreneur incubator.",
        "body": "<p>Suzhou Hengtai Group officially launched the \u201cZero-Space OPC Community\u201d at Dongyan Siji Apartments, marking a significant milestone in the integration of talent housing and entrepreneurial support. Founder Jessica Chang appears in the video being interviewed about the community\u2019s role in the OPC ecosystem.</p><p>The Zero-Space OPC Community is a innovative concept that provides entrepreneurs with both living space and working space in one integrated environment. This model reduces the cost and complexity of relocating to Suzhou, making it easier for international entrepreneurs to set up their operations quickly.</p><p>The partnership between Suzhou Hengtai and Moon Bay OPC represents a growing recognition that successful entrepreneurship requires more than just company registration \u2014 it needs a complete ecosystem of housing, office space, community support, and access to resources.</p>",
        "external_url": "https://weixin.qq.com/sph/Ah27dyShnD",
        "external_label": "Watch on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "opc-talent-apartment-signing",
        "title": "Founder Jessica Chang Interview: OPC Community Partners with SIP Talent Apartments",
        "date": "July 26, 2026",
        "outlet": "\u5f20\u5fd7\u7fa4 (WeChat Channels)",
        "badge": "WeChat Video",
        "image": "",
        "alt": "Jessica Chang interviewed at the signing ceremony",
        "summary": "Founder Jessica Chang is interviewed at the signing ceremony between the SIP Overseas Talent OPC Community and the park\u2019s talent apartments.",
        "body": "<p>Founder Jessica Chang was interviewed at the signing ceremony between the Suzhou Industrial Park Overseas Talent OPC Community and the park\u2019s talent apartments. This partnership provides world-class accommodation for returning overseas entrepreneurs, addressing one of the key challenges faced by international founders: finding quality housing in a new city.</p><p>The collaboration between the OPC community and SIP talent apartments represents a comprehensive approach to supporting international entrepreneurs. By combining company registration, office space, and now accommodation, Moon Bay OPC is building a truly end-to-end ecosystem for foreign founders.</p><p>Chang emphasizes that this partnership is about more than just housing \u2014 it\u2019s about creating a community where international entrepreneurs can live, work, and collaborate together, sharing experiences and supporting each other\u2019s growth.</p>",
        "external_url": "https://weixin.qq.com/sph/AE8FmmUgOw",
        "external_label": "Watch on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "signing-ceremony-coverage",
        "title": "OPC Community Signs Cooperation Agreement with SIP Talent Apartments",
        "date": "July 26, 2026",
        "outlet": "\u5f20\u5fd7\u7fa4 (WeChat Channels)",
        "badge": "WeChat Video",
        "image": "",
        "alt": "Signing ceremony coverage",
        "summary": "Coverage of the official signing ceremony between the Moon Bay Overseas Talent OPC Entrepreneurship Community and SIP talent apartments.",
        "body": "<p>Full coverage of the official signing ceremony between the Moon Bay Overseas Talent OPC Entrepreneurship Community and SIP talent apartments. The ceremony established a formal partnership to provide housing for overseas entrepreneurs, creating a seamless integration of entrepreneurial support and living accommodations.</p><p>The event was attended by representatives from multiple organizations, including the Suzhou Industrial Park management, talent apartment operators, and members of the OPC community. The partnership is expected to serve as a model for other innovation parks across China looking to attract and retain international entrepreneurial talent.</p><p>This signing ceremony represents a key milestone in Moon Bay OPC\u2019s mission to create a comprehensive support system for international entrepreneurs, covering everything from company registration to daily life needs.</p>",
        "external_url": "https://weixin.qq.com/sph/AoYrYT6Pw8",
        "external_label": "Watch on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "hengtai-zero-space-agreement",
        "title": "Moon Bay OPC Signs Cooperation Agreement at Hengtai Zero-Space Community Launch",
        "date": "July 25, 2026",
        "outlet": "\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a (Official WeChat)",
        "badge": "Featured Article",
        "image": "../assets/images/dpa-entrance.jpg",
        "alt": "Moon Bay OPC community entrance",
        "summary": "Founder Jessica Chang signs a symbiotic cooperation agreement with Hengtai Leasing and Qingchuanggang at the Zero-Space OPC Community opening ceremony.",
        "body": "<p>Founder Jessica Chang signed a symbiotic cooperation agreement with Hengtai Leasing and Qingchuanggang at the Zero-Space OPC Community opening ceremony. The agreement expands the community\u2019s service scenarios with shared event spaces, startup showcases, and talent housing for overseas entrepreneurs.</p><p>The three-party cooperation creates a unique ecosystem where entrepreneurs can access shared event spaces for networking and presentations, showcase their startups to potential investors and partners, and secure quality housing through the talent apartment program \u2014 all through a single community membership.</p><p>This integrated approach reflects Moon Bay OPC\u2019s philosophy that entrepreneurship support should be comprehensive and seamless. By partnering with leading real estate and innovation organizations, the community provides its members with resources that would be difficult for individual entrepreneurs to access on their own.</p>",
        "external_url": "https://mp.weixin.qq.com/s/uIEOTHA2O7X8d0piRodyjw",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "opc-entrepreneurship-philosophy",
        "title": "OPC Entrepreneurship Philosophy: From Product Mindset to Business Mindset",
        "date": "July 2026",
        "outlet": "\u6708\u4eae\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a (Official WeChat)",
        "badge": "Featured Article",
        "image": "../assets/images/opc-ruc-classmates-visit.jpg",
        "alt": "RUC classmates visiting Moon Bay OPC office",
        "summary": "Founder Jessica Chang explains how AI lowers development barriers but raises entrepreneurship barriers, and why OPC is a validation stage \u2014 not a permanent solo state.",
        "body": "<p>Founder Jessica Chang shares a nuanced perspective on the relationship between AI and entrepreneurship. While AI has dramatically lowered the technical barriers to building products, she argues that it has simultaneously raised the entrepreneurship bar. When anyone can build a product with AI, the real competitive advantage comes from business acumen, market understanding, and execution capability.</p><p>Chang explains that OPC should be viewed as a validation stage, not a permanent solo state. The community provides industry resources, mentors, partners, and policy support to help entrepreneurs transition from solo founder to team leader when the time is right. The key is to validate your business model and achieve product-market fit before scaling.</p><p>The article also discusses the importance of shifting from a product mindset (building features) to a business mindset (building value). For international entrepreneurs in China, this means understanding local market dynamics, regulatory requirements, and cultural nuances \u2014 areas where Moon Bay OPC provides critical support.</p>",
        "external_url": "https://mp.weixin.qq.com/s/wwwgP5_-auCb_a1-JSrrTQ",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "moon-bay-joins-dpa",
        "title": "Moon Bay OPC Joins Suzhou Industrial Park Development Promotion Association",
        "date": "July 2026",
        "outlet": "\u56ed\u533a\u8fdb\u5316\u8bba (WeChat)",
        "badge": "Featured Article",
        "image": "../assets/images/dpa-event-photo.jpg",
        "alt": "Moon Bay OPC community event at DPA",
        "summary": "Feature on Moon Bay OPC joining the SIP Development Promotion Association, highlighting founder Jessica Chang\u2019s 18 years of cross-cultural project management experience.",
        "body": "<p>Moon Bay OPC has been recognized as a member of the Suzhou Industrial Park Development Promotion Association (DPA), a significant milestone that validates the community\u2019s role in the park\u2019s entrepreneurial ecosystem. The feature highlights founder Jessica Chang\u2019s 18 years of cross-cultural project management experience and 8 years in global healthcare.</p><p>As a DPA member, Moon Bay OPC gains access to a broader network of industry partners, government resources, and policy insights that benefit its community members. The membership also positions Moon Bay OPC as a key stakeholder in the park\u2019s efforts to attract international entrepreneurial talent.</p><p>Chang\u2019s background in cross-cultural project management and global healthcare gives her unique insights into the challenges faced by international entrepreneurs in China. Her deep understanding of both Chinese and Western business cultures enables Moon Bay OPC to provide more effective support to its diverse community of founders.</p>",
        "external_url": "https://mp.weixin.qq.com/s/uhWDEFIVGnqsOyx4vMMPCQ",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": True,
    },
    {
        "slug": "mia-opc-license",
        "title": "First-Day Registration: Morocco Entrepreneur Mia Receives OPC License in Record Time",
        "date": "July 2026",
        "outlet": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u4e00\u7ad9\u5f0f\u670d\u52a1\u5927\u5385 (WeChat)",
        "badge": "Featured Article",
        "image": "../assets/images/mia-entrepreneur-holding-license.webp",
        "alt": "Mia holding her Chinese business license",
        "summary": "Mia, an entrepreneur from Morocco, applied for her foreigner OPC business license and had it approved the very next day.",
        "body": "<p>Moon Bay OPC\u2019s world-class service delivers again: Mia, an entrepreneur from Morocco, applied for her foreigner OPC business license and had it approved the very next day. This remarkable turnaround time demonstrates the efficiency of the community\u2019s full-process support for international founders.</p><p>The quick approval was made possible by Moon Bay OPC\u2019s deep expertise in the registration process, strong relationships with government service centers, and meticulous preparation of all required documentation. From the initial consultation to the final submission, every step was carefully managed to ensure a smooth and fast process.</p><p>Mia\u2019s story is just one example of how Moon Bay OPC is helping international entrepreneurs turn their China dreams into reality. The community\u2019s end-to-end support covers everything from company name reservation to bank account opening, making the complex process of setting up a business in China accessible to founders from around the world.</p>",
        "external_url": "https://mp.weixin.qq.com/s/GUzPifvWmg16Jh3vomCXUg",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": True,
    },
    {
        "slug": "suzhou-news-first-foreigner-opc",
        "title": "Suzhou Industrial Park Issues First Foreigner OPC Business License",
        "date": "June 2026",
        "outlet": "\u5f15\u529b\u64ad / \u82cf\u5dde\u65b0\u95fb (Suzhou News)",
        "badge": "News Coverage",
        "image": "../assets/images/suzhou-news-article-cover.jpg",
        "alt": "Suzhou News coverage of first foreigner OPC license",
        "summary": "Suzhou News covers the milestone of Rob Moya receiving the first foreigner OPC business license in SIP.",
        "body": "<p>Suzhou News (via \u5f15\u529b\u64ad) reported on the historic milestone of Rob Moya (Moya Sancho Jose Roberto) receiving the first foreigner OPC business license in Suzhou Industrial Park. The coverage highlights the park\u2019s commitment to attracting international entrepreneurial talent and its innovative approach to business registration.</p><p>The article notes that this milestone represents a significant step forward in SIP\u2019s efforts to create a globally competitive business environment. By enabling foreign entrepreneurs to register as OPCs, the park is removing a key barrier to entry and positioning itself as a leading destination for international startups.</p><p>Rob Moya\u2019s successful registration was facilitated by Moon Bay OPC\u2019s end-to-end support services, demonstrating the effectiveness of the community\u2019s approach to helping international entrepreneurs navigate China\u2019s business registration process.</p>",
        "external_url": "https://mp.weixin.qq.com/s/D567fNyB5U1c2dthL88Yuw",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": False,
    },
    {
        "slug": "first-foreigner-opc-license",
        "title": "Park Issues First Foreigner OPC Business License",
        "date": "May 2026",
        "outlet": "SIP Science & Technology Innovation Commission (SIP\u79d1\u6280\u521b\u65b0)",
        "badge": "Official Government Publication",
        "image": "../assets/photos/rob-jessica-license-sip-service-center.jpeg",
        "alt": "Rob Moya receiving his OPC business license with Jessica Chang",
        "summary": "Foreign entrepreneur Rob Moya successfully completed all registration procedures with the help of the Moon Bay OPC Entrepreneurship Community, obtaining the first foreigner OPC business license in SIP.",
        "body": "<p>In a landmark achievement for Suzhou Industrial Park, the SIP Science & Technology Innovation Commission published the official announcement of the first foreigner OPC business license issuance. Foreign entrepreneur Rob Moya (Moya Sancho Jose Roberto) successfully completed all registration procedures with the help of the Moon Bay OPC Entrepreneurship Community.</p><p>This milestone represents a key step in the park\u2019s global aggregation of innovative talent. The OPC (One Person Company) structure, introduced as part of China\u2019s Company Law reforms, allows solo founders to establish limited liability companies without the need for a local partner or co-founder \u2014 a significant simplification for international entrepreneurs.</p><p>The official government publication underscores SIP\u2019s commitment to creating an entrepreneur-friendly environment and its recognition of the important role that international founders play in driving innovation and economic growth.</p>",
        "external_url": "https://mp.weixin.qq.com/s/gIVqPiId-cSUV_bXJNepWg",
        "external_label": "Read Article on WeChat",
        "featured_on_homepage": True,
    },
    {
        "slug": "china-vs-us-ai-documentary",
        "title": "China vs US AI Large Models: A Costa Rican Entrepreneur\u2019s Perspective",
        "date": "May 2, 2026",
        "outlet": "\u6b64\u95f4\u521b (WeChat Channels \u2014 Documentary)",
        "badge": "Documentary",
        "image": "../assets/images/sip-sci-tech-article-cover.jpg",
        "alt": "SIP Science and Technology Innovation coverage",
        "summary": "Rob Moya shares his firsthand experience comparing Chinese and American AI large language models, discussing his one-person company model and journey as a foreign founder in Suzhou.",
        "body": "<p>In this documentary episode of \u6b64\u95f4\u521b, Costa Rican entrepreneur Rob Moya shares his firsthand experience comparing Chinese and American AI large language models. He discusses his one-person company model and his journey as a foreign founder in Suzhou, offering unique insights into the differences between the two major AI ecosystems.</p><p>Rob\u2019s perspective is particularly valuable because he has experience building AI-powered products in both markets. He compares the development ecosystems, access to APIs, pricing models, and the quality of AI models available in China versus the United States, providing practical insights for other international entrepreneurs considering building AI businesses in China.</p><p>The documentary also explores Rob\u2019s experience of building a company entirely on his own using the OPC structure, demonstrating how AI tools and the OPC model can combine to enable a new generation of solo entrepreneurs to compete effectively in the global market.</p>",
        "external_url": "https://weixin.qq.com/sph/AahddTKwrO",
        "external_label": "Watch on WeChat Channels",
        "featured_on_homepage": True,
    },
]

# ── ZH press items ──────────────────────────────────────────────
zh_items = [
    {
        "slug": "moroccan-entrepreneur-suzhou",
        "title": "\u8df3\u51fa\u8212\u9002\u533a\u8fdc\u8d74\u4e2d\u56fd\uff0c\u6469\u6d1b\u54e5\u5973\u5b69\u843d\u6237\u82cf\u5dde\u521b\u4e1a",
        "date": "2026\u5e748\u670823\u65e5",
        "outlet": "\u6b64\u95f4\u521b\uff08\u5fae\u4fe1\u89c6\u9891\u53f7\uff09",
        "badge": "\u89c6\u9891\u91c7\u8bbf",
        "image": "../assets/images/moroccan-entrepreneur-interview.png",
        "alt": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u91c7\u8bbf\u4e00\u4f4d\u4ece\u6469\u6d1b\u54e5\u6765\u5230\u82cf\u5dde\u521b\u4e1a\u7684\u5973\u5b69",
        "summary": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u91c7\u8bbf\u4e00\u4f4d\u4ece\u6469\u6d1b\u54e5\u6765\u5230\u82cf\u5dde\u521b\u4e1a\u7684\u5973\u5b69\uff0c\u8bb2\u8ff0\u4e24\u56fd\u5546\u4e1a\u6587\u5316\u7684\u78b0\u649e\u4e0e\u673a\u9047\u3002",
        "body": "<p>\u5728\u672c\u671f\u6b64\u95f4\u521b\u8282\u76ee\u4e2d\uff0c\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u4e0e\u4e00\u4f4d\u65b0\u8fd1\u6765\u5230\u82cf\u5dde\u521b\u4e1a\u7684\u6469\u6d1b\u54e5\u521b\u4e1a\u8005\u5ea7\u8c08\u3002\u5bf9\u8bdd\u6db5\u76d6\u4e2d\u6469\u4e24\u56fd\u5546\u4e1a\u6587\u5316\u7684\u5dee\u5f02\u3001\u9002\u5e94\u65b0\u76d1\u7ba1\u73af\u5883\u7684\u6311\u6218\uff0c\u4ee5\u53ca\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u4e3a\u56fd\u9645\u521b\u4e1a\u8005\u63d0\u4f9b\u7684\u673a\u9047\u3002</p><p>\u8fd9\u4f4d\u6469\u6d1b\u54e5\u521b\u4e1a\u8005\u5206\u4eab\u4e86\u5979\u4ece\u6000\u63e3\u60f3\u6cd5\u8e0f\u4e0a\u82cf\u5dde\uff0c\u5230\u5728\u6708\u5149\u6e7eOPC\u7684\u5168\u7a0b\u652f\u6301\u4e0b\u6210\u529f\u6ce8\u518c\u516c\u53f8\u7684\u7ecf\u5386\u3002\u5979\u8c08\u53caOPC\u7ed3\u6784\u5982\u4f55\u8ba9\u5979\u80fd\u591f\u72ec\u7acb\u521b\u4e1a\uff0c\u65e0\u9700\u5f53\u5730\u5408\u4f19\u4eba\u6216\u5171\u540c\u521b\u59cb\u4eba\u3002</p><p>\u8fd9\u573a\u8de8\u6587\u5316\u5bf9\u8bdd\u5c55\u793a\u4e86\u56fd\u9645\u521b\u4e1a\u8005\u9009\u62e9\u82cf\u5dde\u4f5c\u4e3a\u8fdb\u5165\u4e2d\u56fd\u5e02\u573a\u8df3\u677f\u7684\u65b0\u8d8b\u52bf\uff0c\u4ee5\u53ca\u793e\u533a\u652f\u6301\u5728\u4ed6\u4eec\u6210\u529f\u8fc7\u7a0b\u4e2d\u7684\u5173\u952e\u4f5c\u7528\u3002</p>",
        "external_url": "https://weixin.qq.com/sph/AkXkd91JH0",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": True,
    },
    {
        "slug": "enterprise-ai-transformation",
        "title": "\u4f01\u4e1aAI\u8f6c\u578b\uff1a\u8001\u677f\u662f\u5173\u952e\uff0c\u4ece\u4e0a\u624b\u611f\u5f00\u59cb\u514b\u670d\u5931\u63a7\u6050\u60e7",
        "date": "2026\u5e748\u670817\u65e5",
        "outlet": "\u6b64\u95f4\u521b\uff08\u5fae\u4fe1\u89c6\u9891\u53f7\uff09",
        "badge": "\u89c6\u9891\u91c7\u8bbf",
        "image": "../assets/images/mia-chang-hengtai-interview.jpg",
        "alt": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u63a2\u8ba8\u4f01\u4e1aAI\u8f6c\u578b",
        "summary": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u63a2\u8ba8\u4e3a\u4ec0\u4e48\u4f01\u4e1a\u8001\u677f\u662fAI\u8f6c\u578b\u7684\u5173\u952e\u56e0\u7d20\u3002",
        "body": "<p>\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u5206\u4eab\u5979\u5bf9\u4f01\u4e1aAI\u8f6c\u578b\u7684\u6df1\u523b\u89c1\u89e3\u3002\u5979\u8ba4\u4e3a\uff0c\u4f01\u4e1aAI\u8f6c\u578b\u5e38\u5e38\u505c\u6ede\u4e0d\u662f\u56e0\u4e3a\u6280\u672f\u95ee\u9898\uff0c\u800c\u662f\u56e0\u4e3a\u9886\u5bfc\u529b\u95ee\u9898\u3002\u4f01\u4e1a\u4e3b\u6216CEO\u5bf9\u5931\u53bb\u63a7\u5236\u7684\u6050\u60e7\u662f\u6700\u5927\u7684\u969c\u788d\u3002</p><p>\u5979\u8ba4\u4e3a\uff0c\u514b\u670d\u8fd9\u79cd\u6050\u60e7\u7684\u552f\u4e00\u65b9\u6cd5\u662f\u4ece\u4eb2\u624b\u5b9e\u9a8c\u5f00\u59cb\u3002\u5f53\u4f01\u4e1a\u4e3b\u4eb2\u81ea\u4f53\u9a8cAI\u5de5\u5177\u65f6\uff0c\u4ed6\u4eec\u5c06\u83b7\u5f97\u5e26\u9886\u56e2\u961f\u8fdb\u884c\u6570\u5b57\u5316\u8f6c\u578b\u7684\u81ea\u4fe1\u3002</p><p>\u5bf9\u8bdd\u8fd8\u63a2\u8ba8\u4e86AI\u5982\u4f55\u91cd\u5851\u4e2d\u56fd\u7684\u521b\u4e1a\u751f\u6001\uff0c\u4f7f\u5355\u4eba\u521b\u4e1a\u8005\u80fd\u591f\u4e0e\u5927\u578b\u7ec4\u7ec7\u7ade\u4e89\uff0c\u4ee5\u53ca\u4e3a\u4ec0\u4e48OPC\u662fAI\u65f6\u4ee3\u521b\u4e1a\u8005\u7684\u7406\u60f3\u516c\u53f8\u7ed3\u6784\u3002</p>",
        "external_url": "https://weixin.qq.com/sph/APe5dhPNV2",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": False,
    },
    {
        "slug": "sip-opc-community-video",
        "title": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u5b98\u65b9\u89c6\u9891\u53f7\u805a\u7126\u6708\u5149\u6e7eOPC\u521b\u4e1a\u793e\u533a",
        "date": "2026\u5e748\u67088\u65e5",
        "outlet": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\uff08\u5b98\u65b9\u89c6\u9891\u53f7\uff09",
        "badge": "\u5b98\u65b9\u653f\u5e9c\u89c6\u9891",
        "image": "../assets/images/sip-opc-video-rob-office.jpg",
        "alt": "Rob Moya\u5728\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u6d77\u5916\u4eba\u624dOPC\u793e\u533a\u529e\u516c\u5ba4",
        "summary": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u5b98\u65b9\u89c6\u9891\u53f7\u53d1\u5e03\u89c6\u9891\uff0c\u5c55\u793a\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u529e\u516c\u5ba4\u53ca\u5176\u9996\u4e2a\u8fd0\u8425\u671f\u3002",
        "body": "<p>\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u5b98\u65b9\u89c6\u9891\u53f7\u53d1\u5e03\u89c6\u9891\uff0c\u5c55\u793a\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u529e\u516c\u5ba4\u53ca\u5176\u9996\u4e2a\u8fd0\u8425\u671f\uff082026\u5e744\u6708\u81f38\u6708\uff09\u3002\u89c6\u9891\u53c2\u89c2\u4e86\u793e\u533a\u7684\u5c55\u793a\u4e2d\u5fc3\u548c\u5de5\u4f5c\u7a7a\u95f4\uff0c\u5c55\u793a\u4e86\u4e3a\u56fd\u9645\u521b\u4e1a\u8005\u63d0\u4f9b\u7684\u4f18\u8d28\u73af\u5883\u3002</p><p>\u8fd9\u4e00\u5b98\u65b9\u8ba4\u53ef\u5f3a\u8c03\u4e86\u56ed\u533a\u5bf9\u652f\u6301\u5916\u56fd\u521b\u4e1a\u8005\u7684\u627f\u8bfa\u3002\u89c6\u9891\u5c55\u793a\u4e86\u73b0\u4ee3\u5316\u529e\u516c\u8bbe\u65bd\u3001\u534f\u4f5c\u7a7a\u95f4\u4ee5\u53ca\u6708\u5149\u6e7eOPC\u4e3a\u5176\u6210\u5458\u63d0\u4f9b\u7684\u652f\u6301\u6027\u751f\u6001\u7cfb\u7edf\u3002</p><p>\u81ea\u542f\u52a8\u4ee5\u6765\uff0c\u793e\u533a\u5df2\u670d\u52a1\u6765\u81ea\u8d8510\u4e2a\u56fd\u5bb6\u7684\u521b\u4e1a\u8005\uff0c\u5e2e\u52a9\u4ed6\u4eec\u5e94\u5bf9\u516c\u53f8\u6ce8\u518c\u3001\u94f6\u884c\u5f00\u6237\u548c\u4e1a\u52a1\u8fd0\u8425\u7684\u5404\u79cd\u6311\u6218\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/XounXneaBx5by04bTBezSQ",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": False,
    },
    {
        "slug": "founder-philosophy-choosing-small",
        "title": "\u521b\u59cb\u4eba\u601d\u8003\uff1a\u523b\u610f\u505a\u5c0f\uff0c\u624d\u662f\u8d85\u7ea7\u4e2a\u4f53\u6700\u53ef\u6301\u7eed\u7684\u957f\u671f\u8def\u7ebf",
        "date": "2026\u5e748\u6708",
        "outlet": "\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\uff08\u5fae\u4fe1\u516c\u4f17\u53f7\uff09",
        "badge": "\u7cbe\u9009\u6587\u7ae0",
        "image": "../assets/images/founder-philosophy-choosing-small.jpg",
        "alt": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u9610\u8ff0\u523b\u610f\u505a\u5c0f\u7684\u7ecf\u8425\u54f2\u5b66",
        "summary": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u63d0\u51fa\uff0c\u8d85\u7ea7\u4e2a\u4f53\u521b\u4e1a\u8005\u5e94\u4e3b\u52a8\u9009\u62e9\u8f7b\u91cf\u5316\u5546\u4e1a\u67b6\u6784\uff0cOPC\u662f\u5b9e\u73b0\u201c\u5c0f\u800c\u5f3a\u201d\u5546\u4e1a\u6a21\u5f0f\u7684\u7406\u60f3\u8f7d\u4f53\u3002",
        "body": "<p>\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u7ed3\u5408\u6708\u5149\u6e7eOPC\u793e\u533a\u670d\u52a1\u8fd1\u767e\u4f4d\u6d77\u5916\u4eba\u624d\u7684\u5b9e\u8df5\u7ecf\u9a8c\uff0c\u63d0\u51fa\u4e0e\u4e3b\u6d41\u8ba4\u77e5\u76f8\u53cd\u7684\u5224\u65ad\uff1a\u5728\u5f53\u4e0b\u5546\u4e1a\u73af\u5883\u4e2d\uff0c\u8d85\u7ea7\u4e2a\u4f53\u521b\u4e1a\u8005\u5e94\u4e3b\u52a8\u9009\u62e9\u8f7b\u91cf\u5316\u5546\u4e1a\u67b6\u6784\uff0c\u800c\u975e\u76f2\u76ee\u8ffd\u9010\u89c4\u6a21\u3002</p><p>\u5e38\u6770\u96c5\u8ba4\u4e3aOPC\u7ed3\u6784\u662f\u5b9e\u73b0\u8fd9\u4e00\u54f2\u5b66\u7684\u7406\u60f3\u8f7d\u4f53\u3002\u5b83\u8ba9\u521b\u4e1a\u8005\u80fd\u591f\u9a8c\u8bc1\u5546\u4e1a\u6a21\u5f0f\u3001\u5efa\u7acb\u8fd0\u8425\u5e76\u4ea7\u751f\u6536\u5165\uff0c\u800c\u65e0\u9700\u4f20\u7edf\u516c\u53f8\u7ed3\u6784\u7684\u7e41\u91cd\u5f00\u652f\u3002\u6838\u5fc3\u89c1\u89e3\uff1aOPC\u4e0d\u662f\u6c38\u4e45\u72b6\u6001\uff0c\u800c\u662f\u4e00\u4e2a\u9a8c\u8bc1\u9636\u6bb5\u3002</p><p>\u6587\u7ae0\u8fd8\u63a2\u8ba8\u4e86AI\u5de5\u5177\u5982\u4f55\u964d\u4f4e\u5355\u4eba\u521b\u4e1a\u95e8\u69db\uff0c\u4f7f\u4e00\u4e2a\u4eba\u80fd\u8fd0\u8425\u4ee5\u524d\u9700\u8981\u56e2\u961f\u624d\u80fd\u5b8c\u6210\u7684\u4e8b\u4e1a\u3002OPC\u52a0AI\u7684\u7ec4\u5408\u521b\u9020\u4e86\u4e00\u79cd\u66f4\u53ef\u53ca\u3001\u66f4\u53ef\u6301\u7eed\u3001\u66f4\u6709\u76ca\u53ef\u56fe\u7684\u65b0\u521b\u4e1a\u8303\u5f0f\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/LJxwTHCC1Q_ButEXcc6TBw",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": True,
    },
    {
        "slug": "hengtai-zero-space-opc",
        "title": "\u82cf\u5dde\u6052\u6cf0\u00b7\u96f6\u65f6\u7a7aOPC\u793e\u533a\u5728\u4e1c\u5ef6\u56db\u5b63\u516c\u5bd3\u63ed\u724c\u542f\u7528",
        "date": "2026\u5e747\u670828\u65e5",
        "outlet": "\u82cf\u5dde\u6052\u6cf0\u96c6\u56e2\uff08\u5fae\u4fe1\u89c6\u9891\u53f7\uff09",
        "badge": "\u5fae\u4fe1\u89c6\u9891",
        "image": "",
        "alt": "\u82cf\u5dde\u6052\u6cf0\u96f6\u65f6\u7a7aOPC\u793e\u533a\u542f\u7528",
        "summary": "\u82cf\u5dde\u6052\u6cf0\u96c6\u56e2\u6b63\u5f0f\u542f\u7528\u201c\u96f6\u65f6\u7a7aOPC\u793e\u533a\u201d\uff0c\u5e38\u6770\u96c5\u5728\u89c6\u9891\u4e2d\u63a5\u53d7\u91c7\u8bbf\u3002",
        "body": "<p>\u82cf\u5dde\u6052\u6cf0\u96c6\u56e2\u6b63\u5f0f\u542f\u7528\u201c\u96f6\u65f6\u7a7aOPC\u793e\u533a\u201d\uff0c\u6807\u5fd7\u7740\u4eba\u624d\u5b89\u5c45\u4e0e\u521b\u4e1a\u652f\u6301\u7684\u91cd\u5927\u878d\u5408\u3002\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u5728\u89c6\u9891\u4e2d\u63a5\u53d7\u91c7\u8bbf\uff0c\u4ecb\u7ecd\u793e\u533a\u5728OPC\u751f\u6001\u7cfb\u7edf\u4e2d\u7684\u89d2\u8272\u3002</p><p>\u96f6\u65f6\u7a7aOPC\u793e\u533a\u662f\u4e00\u4e2a\u521b\u65b0\u6982\u5ff5\uff0c\u4e3a\u521b\u4e1a\u8005\u63d0\u4f9b\u751f\u6d3b\u7a7a\u95f4\u548c\u5de5\u4f5c\u7a7a\u95f4\u4e00\u4f53\u5316\u7684\u73af\u5883\u3002\u8fd9\u79cd\u6a21\u5f0f\u964d\u4f4e\u4e86\u642c\u8fc1\u82cf\u5dde\u7684\u6210\u672c\u548c\u590d\u6742\u6027\uff0c\u4f7f\u56fd\u9645\u521b\u4e1a\u8005\u80fd\u591f\u5feb\u901f\u5efa\u7acb\u8fd0\u8425\u3002</p><p>\u6052\u6cf0\u96c6\u56e2\u4e0e\u6708\u5149\u6e7eOPC\u7684\u5408\u4f5c\u4ee3\u8868\u4e86\u5bf9\u6210\u529f\u521b\u4e1a\u751f\u6001\u7684\u6df1\u523b\u7406\u89e3\u2014\u2014\u4e0d\u4ec5\u9700\u8981\u516c\u53f8\u6ce8\u518c\uff0c\u8fd8\u9700\u8981\u4f4f\u623f\u3001\u529e\u516c\u7a7a\u95f4\u3001\u793e\u533a\u652f\u6301\u548c\u8d44\u6e90\u5bf9\u63a5\u3002</p>",
        "external_url": "https://weixin.qq.com/sph/Ah27dyShnD",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": False,
    },
    {
        "slug": "opc-talent-apartment-signing",
        "title": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u91c7\u8bbf\uff1aOPC\u793e\u533a\u4e0e\u56ed\u533a\u4eba\u624d\u516c\u5bd3\u7b7e\u7ea6\u5408\u4f5c",
        "date": "2026\u5e747\u670826\u65e5",
        "outlet": "\u5f20\u5fd7\u7fa4\uff08\u5fae\u4fe1\u89c6\u9891\u53f7\uff09",
        "badge": "\u5fae\u4fe1\u89c6\u9891",
        "image": "",
        "alt": "\u5e38\u6770\u96c5\u5728\u7b7e\u7ea6\u4eea\u5f0f\u4e0a\u63a5\u53d7\u91c7\u8bbf",
        "summary": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u5728OPC\u793e\u533a\u4e0e\u56ed\u533a\u4eba\u624d\u516c\u5bd3\u7b7e\u7ea6\u4eea\u5f0f\u4e0a\u63a5\u53d7\u91c7\u8bbf\u3002",
        "body": "<p>\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u5728\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u6d77\u5916\u4eba\u624dOPC\u793e\u533a\u4e0e\u56ed\u533a\u4eba\u624d\u516c\u5bd3\u5408\u4f5c\u7b7e\u7ea6\u4eea\u5f0f\u4e0a\u63a5\u53d7\u91c7\u8bbf\u3002\u8fd9\u9879\u5408\u4f5c\u4e3a\u56de\u56fd\u521b\u4e1a\u7684\u6d77\u5916\u4eba\u624d\u63d0\u4f9b\u4e86\u4e00\u6d41\u7684\u4f4f\u5bbf\u6761\u4ef6\uff0c\u89e3\u51b3\u4e86\u56fd\u9645\u521b\u4e1a\u8005\u5728\u65b0\u57ce\u5e02\u5bfb\u627e\u4f18\u8d28\u4f4f\u623f\u7684\u5173\u952e\u96be\u9898\u3002</p><p>OPC\u793e\u533a\u4e0e\u4eba\u624d\u516c\u5bd3\u7684\u5408\u4f5c\u5c55\u73b0\u4e86\u652f\u6301\u56fd\u9645\u521b\u4e1a\u8005\u7684\u7efc\u5408\u65b9\u6cd5\u3002\u901a\u8fc7\u7ed3\u5408\u516c\u53f8\u6ce8\u518c\u3001\u529e\u516c\u7a7a\u95f4\u548c\u4f4f\u5bbf\u670d\u52a1\uff0c\u6708\u5149\u6e7eOPC\u6b63\u5728\u6784\u5efa\u771f\u6b63\u5168\u65b9\u4f4d\u7684\u56fd\u9645\u521b\u4e1a\u8005\u751f\u6001\u7cfb\u7edf\u3002</p><p>\u5e38\u6770\u96c5\u5f3a\u8c03\uff0c\u8fd9\u9879\u5408\u4f5c\u4e0d\u4ec5\u662f\u5173\u4e8e\u4f4f\u623f\uff0c\u66f4\u662f\u5173\u4e8e\u521b\u5efa\u4e00\u4e2a\u56fd\u9645\u521b\u4e1a\u8005\u53ef\u4ee5\u5171\u540c\u751f\u6d3b\u3001\u5de5\u4f5c\u548c\u5408\u4f5c\u7684\u793e\u533a\u3002</p>",
        "external_url": "https://weixin.qq.com/sph/AE8FmmUgOw",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": False,
    },
    {
        "slug": "signing-ceremony-coverage",
        "title": "\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u4e0e\u56ed\u533a\u4eba\u624d\u516c\u5bd3\u7b7e\u7ea6\u5408\u4f5c",
        "date": "2026\u5e747\u670826\u65e5",
        "outlet": "\u5f20\u5fd7\u7fa4\uff08\u5fae\u4fe1\u89c6\u9891\u53f7\uff09",
        "badge": "\u5fae\u4fe1\u89c6\u9891",
        "image": "",
        "alt": "\u7b7e\u7ea6\u4eea\u5f0f\u73b0\u573a",
        "summary": "\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u4e0e\u56ed\u533a\u4eba\u624d\u516c\u5bd3\u6b63\u5f0f\u7b7e\u7ea6\u5408\u4f5c\u3002",
        "body": "<p>\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u4e0e\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u4eba\u624d\u516c\u5bd3\u6b63\u5f0f\u4e3e\u884c\u7b7e\u7ea6\u5408\u4f5c\u4eea\u5f0f\uff0c\u4e3a\u6d77\u5916\u4eba\u624d\u63d0\u4f9b\u4e00\u6d41\u4f4f\u5bbf\u8bbe\u65bd\u548c\u914d\u5957\u670d\u52a1\u3002</p><p>\u6d3b\u52a8\u5f15\u8d77\u4e86\u591a\u4e2a\u673a\u6784\u7684\u5173\u6ce8\uff0c\u5305\u62ec\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u7ba1\u59d4\u4f1a\u3001\u4eba\u624d\u516c\u5bd3\u8fd0\u8425\u65b9\u4ee5\u53caOPC\u793e\u533a\u6210\u5458\u3002\u8fd9\u9879\u5408\u4f5c\u6709\u671b\u6210\u4e3a\u5168\u56fd\u5176\u4ed6\u521b\u65b0\u56ed\u533a\u5438\u5f15\u548c\u7559\u4f4f\u56fd\u9645\u521b\u4e1a\u4eba\u624d\u7684\u5148\u8fdb\u6a21\u5f0f\u3002</p><p>\u8fd9\u6b21\u7b7e\u7ea6\u4eea\u5f0f\u662f\u6708\u5149\u6e7eOPC\u6784\u5efa\u56fd\u9645\u521b\u4e1a\u8005\u7efc\u5408\u652f\u6301\u7cfb\u7edf\u7684\u91cd\u8981\u91cc\u7a0b\u7891\uff0c\u6db5\u76d6\u4ece\u516c\u53f8\u6ce8\u518c\u5230\u65e5\u5e38\u751f\u6d3b\u7684\u5404\u4e2a\u65b9\u9762\u3002</p>",
        "external_url": "https://weixin.qq.com/sph/AoYrYT6Pw8",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": False,
    },
    {
        "slug": "hengtai-zero-space-agreement",
        "title": "\u6708\u5149\u6e7eOPC\u793e\u533a\u51fa\u5e2d\u6052\u6cf0\u00b7\u96f6\u65f6\u7a7aOPC\u793e\u533a\u542f\u7528\u4eea\u5f0f\u5e76\u7b7e\u7f72\u5171\u751f\u5408\u4f5c\u534f\u8bae",
        "date": "2026\u5e747\u670825\u65e5",
        "outlet": "\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\uff08\u5fae\u4fe1\u516c\u4f17\u53f7\uff09",
        "badge": "\u7cbe\u9009\u6587\u7ae0",
        "image": "../assets/images/dpa-entrance.jpg",
        "alt": "\u6708\u5149\u6e7eOPC\u793e\u533a\u5927\u697c\u5165\u53e3",
        "summary": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u4ee3\u8868\u793e\u533a\u4e0e\u6052\u6cf0\u79df\u8d41\u4f4f\u623f\u3001\u9752\u521b\u6e2f\u4e09\u65b9\u5171\u540c\u7b7e\u7f72\u5171\u751f\u5408\u4f5c\u534f\u8bae\u3002",
        "body": "<p>\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u4ee3\u8868\u793e\u533a\u4e0e\u6052\u6cf0\u79df\u8d41\u4f4f\u623f\u3001\u9752\u521b\u6e2f\u4e09\u65b9\u5171\u540c\u7b7e\u7f72\u5171\u751f\u5408\u4f5c\u534f\u8bae\uff0c\u5c06\u5728\u7a7a\u95f4\u8d44\u6e90\u3001\u521b\u4e1a\u6d3b\u52a8\u3001\u4eba\u624d\u670d\u52a1\u7b49\u65b9\u9762\u5c55\u5f00\u5408\u4f5c\uff0c\u4e3a\u6d77\u5916\u4eba\u624d\u521b\u4e1a\u8005\u63d0\u4f9b\u66f4\u4e30\u5bcc\u7684\u8d44\u6e90\u94fe\u63a5\u4e0e\u53d1\u5c55\u7a7a\u95f4\u3002</p><p>\u4e09\u65b9\u5408\u4f5c\u521b\u9020\u4e86\u72ec\u7279\u7684\u751f\u6001\u7cfb\u7edf\uff0c\u521b\u4e1a\u8005\u53ef\u4ee5\u901a\u8fc7\u5355\u4e00\u793e\u533a\u4f1a\u5458\u8eab\u4efd\u83b7\u5f97\u5171\u4eab\u6d3b\u52a8\u7a7a\u95f4\u3001\u521b\u4e1a\u5c55\u793a\u673a\u4f1a\u548c\u4f18\u8d28\u4f4f\u5bbf\u3002</p><p>\u8fd9\u79cd\u96c6\u6210\u65b9\u6cd5\u53cd\u6620\u4e86\u6708\u5149\u6e7eOPC\u7684\u7406\u5ff5\uff1a\u521b\u4e1a\u652f\u6301\u5e94\u8be5\u5168\u9762\u800c\u65e0\u7f1d\u3002\u901a\u8fc7\u4e0e\u9886\u5148\u7684\u623f\u5730\u4ea7\u548c\u521b\u65b0\u7ec4\u7ec7\u5408\u4f5c\uff0c\u793e\u533a\u4e3a\u6210\u5458\u63d0\u4f9b\u4e86\u5355\u4e2a\u521b\u4e1a\u8005\u96be\u4ee5\u72ec\u81ea\u83b7\u5f97\u7684\u8d44\u6e90\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/uIEOTHA2O7X8d0piRodyjw",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": False,
    },
    {
        "slug": "opc-entrepreneurship-philosophy",
        "title": "OPC\u521b\u4e1a\u54f2\u5b66\uff1a\u4ece\u4ea7\u54c1\u601d\u7ef4\u5230\u5546\u4e1a\u601d\u7ef4",
        "date": "2026\u5e747\u6708",
        "outlet": "\u6708\u4eae\u6e7e\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\uff08\u5fae\u4fe1\u516c\u4f17\u53f7\uff09",
        "badge": "\u7cbe\u9009\u6587\u7ae0",
        "image": "../assets/images/opc-ruc-classmates-visit.jpg",
        "alt": "\u4eba\u5927\u4e1d\u8def\u5b66\u9662\u540c\u5b66\u53c2\u89c2\u6708\u5149\u6e7eOPC\u529e\u516c\u5ba4",
        "summary": "\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u9610\u8ff0AI\u964d\u4f4e\u4e86\u5f00\u53d1\u95e8\u69db\u5374\u63d0\u9ad8\u4e86\u521b\u4e1a\u95e8\u69db\uff0cOPC\u662f\u9a8c\u8bc1\u9636\u6bb5\u800c\u975e\u6c38\u4e45\u72ec\u884c\u72b6\u6001\u3002",
        "body": "<p>\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u5206\u4eab\u4e86\u5bf9AI\u4e0e\u521b\u4e1a\u5173\u7cfb\u7684\u6df1\u523b\u89c1\u89e3\u3002AI\u663e\u8457\u964d\u4f4e\u4e86\u5efa\u7acb\u4ea7\u54c1\u7684\u6280\u672f\u95e8\u69db\uff0c\u4f46\u540c\u65f6\u63d0\u9ad8\u4e86\u521b\u4e1a\u95e8\u69db\u3002\u5f53\u4efb\u4f55\u4eba\u90fd\u53ef\u4ee5\u7528AI\u6784\u5efa\u4ea7\u54c1\u65f6\uff0c\u771f\u6b63\u7684\u7ade\u4e89\u4f18\u52bf\u6765\u81ea\u5546\u4e1a\u667a\u6167\u3001\u5e02\u573a\u7406\u89e3\u548c\u6267\u884c\u529b\u3002</p><p>\u5e38\u6770\u96c5\u5f3a\u8c03OPC\u5e94\u89c6\u4e3a\u9a8c\u8bc1\u9636\u6bb5\uff0c\u800c\u975e\u6c38\u4e45\u72ec\u884c\u72b6\u6001\u3002\u793e\u533a\u63d0\u4f9b\u4ea7\u4e1a\u8d44\u6e90\u3001\u5bfc\u5e08\u3001\u5408\u4f5c\u4f19\u4f34\u548c\u653f\u7b56\u652f\u6301\uff0c\u5e2e\u52a9\u521b\u4e1a\u8005\u5728\u65f6\u673a\u6210\u719f\u65f6\u4ece\u5355\u4eba\u521b\u59cb\u4eba\u8f6c\u53d8\u4e3a\u56e2\u961f\u9886\u5bfc\u8005\u3002</p><p>\u6587\u7ae0\u8fd8\u8ba8\u8bba\u4e86\u4ece\u4ea7\u54c1\u601d\u7ef4\u8f6c\u53d8\u4e3a\u5546\u4e1a\u601d\u7ef4\u7684\u91cd\u8981\u6027\u3002\u5bf9\u4e8e\u5728\u4e2d\u56fd\u7684\u56fd\u9645\u521b\u4e1a\u8005\u800c\u8a00\uff0c\u8fd9\u610f\u5473\u7740\u7406\u89e3\u5f53\u5730\u5e02\u573a\u52a8\u6001\u3001\u76d1\u7ba1\u8981\u6c42\u548c\u6587\u5316\u5dee\u5f02\u2014\u2014\u8fd9\u6b63\u662f\u6708\u5149\u6e7eOPC\u63d0\u4f9b\u5173\u952e\u652f\u6301\u7684\u9886\u57df\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/wwwgP5_-auCb_a1-JSrrTQ",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": False,
    },
    {
        "slug": "moon-bay-joins-dpa",
        "title": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u6708\u4eae\u6e7e\u00b7\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u52a0\u5165\u82cf\u5dde\u5e02\u4ea7\u4e1a\u56ed\u533a\u53d1\u5c55\u4fc3\u8fdb\u4f1a",
        "date": "2026\u5e747\u6708",
        "outlet": "\u56ed\u533a\u8fdb\u5316\u8bba\uff08\u5fae\u4fe1\u516c\u4f17\u53f7\uff09",
        "badge": "\u7cbe\u9009\u6587\u7ae0",
        "image": "../assets/images/dpa-event-photo.jpg",
        "alt": "\u6708\u5149\u6e7eOPC\u52a0\u5165DPA\u6d3b\u52a8",
        "summary": "\u6708\u5149\u6e7eOPC\u52a0\u5165\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u53d1\u5c55\u4fc3\u8fdb\u4f1a\uff0c\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u5177\u670918\u5e74\u8de8\u6587\u5316\u9879\u76ee\u7ba1\u7406\u7ecf\u9a8c\u3002",
        "body": "<p>\u6708\u5149\u6e7eOPC\u6b63\u5f0f\u6210\u4e3a\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u53d1\u5c55\u4fc3\u8fdb\u4f1a\uff08DPA\uff09\u4f1a\u5458\u5355\u4f4d\uff0c\u8fd9\u662f\u793e\u533a\u53d1\u5c55\u5386\u7a0b\u4e2d\u7684\u91cd\u8981\u91cc\u7a0b\u7891\u3002\u62a5\u9053\u7a81\u51fa\u4ecb\u7ecd\u4e86\u521b\u59cb\u4eba\u5e38\u6770\u96c5\u768418\u5e74\u8de8\u6587\u5316\u9879\u76ee\u7ba1\u7406\u7ecf\u9a8c\u548c8\u5e74\u5168\u7403\u533b\u7597\u5065\u5eb7\u884c\u4e1a\u80cc\u666f\u3002</p><p>\u4f5c\u4e3aDPA\u4f1a\u5458\uff0c\u6708\u5149\u6e7eOPC\u5c06\u83b7\u5f97\u66f4\u5e7f\u9614\u7684\u4ea7\u4e1a\u5408\u4f5c\u4f19\u4f34\u7f51\u7edc\u3001\u653f\u5e9c\u8d44\u6e90\u548c\u653f\u7b56\u4fe1\u606f\uff0c\u8fd9\u4e9b\u90fd\u5c06\u76ca\u4e8e\u793e\u533a\u6210\u5458\u3002\u540c\u65f6\uff0c\u8fd9\u9879\u8ba4\u8bc1\u4e5f\u6807\u5fd7\u7740\u6708\u5149\u6e7eOPC\u6210\u4e3a\u56ed\u533a\u52aa\u529b\u5438\u5f15\u56fd\u9645\u521b\u4e1a\u4eba\u624d\u7684\u5173\u952e\u53c2\u4e0e\u8005\u3002</p><p>\u5e38\u6770\u96c5\u7684\u8de8\u6587\u5316\u80cc\u666f\u4f7f\u5979\u5bf9\u56fd\u9645\u521b\u4e1a\u8005\u5728\u4e2d\u56fd\u9762\u4e34\u7684\u6311\u6218\u62e5\u6709\u72ec\u7279\u89c1\u89e3\uff0c\u8fd9\u4f7f\u5f97\u6708\u5149\u6e7eOPC\u80fd\u591f\u4e3a\u5176\u591a\u5143\u5316\u7684\u521b\u4e1a\u8005\u793e\u7fa4\u63d0\u4f9b\u66f4\u6709\u6548\u7684\u652f\u6301\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/uhWDEFIVGnqsOyx4vMMPCQ",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": True,
    },
    {
        "slug": "mia-opc-license",
        "title": "\u4e00\u6d41\u4e13\u4e1a\u670d\u52a1\uff1a\u7b2c\u4e00\u5929\u7533\u8bf7\uff0c\u7b2c\u4e8c\u5929\u5373\u529e\u7ed3\u2014\u2014\u6469\u6d1b\u54e5\u521b\u4e1a\u8005\u7c73\u5a05\u83b7\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167",
        "date": "2026\u5e747\u6708",
        "outlet": "\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u4e00\u7ad9\u5f0f\u670d\u52a1\u5927\u5385\uff08\u5fae\u4fe1\u516c\u4f17\u53f7\uff09",
        "badge": "\u7cbe\u9009\u6587\u7ae0",
        "image": "../assets/images/mia-entrepreneur-holding-license.webp",
        "alt": "\u7c73\u5a05\u5c55\u793a\u5979\u7684\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167",
        "summary": "\u6469\u6d1b\u54e5\u521b\u4e1a\u8005\u7c73\u5a05\u7b2c\u4e00\u5929\u63d0\u4ea4\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u7533\u8bf7\uff0c\u7b2c\u4e8c\u5929\u5373\u987a\u5229\u529e\u7ed3\u3002",
        "body": "<p>\u6708\u5149\u6e7e\u6d77\u5916\u4eba\u624dOPC\u793e\u533a\u518d\u6b21\u5c55\u73b0\u9ad8\u6548\u670d\u52a1\uff1a\u6765\u81ea\u6469\u6d1b\u54e5\u7684\u521b\u4e1a\u8005\u7c73\u5a05\u7b2c\u4e00\u5929\u63d0\u4ea4\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u7533\u8bf7\uff0c\u7b2c\u4e8c\u5929\u5373\u987a\u5229\u529e\u7ed3\u3002\u8fd9\u4e2a\u60ca\u4eba\u7684\u5468\u8f6c\u65f6\u95f4\u5145\u5206\u8bc1\u660e\u4e86\u793e\u533a\u4e3a\u56fd\u9645\u521b\u59cb\u4eba\u63d0\u4f9b\u5168\u6d41\u7a0b\u652f\u6301\u7684\u9ad8\u6548\u6027\u3002</p><p>\u5feb\u901f\u5ba1\u6279\u5f97\u76ca\u4e8e\u6708\u5149\u6e7eOPC\u5bf9\u6ce8\u518c\u6d41\u7a0b\u7684\u6df1\u539a\u4e13\u4e1a\u77e5\u8bc6\u3001\u4e0e\u653f\u5e9c\u670d\u52a1\u4e2d\u5fc3\u7684\u826f\u597d\u5173\u7cfb\uff0c\u4ee5\u53ca\u5bf9\u6240\u6709\u5fc5\u8981\u6587\u4ef6\u7684\u7cbe\u5fc3\u51c6\u5907\u3002\u4ece\u521d\u6b65\u54a8\u8be2\u5230\u6700\u7ec8\u63d0\u4ea4\uff0c\u6bcf\u4e00\u6b65\u90fd\u7ecf\u8fc7\u4e25\u683c\u7ba1\u7406\u3002</p><p>\u7c73\u5a05\u7684\u6545\u4e8b\u4ec5\u4e3a\u6708\u5149\u6e7eOPC\u5e2e\u52a9\u56fd\u9645\u521b\u4e1a\u8005\u5b9e\u73b0\u4e2d\u56fd\u68a6\u7684\u4e00\u4e2a\u4f8b\u5b50\u3002\u793e\u533a\u7684\u5168\u6d41\u7a0b\u652f\u6301\u6db5\u76d6\u4ece\u516c\u53f8\u540d\u79f0\u9884\u7ea6\u5230\u94f6\u884c\u5f00\u6237\u7684\u5404\u4e2a\u73af\u8282\uff0c\u8ba9\u5728\u4e2d\u56fd\u521b\u4e1a\u7684\u590d\u6742\u6d41\u7a0b\u53d8\u5f97\u66f4\u52a0\u53ef\u53ca\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/GUzPifvWmg16Jh3vomCXUg",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": True,
    },
    {
        "slug": "suzhou-news-first-foreigner-opc",
        "title": "\u56ed\u533a\u53d1\u51fa\u9996\u5f20\u201c\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u201d",
        "date": "2026\u5e746\u6708",
        "outlet": "\u5f15\u529b\u64ad/\u82cf\u5dde\u65b0\u95fb",
        "badge": "\u65b0\u95fb\u62a5\u9053",
        "image": "../assets/images/suzhou-news-article-cover.jpg",
        "alt": "\u82cf\u5dde\u65b0\u95fb\u62a5\u9053\u9996\u5f20\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167",
        "summary": "\u82cf\u5dde\u65b0\u95fb\u62a5\u9053Rob Moya\u83b7\u5f97\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u9996\u5f20\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u3002",
        "body": "<p>\u82cf\u5dde\u65b0\u95fb\uff08\u901a\u8fc7\u5f15\u529b\u64ad\uff09\u62a5\u9053\u4e86Rob Moya\uff08Moya Sancho Jose Roberto\uff09\u83b7\u5f97\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u9996\u5f20\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u7684\u5386\u53f2\u6027\u91cc\u7a0b\u7891\u3002\u62a5\u9053\u7a81\u51fa\u5c55\u793a\u4e86\u56ed\u533a\u5438\u5f15\u56fd\u9645\u521b\u4e1a\u4eba\u624d\u7684\u51b3\u5fc3\u548c\u521b\u65b0\u65b9\u6cd5\u3002</p><p>\u6587\u7ae0\u6307\u51fa\uff0c\u8fd9\u4e00\u91cc\u7a0b\u7891\u4ee3\u8868\u4e86SIP\u5728\u521b\u9020\u5168\u7403\u7ade\u4e89\u529b\u5546\u4e1a\u73af\u5883\u65b9\u9762\u7684\u91cd\u5927\u8fdb\u6b65\u3002\u901a\u8fc7\u8ba9\u5916\u56fd\u521b\u4e1a\u8005\u80fd\u591f\u6ce8\u518c\u4e3aOPC\uff0c\u56ed\u533a\u6b63\u5728\u79fb\u9664\u5173\u952e\u95e8\u69db\uff0c\u5c06\u81ea\u5df1\u5b9a\u4f4d\u4e3a\u56fd\u9645\u521d\u521b\u4f01\u4e1a\u7684\u9886\u5148\u76ee\u7684\u5730\u3002</p><p>Rob Moya\u7684\u6210\u529f\u6ce8\u518c\u5f97\u76ca\u4e8e\u6708\u5149\u6e7eOPC\u7684\u5168\u6d41\u7a0b\u652f\u6301\u670d\u52a1\uff0c\u5c55\u793a\u4e86\u793e\u533a\u5e2e\u52a9\u56fd\u9645\u521b\u4e1a\u8005\u5e94\u5bf9\u4e2d\u56fd\u516c\u53f8\u6ce8\u518c\u6d41\u7a0b\u7684\u6709\u6548\u6027\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/D567fNyB5U1c2dthL88Yuw",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": False,
    },
    {
        "slug": "first-foreigner-opc-license",
        "title": "\u56ed\u533a\u53d1\u51fa\u9996\u5f20\u201c\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u201d",
        "date": "2026\u5e745\u6708",
        "outlet": "SIP\u79d1\u6280\u521b\u65b0\uff08\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u79d1\u6280\u521b\u65b0\u59d4\u5458\u4f1a\uff09",
        "badge": "\u5b98\u65b9\u653f\u5e9c\u53d1\u5e03",
        "image": "../assets/photos/rob-jessica-license-sip-service-center.jpeg",
        "alt": "Rob Moya\u5728\u4e00\u7ad9\u5f0f\u670d\u52a1\u5927\u5385\u9886\u53d6OPC\u8425\u4e1a\u6267\u7167",
        "summary": "\u5916\u56fd\u521b\u4e1a\u8005Rob Moya\u5728\u6708\u5149\u6e7eOPC\u793e\u533a\u5e2e\u52a9\u4e0b\u987a\u5229\u5b8c\u6210\u6ce8\u518c\u624b\u7eed\uff0c\u83b7\u5f97SIP\u9996\u5f20\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u3002",
        "body": "<p>\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u79d1\u6280\u521b\u65b0\u59d4\u5458\u4f1a\u6b63\u5f0f\u53d1\u5e03\u516c\u544a\uff0c\u5ba3\u5e03\u9996\u5f20\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u7684\u9881\u53d1\u3002\u5916\u56fd\u521b\u4e1a\u8005Moya Sancho Jose Roberto\uff08Rob Moya\uff09\u5728\u6708\u5149\u6e7e\u00b7\u6d77\u5916\u4eba\u624dOPC\u521b\u4e1a\u793e\u533a\u7684\u5168\u7a0b\u5e2e\u52a9\u4e0b\uff0c\u987a\u5229\u5b8c\u6210\u6240\u6709\u6ce8\u518c\u624b\u7eed\uff0c\u6210\u529f\u83b7\u5f97\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u9996\u5f20\u5916\u56fd\u4ebaOPC\u8425\u4e1a\u6267\u7167\u3002</p><p>\u8fd9\u4e00\u91cc\u7a0b\u7891\u4ee3\u8868\u4e86\u56ed\u533a\u5168\u7403\u805a\u96c6\u521b\u65b0\u4eba\u624d\u7684\u91cd\u8981\u4e00\u6b65\u3002OPC\u7ed3\u6784\u4f5c\u4e3a\u4e2d\u56fd\u516c\u53f8\u6cd5\u6539\u9769\u7684\u4e00\u90e8\u5206\uff0c\u5141\u8bb8\u5355\u4eba\u521b\u59cb\u4eba\u6210\u7acb\u6709\u9650\u8d23\u4efb\u516c\u53f8\uff0c\u65e0\u9700\u5f53\u5730\u5408\u4f19\u4eba\u6216\u5171\u540c\u521b\u59cb\u4eba\u2014\u2014\u8fd9\u5bf9\u56fd\u9645\u521b\u4e1a\u8005\u6765\u8bf4\u662f\u4e00\u4e2a\u91cd\u5927\u7b80\u5316\u3002</p><p>\u8fd9\u9879\u5b98\u65b9\u53d1\u5e03\u5f3a\u8c03\u4e86SIP\u521b\u9020\u521b\u4e1a\u53cb\u597d\u73af\u5883\u7684\u627f\u8bfa\uff0c\u4ee5\u53ca\u56fd\u9645\u521b\u59cb\u4eba\u5728\u63a8\u52a8\u521b\u65b0\u548c\u7ecf\u6d4e\u589e\u957f\u4e2d\u7684\u91cd\u8981\u4f5c\u7528\u3002</p>",
        "external_url": "https://mp.weixin.qq.com/s/gIVqPiId-cSUV_bXJNepWg",
        "external_label": "\u5728\u5fae\u4fe1\u9605\u8bfb",
        "featured_on_homepage": True,
    },
    {
        "slug": "china-vs-us-ai-documentary",
        "title": "\u4e2d\u7f8eAI\u5927\u6a21\u578b\u7684\u533a\u522b\u662f\u4ec0\u4e48\uff1f\u6765\u81ea\u54e5\u65af\u8fbe\u9ece\u52a0\u7684\u521b\u4e1a\u8005Rob\u8bb2\u8ff0\u4eb2\u8eab\u611f\u53d7",
        "date": "2026\u5e745\u67082\u65e5",
        "outlet": "\u6b64\u95f4\u521b\uff08\u5fae\u4fe1\u89c6\u9891\u53f7\u2014\u2014\u7eaa\u5f55\u7247\uff09",
        "badge": "\u7eaa\u5f55\u7247",
        "image": "../assets/images/sip-sci-tech-article-cover.jpg",
        "alt": "SIP\u79d1\u6280\u521b\u65b0\u62a5\u9053",
        "summary": "Rob Moya\u5206\u4eab\u4e2d\u7f8eAI\u5927\u8bed\u8a00\u6a21\u578b\u7684\u5bf9\u6bd4\u4f53\u9a8c\uff0c\u8bb2\u8ff0\u5728\u82cf\u5dde\u521b\u7acb\u4e00\u4eba\u516c\u53f8\u7684\u7ecf\u5386\u3002",
        "body": "<p>\u5728\u6b64\u95f4\u521b\u7eaa\u5f55\u7247\u8282\u76ee\u4e2d\uff0c\u54e5\u65af\u8fbe\u9ece\u52a0\u521b\u4e1a\u8005Rob Moya\u5206\u4eab\u4e86\u4ed6\u5bf9\u4e2d\u7f8eAI\u5927\u8bed\u8a00\u6a21\u578b\u7684\u7b2c\u4e00\u624b\u4f53\u9a8c\u3002\u4ed6\u8ba8\u8bba\u4e86\u4ed6\u7684\u4e00\u4eba\u516c\u53f8\u6a21\u5f0f\u4ee5\u53ca\u4f5c\u4e3a\u82cf\u5dde\u5916\u56fd\u521b\u59cb\u4eba\u7684\u7ecf\u5386\uff0c\u4e3a\u4e24\u5927AI\u751f\u6001\u7cfb\u7edf\u7684\u5dee\u5f02\u63d0\u4f9b\u4e86\u72ec\u7279\u89c1\u89e3\u3002</p><p>Rob\u7684\u89c6\u89d2\u5c24\u4e3a\u73cd\u8d35\uff0c\u56e0\u4e3a\u4ed6\u5728\u4e24\u4e2a\u5e02\u573a\u90fd\u6709\u6784\u5efaAI\u9a71\u52a8\u4ea7\u54c1\u7684\u7ecf\u9a8c\u3002\u4ed6\u6bd4\u8f83\u4e86\u4e2d\u56fd\u548c\u7f8e\u56fd\u7684\u5f00\u53d1\u751f\u6001\u3001API\u8bbf\u95ee\u3001\u4ef7\u683c\u6a21\u578b\u4ee5\u53caAI\u6a21\u578b\u7684\u8d28\u91cf\uff0c\u4e3a\u8003\u8651\u5728\u4e2d\u56fd\u6784\u5efaAI\u4e1a\u52a1\u7684\u56fd\u9645\u521b\u4e1a\u8005\u63d0\u4f9b\u4e86\u5b9e\u7528\u89c1\u89e3\u3002</p><p>\u7eaa\u5f55\u7247\u8fd8\u63a2\u8ba8\u4e86Rob\u5982\u4f55\u4f7f\u7528OPC\u7ed3\u6784\u5b8c\u5168\u72ec\u81ea\u521b\u5efa\u516c\u53f8\uff0c\u5c55\u793a\u4e86AI\u5de5\u5177\u548cOPC\u6a21\u5f0f\u5982\u4f55\u7ed3\u5408\uff0c\u4f7f\u65b0\u4e00\u4ee3\u5355\u4eba\u521b\u4e1a\u8005\u80fd\u591f\u5728\u5168\u7403\u5e02\u573a\u6709\u6548\u7ade\u4e89\u3002</p>",
        "external_url": "https://weixin.qq.com/sph/AahddTKwrO",
        "external_label": "\u5728\u5fae\u4fe1\u89c2\u770b",
        "featured_on_homepage": True,
    },
]


# ── Helper: NAV / FOOTER templates ──────────────────────────────

EN_HEADER = """  <header class="header" id="header">
    <div class="header-inner">
      <a href="../index.html" class="logo">Moon Bay <span>OPC</span></a>
            <nav class="nav-links" id="navLinks">
  <div class="mega-menu">
    <a href="../en/services.html" class="mega-menu-trigger">Services <svg class="mega-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></a>
    <div class="mega-menu-panel">
      <div class="mega-menu-container">
        <div class="mega-menu-grid mega-menu-grid--2">
          <a href="../en/services.html" class="mega-card">
            <img src="../assets/images/modern-office.jpg" alt="Our Services" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">Our Services</div>
              <div class="mega-card__desc">End-to-end OPC registration, office space, and ongoing business support</div>
            </div>
          </a>
          <a href="../en/process.html" class="mega-card">
            <img src="../assets/images/mia-license-process.webp" alt="The Process" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">The Process</div>
              <div class="mega-card__desc">Step-by-step guide to registering your OPC in 15\u201320 days</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="mega-menu">
    <a href="../en/why-suzhou.html" class="mega-menu-trigger">Why Suzhou <svg class="mega-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></a>
    <div class="mega-menu-panel">
      <div class="mega-menu-container">
        <div class="mega-menu-grid">
          <a href="../en/why-suzhou.html" class="mega-card">
            <img src="../assets/images/suzhou-hero-sip-aerial.jpg" alt="Why Suzhou" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">Why Suzhou</div>
              <div class="mega-card__desc">China's most innovative district for foreign entrepreneurs</div>
            </div>
          </a>
          <a href="../en/what-is-opc.html" class="mega-card">
            <img src="../assets/images/hero-opc-concept.jpg" alt="What is OPC" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">What is OPC</div>
              <div class="mega-card__desc">China's newest company structure for solo founders</div>
            </div>
          </a>
          <a href="../en/faq.html" class="mega-card">
            <img src="../assets/images/opc-story-want-to-open-company.jpg" alt="FAQ" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">FAQ</div>
              <div class="mega-card__desc">Answers to the most common questions about OPC registration</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="mega-menu">
    <a href="../en/resources.html" class="mega-menu-trigger">Resources <svg class="mega-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></a>
    <div class="mega-menu-panel">
      <div class="mega-menu-container">
        <div class="mega-menu-grid">
          <a href="../en/resources.html" class="mega-card">
            <img src="../assets/images/opc-ruc-classmates-visit.jpg" alt="Resources" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">Resources</div>
              <div class="mega-card__desc">Guides, templates, and policy summaries for OPC founders</div>
            </div>
          </a>
          <a href="../en/press.html" class="mega-card">
            <img src="../assets/images/sip-sci-tech-article-cover.jpg" alt="Press" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">Press & Media</div>
              <div class="mega-card__desc">Featured stories and media coverage</div>
            </div>
          </a>
          <a href="../en/community.html" class="mega-card">
            <img src="../assets/images/dpa-event-photo.jpg" alt="Community" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">Community</div>
              <div class="mega-card__desc">Join the network of international entrepreneurs in Suzhou</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <a href="../en/about.html">About</a>
  <a href="../en/contact.html" class="nav-cta">Contact</a>
</nav>
      <div class="header-right">
        <div class="lang-toggle">
          <a href="../index.html">EN</a>
          <span class="separator">|</span>
          <a href="../zh/press.html">\u4e2d</a>
        </div>
        <button class="hamburger" id="hamburger" aria-label="Toggle navigation" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
    <div class="mobile-nav" id="mobileNav">
      <a href="../en/services.html">Services</a>
      <a href="../en/process.html">Process</a>
      <a href="../en/why-suzhou.html">Why Suzhou</a>
      <a href="../en/what-is-opc.html">What is OPC</a>
      <a href="../en/faq.html">FAQ</a>
      <a href="../en/resources.html">Resources</a>
      <a href="../en/press.html">Press</a>
      <a href="../en/about.html">About</a>
      <a href="../en/community.html">Community</a>
      <a href="../en/contact.html">Contact</a>
      <a href="../zh/index.html">\u4e2d\u6587</a>
    </div>
  </header>"""

EN_FOOTER = """  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand footer-col">
          <div class="footer-logo">Moon Bay <span>OPC</span></div>
          <p class="footer-tagline">Your trusted partner for company registration and business support in Suzhou Industrial Park, China.</p>
          <div class="social-links">
            <a href="#" aria-label="WeChat" title="WeChat: changjieya (Miss Chang from OPC)">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 01.213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 00.167-.054l1.903-1.114a.864.864 0 01.717-.098 10.16 10.16 0 002.837.403c.276 0 .543-.027.811-.05a6.127 6.127 0 01-.259-1.795c0-3.8 3.503-6.874 7.82-6.874.279 0 .553.014.826.033C16.469 4.472 12.927 2.188 8.691 2.188zm-2.93 4.796a1.04 1.04 0 110 2.08 1.04 1.04 0 010-2.08zm5.832 0a1.04 1.04 0 110 2.08 1.04 1.04 0 010-2.08zM23.996 14.58c0-3.371-3.268-6.108-7.296-6.108-4.028 0-7.296 2.737-7.296 6.108 0 3.371 3.268 6.108 7.296 6.108.85 0 1.67-.117 2.443-.335a.72.72 0 01.596.082l1.563.912a.275.275 0 00.137.044c.132 0 .24-.109.24-.243 0-.059-.024-.117-.04-.175l-.319-1.214a.484.484 0 01.175-.546c1.548-1.125 2.501-2.79 2.501-4.633zm-9.744-1.158a.855.855 0 110 1.71.855.855 0 010-1.71zm4.897 0a.855.855 0 110 1.71.855.855 0 010-1.71z"/></svg>
            </a>
            <a href="https://www.youtube.com/@suzhouopc" aria-label="YouTube">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="../en/services.html">Company Registration</a></li>
            <li><a href="../en/services.html">Banking & Finance</a></li>
            <li><a href="../en/services.html">Visa & Immigration</a></li>
            <li><a href="../en/services.html">Legal & Compliance</a></li>
            <li><a href="../en/services.html">HR & Payroll</a></li>
            <li><a href="../en/services.html">Office Space</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="../en/about.html">About Us</a></li>
            <li><a href="../en/process.html">Our Process</a></li>
            <li><a href="../en/why-suzhou.html">Why Suzhou</a></li>
            <li><a href="../en/what-is-opc.html">What is OPC</a></li>
            <li><a href="../en/press.html">Press</a></li>
            <li><a href="../en/faq.html">FAQ</a></li>
          </ul>
        </div>
        <div class="footer-col footer-contact">
          <h4>Contact</h4>
        </div>
        <div class="footer-col footer-lang">
          <h4>Language</h4>
          <div class="lang-switch">
            <a href="../index.html">EN</a>
            <a href="../zh/press.html">\u4e2d\u6587</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Moon Bay OPC. All rights reserved. | Suzhou Industrial Park, China</p>
      </div>
    </div>
  </footer>"""

ZH_HEADER = """  <header class="header" id="header">
    <div class="header-inner">
      <a href="../index.html" class="logo">Moon Bay <span>OPC</span></a>
                        <nav class="nav-links" id="navLinks">
  <div class="mega-menu">
    <a href="services.html" class="mega-menu-trigger">\u670d\u52a1 <svg class="mega-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></a>
    <div class="mega-menu-panel">
      <div class="mega-menu-container">
        <div class="mega-menu-grid mega-menu-grid--2">
          <a href="services.html" class="mega-card">
            <img src="../assets/images/modern-office.jpg" alt="\u6211\u4eec\u7684\u670d\u52a1" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u6211\u4eec\u7684\u670d\u52a1</div>
              <div class="mega-card__desc">OPC\u6ce8\u518c\u3001\u529e\u516c\u7a7a\u95f4\u548c\u6301\u7eed\u4e1a\u52a1\u652f\u6301</div>
            </div>
          </a>
          <a href="process.html" class="mega-card">
            <img src="../assets/images/mia-license-process.webp" alt="\u529e\u7406\u6d41\u7a0b" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u529e\u7406\u6d41\u7a0b</div>
              <div class="mega-card__desc">15\u201320\u5929\u5b8c\u6210OPC\u6ce8\u518c\u7684\u9010\u6b65\u6307\u5357</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="mega-menu">
    <a href="why-suzhou.html" class="mega-menu-trigger">\u4e3a\u4ec0\u4e48\u9009\u62e9\u82cf\u5dde <svg class="mega-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></a>
    <div class="mega-menu-panel">
      <div class="mega-menu-container">
        <div class="mega-menu-grid">
          <a href="why-suzhou.html" class="mega-card">
            <img src="../assets/images/suzhou-hero-sip-aerial.jpg" alt="\u4e3a\u4ec0\u4e48\u9009\u62e9\u82cf\u5dde" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u4e3a\u4ec0\u4e48\u9009\u62e9\u82cf\u5dde</div>
              <div class="mega-card__desc">\u4e2d\u56fd\u6700\u9002\u5408\u5916\u56fd\u521b\u4e1a\u8005\u7684\u521b\u65b0\u56ed\u533a</div>
            </div>
          </a>
          <a href="what-is-opc.html" class="mega-card">
            <img src="../assets/images/hero-opc-concept.jpg" alt="\u4ec0\u4e48\u662fOPC" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u4ec0\u4e48\u662fOPC</div>
              <div class="mega-card__desc">\u4e2d\u56fd\u6700\u65b0\u7684\u5355\u4eba\u516c\u53f8\u7ed3\u6784</div>
            </div>
          </a>
          <a href="faq.html" class="mega-card">
            <img src="../assets/images/opc-story-want-to-open-company.jpg" alt="\u5e38\u89c1\u95ee\u9898" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u5e38\u89c1\u95ee\u9898</div>
              <div class="mega-card__desc">\u5173\u4e8eOPC\u6ce8\u518c\u6700\u5e38\u89c1\u95ee\u9898\u7684\u89e3\u7b54</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <div class="mega-menu">
    <a href="resources.html" class="mega-menu-trigger">\u8d44\u6e90\u4e2d\u5fc3 <svg class="mega-chevron" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></a>
    <div class="mega-menu-panel">
      <div class="mega-menu-container">
        <div class="mega-menu-grid">
          <a href="resources.html" class="mega-card">
            <img src="../assets/images/opc-ruc-classmates-visit.jpg" alt="\u8d44\u6e90\u4e2d\u5fc3" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u8d44\u6e90\u4e2d\u5fc3</div>
              <div class="mega-card__desc">OPC\u521b\u4e1a\u8005\u7684\u6307\u5357\u3001\u6a21\u677f\u548c\u653f\u7b56\u6458\u8981</div>
            </div>
          </a>
          <a href="press.html" class="mega-card">
            <img src="../assets/images/sip-sci-tech-article-cover.jpg" alt="\u5a92\u4f53\u62a5\u9053" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u5a92\u4f53\u62a5\u9053</div>
              <div class="mega-card__desc">\u4e13\u9898\u62a5\u9053\u548c\u5a92\u4f53\u91c7\u8bbf</div>
            </div>
          </a>
          <a href="community.html" class="mega-card">
            <img src="../assets/images/dpa-event-photo.jpg" alt="\u793e\u533a" class="mega-card__image" loading="lazy">
            <div class="mega-card__content">
              <div class="mega-card__title">\u793e\u533a</div>
              <div class="mega-card__desc">\u52a0\u5165\u82cf\u5dde\u56fd\u9645\u521b\u4e1a\u8005\u7f51\u7edc</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
  <a href="about.html">\u5173\u4e8e\u6211\u4eec</a>
  <a href="contact.html" class="nav-cta">\u8054\u7cfb\u6211\u4eec</a>
</nav>
      <div class="header-right">
        <div class="lang-toggle">
          <a href="../index.html">EN</a>
          <span class="separator">|</span>
          <a href="press.html">\u4e2d</a>
        </div>
        <button class="hamburger" id="hamburger" aria-label="\u5207\u6362\u5bfc\u822a" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
    <div class="mobile-nav" id="mobileNav">
      <a href="services.html">\u670d\u52a1</a>
      <a href="process.html">\u6d41\u7a0b</a>
      <a href="why-suzhou.html">\u4e3a\u4ec0\u4e48\u9009\u62e9\u82cf\u5dde</a>
      <a href="what-is-opc.html">\u4ec0\u4e48\u662fOPC</a>
      <a href="faq.html">\u5e38\u89c1\u95ee\u9898</a>
      <a href="resources.html">\u8d44\u6e90\u4e2d\u5fc3</a>
      <a href="press.html">\u5a92\u4f53\u62a5\u9053</a>
      <a href="about.html">\u5173\u4e8e\u6211\u4eec</a>
      <a href="community.html">\u793e\u533a</a>
      <a href="contact.html">\u8054\u7cfb\u6211\u4eec</a>
      <a href="../index.html">English</a>
    </div>
  </header>"""

ZH_FOOTER = """  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand footer-col">
          <div class="footer-logo">Moon Bay <span>OPC</span></div>
          <p class="footer-tagline">\u60a8\u503c\u5f97\u4fe1\u8d56\u7684\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a\u516c\u53f8\u6ce8\u518c\u4e0e\u5546\u4e1a\u670d\u52a1\u5408\u4f5c\u4f19\u4f34\u3002</p>
          <div class="social-links">
            <a href="#" aria-label="WeChat">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 01.213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 00.167-.054l1.903-1.114a.864.864 0 01.717-.098 10.16 10.16 0 002.837.403c.276 0 .543-.027.811-.05a6.127 6.127 0 01-.259-1.795c0-3.8 3.503-6.874 7.82-6.874.279 0 .553.014.826.033C16.469 4.472 12.927 2.188 8.691 2.188zm-2.93 4.796a1.04 1.04 0 110 2.08 1.04 1.04 0 010-2.08zm5.832 0a1.04 1.04 0 110 2.08 1.04 1.04 0 010-2.08zM23.996 14.58c0-3.371-3.268-6.108-7.296-6.108-4.028 0-7.296 2.737-7.296 6.108 0 3.371 3.268 6.108 7.296 6.108.85 0 1.67-.117 2.443-.335a.72.72 0 01.596.082l1.563.912a.275.275 0 00.137.044c.132 0 .24-.109.24-.243 0-.059-.024-.117-.04-.175l-.319-1.214a.484.484 0 01.175-.546c1.548-1.125 2.501-2.79 2.501-4.633zm-9.744-1.158a.855.855 0 110 1.71.855.855 0 010-1.71zm4.897 0a.855.855 0 110 1.71.855.855 0 010-1.71z"/></svg>
            </a>
            <a href="https://www.youtube.com/@suzhouopc" aria-label="YouTube" target="_blank" rel="noopener">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <h4>\u670d\u52a1</h4>
          <ul>
            <li><a href="services.html">\u516c\u53f8\u6ce8\u518c</a></li>
            <li><a href="services.html">\u94f6\u884c\u4e0e\u8d22\u52a1</a></li>
            <li><a href="services.html">\u7b7e\u8bc1\u4e0e\u79fb\u6c11</a></li>
            <li><a href="services.html">\u6cd5\u5f8b\u4e0e\u5408\u89c4</a></li>
            <li><a href="services.html">\u4eba\u529b\u8d44\u6e90\u4e0e\u85aa\u916c</a></li>
            <li><a href="services.html">\u529e\u516c\u7a7a\u95f4</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>\u516c\u53f8</h4>
          <ul>
            <li><a href="about.html">\u5173\u4e8e\u6211\u4eec</a></li>
            <li><a href="process.html">\u670d\u52a1\u6d41\u7a0b</a></li>
            <li><a href="why-suzhou.html">\u4e3a\u4ec0\u4e48\u9009\u62e9\u82cf\u5dde</a></li>
            <li><a href="what-is-opc.html">\u4ec0\u4e48\u662fOPC</a></li>
            <li><a href="press.html">\u5a92\u4f53\u62a5\u9053</a></li>
            <li><a href="faq.html">\u5e38\u89c1\u95ee\u9898</a></li>
          </ul>
        </div>
        <div class="footer-col footer-contact">
          <h4>\u8054\u7cfb\u6211\u4eec</h4>
        </div>
        <div class="footer-col footer-lang">
          <h4>\u8bed\u8a00</h4>
          <div class="lang-switch">
            <a href="../index.html">EN</a>
            <a href="press.html">\u4e2d\u6587</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 \u6708\u5149\u6e7eOPC. \u4fdd\u7559\u6240\u6709\u6743\u5229\u3002| \u4e2d\u56fd\u82cf\u5dde\u5de5\u4e1a\u56ed\u533a</p>
      </div>
    </div>
  </footer>"""


# ── Generate all pages ──────────────────────────────────────────

def generate_page(item, lang, items, header, footer, is_zh):
    """Generate a single press detail HTML page."""
    press_page = "../en/press.html" if lang == "en" else "../zh/press.html"

    img_html = ""
    if item.get("image"):
        img_html = f'''<div class="press-detail__image">
          <img src="{item["image"]}" alt="{item["alt"]}" loading="lazy">
        </div>'''

    # Navigation
    idx = items.index(item)
    prev_item = items[idx - 1] if idx > 0 else None
    next_item = items[idx + 1] if idx < len(items) - 1 else None

    nav_html = ""
    if prev_item or next_item:
        nav_html = '<div class="press-detail__nav">'
        if prev_item:
            prev_label = "\u4e0a\u4e00\u7bc7" if is_zh else "Previous"
            nav_html += f'''<a href="{prev_item["slug"]}.html" class="press-detail__nav-prev">
            <span class="press-detail__nav-label">{prev_label}</span>
            <span class="press-detail__nav-title">{prev_item["title"]}</span>
          </a>'''
        else:
            nav_html += '<div></div>'
        if next_item:
            next_label = "\u4e0b\u4e00\u7bc7" if is_zh else "Next"
            nav_html += f'''<a href="{next_item["slug"]}.html" class="press-detail__nav-next">
            <span class="press-detail__nav-label">{next_label}</span>
            <span class="press-detail__nav-title">{next_item["title"]}</span>
          </a>'''
        nav_html += '</div>'

    back_label = "\u2190 \u8fd4\u56de\u5a92\u4f53\u62a5\u9053" if is_zh else "\u2190 Back to Press"

    external_icon = '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>'

    site_name = "\u6708\u5149\u6e7eOPC" if is_zh else "Moon Bay OPC"
    emdash = "\u2014"
    lang_attr = "zh-CN" if is_zh else "en"
    hero_title = "Press & Media" if not is_zh else "\u5a92\u4f53\u62a5\u9053"

    page = f'''<!-- Generated by Trae Work -->
<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{item["summary"]}">
  <title>{item["title"]} {emdash} {site_name}</title>

  <link rel="canonical" href="https://moonbayopc.netlify.app/{lang}/press/{item["slug"]}.html">
  <meta property="og:title" content="{item["title"]}">
  <meta property="og:description" content="{item["summary"]}">
  <meta property="og:url" content="https://moonbayopc.netlify.app/{lang}/press/{item["slug"]}.html">
  {f'<meta property="og:image" content="https://moonbayopc.netlify.app/{item["image"].lstrip("../")}">' if item.get("image") else ''}
  <link rel="alternate" hreflang="en" href="https://moonbayopc.netlify.app/en/press/{item["slug"]}.html">
  <link rel="alternate" hreflang="zh" href="https://moonbayopc.netlify.app/zh/press/{item["slug"]}.html">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

{header}

  <section class="page-hero">
    <div class="container">
      <h1 class="page-hero__title">{hero_title}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="press-detail">
        <a href="{press_page}" class="press-detail__back">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
          {back_label}
        </a>

        <span class="press-detail__badge">{item["badge"]}</span>

        <h1>{item["title"]}</h1>
        <p class="press-detail__date">{item["date"]} &middot; {item["outlet"]}</p>

        {img_html}

        <div class="press-detail__summary">
          <p>{item["summary"]}</p>
        </div>

        <div class="press-detail__body">
          {item["body"]}
        </div>

        <div class="press-detail__actions">
          <a href="{item["external_url"]}" class="btn btn-primary" target="_blank" rel="noopener">
            {external_icon}
            {item["external_label"]}
          </a>
        </div>

        {nav_html}

      </div>
    </div>
  </section>

{footer}

  <script src="../js/main.js"></script>
</body>
</html>'''

    return page


# ── Main execution ─────────────────────────────────────────────────

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))

    # Generate EN pages
    en_dir = os.path.join(base, "en", "press")
    os.makedirs(en_dir, exist_ok=True)
    for item in en_items:
        page = generate_page(item, "en", en_items, EN_HEADER, EN_FOOTER, False)
        path = os.path.join(en_dir, f"{item['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  [EN] {item['slug']}.html")

    # Generate ZH pages
    zh_dir = os.path.join(base, "zh", "press")
    os.makedirs(zh_dir, exist_ok=True)
    for item in zh_items:
        page = generate_page(item, "zh", zh_items, ZH_HEADER, ZH_FOOTER, True)
        path = os.path.join(zh_dir, f"{item['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  [ZH] {item['slug']}.html")

    print(f"\nDone! Generated {len(en_items)} EN + {len(zh_items)} ZH = {len(en_items) + len(zh_items)} press detail pages.")