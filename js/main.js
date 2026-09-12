/* ============================================================
   Moon Bay OPC — Main JavaScript
   Mobile nav toggle, scroll-reveal animations, smooth scroll
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     Mobile Navigation Toggle
     ---------------------------------------------------------- */
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', function () {
      const isOpen = hamburger.classList.toggle('active');
      mobileNav.classList.toggle('active');
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile nav when a link is clicked
    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        mobileNav.classList.remove('active');
        document.body.style.overflow = '';
      });
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        hamburger.classList.remove('active');
        mobileNav.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  /* ----------------------------------------------------------
     Scroll Reveal Animations (IntersectionObserver)
     ---------------------------------------------------------- */
  function initScrollReveal() {
    var revealElements = document.querySelectorAll('.reveal');

    if (!('IntersectionObserver' in window)) {
      // Fallback: show everything immediately
      revealElements.forEach(function (el) {
        el.classList.add('revealed');
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      }
    );

    revealElements.forEach(function (el) {
      observer.observe(el);
    });
  }

  initScrollReveal();

  /* ----------------------------------------------------------
     Smooth Scroll for Anchor Links
     ---------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var headerHeight = document.querySelector('.header')
          ? document.querySelector('.header').getBoundingClientRect().height
          : 0;
        var targetPosition =
          target.getBoundingClientRect().top + window.scrollY - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  /* ----------------------------------------------------------
     Header shadow enhancement on scroll
     ---------------------------------------------------------- */
  var header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10) {
        header.style.boxShadow = '0 2px 12px rgba(0, 0, 0, 0.08)';
      } else {
        header.style.boxShadow = '0 1px 4px rgba(0, 0, 0, 0.06)';
      }
    }, { passive: true });
  }

  /* ----------------------------------------------------------
     FAQ Accordion Toggle
     ---------------------------------------------------------- */
  var faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(function (item) {
    var question = item.querySelector('.faq-question');
    var answer = item.querySelector('.faq-answer');

    if (question && answer) {
      question.addEventListener('click', function () {
        var isOpen = item.classList.contains('faq-item--open');

        // Close all other items
        faqItems.forEach(function (other) {
          if (other !== item) {
            other.classList.remove('faq-item--open');
            var otherAnswer = other.querySelector('.faq-answer');
            if (otherAnswer) {
              otherAnswer.style.maxHeight = '0';
            }
            var otherQuestion = other.querySelector('.faq-question');
            if (otherQuestion) {
              otherQuestion.setAttribute('aria-expanded', 'false');
            }
          }
        });

        // Toggle current item
        if (!isOpen) {
          item.classList.add('faq-item--open');
          answer.style.maxHeight = answer.scrollHeight + 'px';
          question.setAttribute('aria-expanded', 'true');
        } else {
          item.classList.remove('faq-item--open');
          answer.style.maxHeight = '0';
          question.setAttribute('aria-expanded', 'false');
        }
      });
    }
  });

  /* ----------------------------------------------------------
     FAQ Category Filtering
     ---------------------------------------------------------- */
  var faqTabs = document.querySelectorAll('.faq-tab');

  faqTabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var category = this.getAttribute('data-category');

      // Update active tab
      faqTabs.forEach(function (t) {
        t.classList.remove('active');
      });
      this.classList.add('active');

      // Filter items
      faqItems.forEach(function (item) {
        // Close any open items
        item.classList.remove('faq-item--open');
        var answer = item.querySelector('.faq-answer');
        if (answer) {
          answer.style.maxHeight = '0';
        }
        var question = item.querySelector('.faq-question');
        if (question) {
          question.setAttribute('aria-expanded', 'false');
        }

        // Show/hide based on category
        if (category === 'all' || item.getAttribute('data-category') === category) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  /* ----------------------------------------------------------
     Lightbox — photo gallery enlargement
     ---------------------------------------------------------- */
  (function initLightbox() {
    var triggers = document.querySelectorAll('.lightbox-trigger');
    if (!triggers.length) return;

    // Create overlay once
    var overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    overlay.innerHTML =
      '<button class="lightbox-close" aria-label="Close">&times;</button>' +
      '<img src="" alt="">' +
      '<div class="lightbox-caption"></div>';
    document.body.appendChild(overlay);

    var lbImg = overlay.querySelector('img');
    var lbCaption = overlay.querySelector('.lightbox-caption');
    var lbClose = overlay.querySelector('.lightbox-close');

    function open(trigger) {
      lbImg.src = trigger.src;
      lbImg.alt = trigger.alt;
      lbCaption.textContent = trigger.getAttribute('data-caption') || trigger.alt || '';
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
      lbImg.src = '';
    }

    triggers.forEach(function (img) {
      img.addEventListener('click', function () { open(this); });
    });

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay || e.target === lbImg || e.target === lbClose) close();
    });
    lbClose.addEventListener('click', close);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('active')) close();
    });
  })();

})();
