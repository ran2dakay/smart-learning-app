// ========== Progress Bar Animation ==========
function animateProgressBars() {
    document.querySelectorAll('.progress-bar-animated').forEach(bar => {
        const target = bar.dataset.width || '0';
        bar.style.setProperty('--target-width', target + '%');
        setTimeout(() => bar.classList.add('animate'), 100);
    });
}

// ========== SVG Circle Progress ==========
function animateCircleProgress() {
    document.querySelectorAll('.progress-circle-fill').forEach(circle => {
        const percent = parseFloat(circle.dataset.percent || 0);
        const circumference = 283;
        const offset = circumference - (percent / 100) * circumference;
        setTimeout(() => {
            circle.style.strokeDashoffset = offset;
        }, 200);
    });
}

// ========== Toast Notifications ==========
function showToast(message, type = 'success') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        document.body.appendChild(container);
    }
    const toast = document.createElement('div');
    toast.className = `toast-msg toast-${type}`;
    toast.innerHTML = `<i class="bi bi-${type === 'success' ? 'check-circle' : 'info-circle'} me-2"></i>${message}`;
    container.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 2500);
}

// ========== Toggle Progress (AJAX) ==========
function setupCheckboxes() {
    document.querySelectorAll('.checkbox-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const topicId = this.dataset.topicId;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(`/toggle-progress/${topicId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
            })
            .then(r => r.json())
            .then(data => {
                const topicCard = this.closest('.topic-card');
                const icon = this.querySelector('.checkbox-icon');
                const checkIcon = this.querySelector('.bi');

                if (data.completed) {
                    this.classList.add('checked');
                    icon.innerHTML = '<i class="bi bi-check text-white" style="font-size:0.9rem"></i>';
                    topicCard && topicCard.classList.add('completed');
                    showToast('Topic marked as complete!', 'success');
                } else {
                    this.classList.remove('checked');
                    icon.innerHTML = '';
                    topicCard && topicCard.classList.remove('completed');
                    showToast('Topic unmarked', 'info');
                }

                // Update roadmap progress bars
                const roadmapId = this.dataset.roadmapId;
                if (roadmapId) {
                    updateRoadmapProgress(roadmapId, data);
                }
            })
            .catch(err => console.error('Error toggling progress:', err));
        });
    });
}

function updateRoadmapProgress(roadmapId, data) {
    const bar = document.querySelector(`[data-roadmap-bar="${roadmapId}"]`);
    const pct = document.querySelector(`[data-roadmap-pct="${roadmapId}"]`);
    const comp = document.querySelector(`[data-roadmap-completed="${roadmapId}"]`);
    const rem = document.querySelector(`[data-roadmap-remaining="${roadmapId}"]`);

    if (bar) {
        bar.dataset.width = data.roadmap_percent;
        bar.style.width = data.roadmap_percent + '%';
    }
    if (pct) pct.textContent = data.roadmap_percent + '%';
    if (comp) comp.textContent = data.completed_count;
    if (rem) rem.textContent = data.remaining_count;
}

// ========== Scroll Reveal ==========
function setupScrollReveal() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.glass-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(card);
    });
}

// ========== Navbar Scroll Effect ==========
function setupNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.4)';
        } else {
            navbar.style.boxShadow = 'none';
        }
    });
}

// ========== Smooth Scroll ==========
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            const target = document.querySelector(a.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
}

// ========== Init ==========
document.addEventListener('DOMContentLoaded', () => {
    animateProgressBars();
    animateCircleProgress();
    setupCheckboxes();
    setupNavbarScroll();
    setupSmoothScroll();

    // Delay scroll reveal slightly
    setTimeout(setupScrollReveal, 300);
});
