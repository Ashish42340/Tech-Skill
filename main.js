/**
 * Tech Skills Checker - Main JavaScript File
 * Handles all client-side interactions
 */

// Wait for DOM to load
$(document).ready(function() {
    console.log('🚀 Tech Skills Checker Loaded!');
    
    // Initialize all components
    initializeAlerts();
    initializeTooltips();
    initializeAnimations();
    initializeFormValidation();
    
    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);
});

/**
 * Initialize Bootstrap tooltips
 */
function initializeTooltips() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Initialize alerts with close functionality
 */
function initializeAlerts() {
    // Add fade-in animation to alerts
    $('.alert').addClass('fade-in');
    
    // Custom close button functionality
    $('.alert .btn-close').on('click', function() {
        $(this).closest('.alert').fadeOut('fast');
    });
}

/**
 * Initialize scroll animations
 */
function initializeAnimations() {
    // Add fade-in animation on scroll
    $(window).scroll(function() {
        $('.fade-in-scroll').each(function() {
            var elementTop = $(this).offset().top;
            var elementBottom = elementTop + $(this).outerHeight();
            var viewportTop = $(window).scrollTop();
            var viewportBottom = viewportTop + $(window).height();
            
            if (elementBottom > viewportTop && elementTop < viewportBottom) {
                $(this).addClass('fade-in');
            }
        });
    });
    
    // Smooth scroll to top button
    var scrollTopBtn = $('<button>')
        .addClass('btn btn-primary btn-floating')
        .attr('id', 'scrollTopBtn')
        .html('<i class="fas fa-arrow-up"></i>')
        .css({
            'position': 'fixed',
            'bottom': '20px',
            'right': '20px',
            'display': 'none',
            'z-index': '999',
            'border-radius': '50%',
            'width': '50px',
            'height': '50px',
            'box-shadow': '0 4px 8px rgba(0,0,0,0.2)'
        });
    
    $('body').append(scrollTopBtn);
    
    // Show/hide scroll button
    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            $('#scrollTopBtn').fadeIn();
        } else {
            $('#scrollTopBtn').fadeOut();
        }
    });
    
    // Scroll to top on click
    $('#scrollTopBtn').click(function() {
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });
}

/**
 * Form validation
 */
function initializeFormValidation() {
    // Add validation to all forms with class 'needs-validation'
    var forms = document.querySelectorAll('.needs-validation');
    
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}

/**
 * Show loading spinner
 */
function showLoading(message = 'Loading...') {
    var loadingHtml = `
        <div class="loading-overlay" id="loadingOverlay">
            <div class="text-center text-white">
                <div class="spinner-border mb-3" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <p>${message}</p>
            </div>
        </div>
    `;
    $('body').append(loadingHtml);
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    $('#loadingOverlay').fadeOut('fast', function() {
        $(this).remove();
    });
}

/**
 * Show toast notification
 */
function showToast(message, type = 'success') {
    var bgColor = type === 'success' ? 'bg-success' : 
                  type === 'error' ? 'bg-danger' : 
                  type === 'warning' ? 'bg-warning' : 'bg-info';
    
    var icon = type === 'success' ? 'fa-check-circle' : 
               type === 'error' ? 'fa-times-circle' : 
               type === 'warning' ? 'fa-exclamation-triangle' : 'fa-info-circle';
    
    var toastHtml = `
        <div class="toast-notification ${bgColor} text-white" style="
            position: fixed;
            top: 80px;
            right: 20px;
            z-index: 9999;
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            gap: 10px;
            animation: slideIn 0.3s ease-out;
        ">
            <i class="fas ${icon}"></i>
            <span>${message}</span>
        </div>
    `;
    
    var $toast = $(toastHtml);
    $('body').append($toast);
    
    setTimeout(function() {
        $toast.fadeOut('fast', function() {
            $(this).remove();
        });
    }, 3000);
}

/**
 * Confirm dialog
 */
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

/**
 * Copy to clipboard
 */
function copyToClipboard(text) {
    var $temp = $('<textarea>');
    $('body').append($temp);
    $temp.val(text).select();
    document.execCommand('copy');
    $temp.remove();
    showToast('Copied to clipboard!', 'success');
}

/**
 * Format date
 */
function formatDate(dateString) {
    var date = new Date(dateString);
    var options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

/**
 * Debounce function for search inputs
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Search filter for tables
 */
function initializeTableSearch() {
    $('#tableSearch').on('keyup', debounce(function() {
        var value = $(this).val().toLowerCase();
        $('#dataTable tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    }, 300));
}

/**
 * Skill card animations
 */
$(document).on('mouseenter', '.skill-card', function() {
    $(this).addClass('pulse');
});

$(document).on('mouseleave', '.skill-card', function() {
    $(this).removeClass('pulse');
});

/**
 * Progress bar animation
 */
function animateProgressBar(element, targetWidth) {
    $(element).css('width', '0%').animate({
        width: targetWidth + '%'
    }, 1000);
}

/**
 * Count up animation for numbers
 */
function countUp(element, target, duration = 1000) {
    var start = 0;
    var increment = target / (duration / 16);
    
    var timer = setInterval(function() {
        start += increment;
        if (start >= target) {
            start = target;
            clearInterval(timer);
        }
        $(element).text(Math.floor(start));
    }, 16);
}

/**
 * Local storage helpers
 */
const Storage = {
    set: function(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            console.error('Storage error:', e);
            return false;
        }
    },
    
    get: function(key) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : null;
        } catch (e) {
            console.error('Storage error:', e);
            return null;
        }
    },
    
    remove: function(key) {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (e) {
            console.error('Storage error:', e);
            return false;
        }
    },
    
    clear: function() {
        try {
            localStorage.clear();
            return true;
        } catch (e) {
            console.error('Storage error:', e);
            return false;
        }
    }
};

/**
 * API Helper functions
 */
const API = {
    // Add skill
    addSkill: function(skillId, proficiency, callback) {
        $.ajax({
            url: '/api/add-skill',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                skill_id: skillId,
                proficiency: proficiency
            }),
            success: function(response) {
                showToast('Skill added successfully!', 'success');
                if (callback) callback(response);
            },
            error: function(xhr) {
                showToast(xhr.responseJSON?.message || 'Error adding skill', 'error');
            }
        });
    },
    
    // Remove skill
    removeSkill: function(skillId, callback) {
        $.ajax({
            url: '/api/remove-skill',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({skill_id: skillId}),
            success: function(response) {
                showToast('Skill removed successfully!', 'success');
                if (callback) callback(response);
            },
            error: function(xhr) {
                showToast(xhr.responseJSON?.message || 'Error removing skill', 'error');
            }
        });
    },
    
    // Update proficiency
    updateProficiency: function(skillId, proficiency, callback) {
        $.ajax({
            url: '/api/update-proficiency',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                skill_id: skillId,
                proficiency: proficiency
            }),
            success: function(response) {
                showToast('Proficiency updated!', 'success');
                if (callback) callback(response);
            },
            error: function(xhr) {
                showToast(xhr.responseJSON?.message || 'Error updating proficiency', 'error');
            }
        });
    }
};

/**
 * Initialize progress bars with animation
 */
$(window).on('load', function() {
    $('.progress-bar').each(function() {
        var width = $(this).attr('style').match(/width:\s*(\d+)%/);
        if (width && width[1]) {
            animateProgressBar(this, parseInt(width[1]));
        }
    });
    
    // Animate stat numbers
    $('.stat-number').each(function() {
        var target = parseInt($(this).text());
        if (!isNaN(target)) {
            countUp(this, target);
        }
    });
});

/**
 * Handle form submissions with loading states
 */
$('form').on('submit', function(e) {
    var $form = $(this);
    var $submitBtn = $form.find('button[type="submit"]');
    
    if ($form.hasClass('ajax-form')) {
        e.preventDefault();
        // Handle AJAX submission
    } else {
        // Show loading for regular form submission
        $submitBtn.prop('disabled', true);
        var originalText = $submitBtn.html();
        $submitBtn.html('<span class="spinner-border spinner-border-sm me-2"></span>Loading...');
        
        // Re-enable after 10 seconds (safety measure)
        setTimeout(function() {
            $submitBtn.prop('disabled', false);
            $submitBtn.html(originalText);
        }, 10000);
    }
});

/**
 * Keyboard shortcuts
 */
$(document).keydown(function(e) {
    // Ctrl/Cmd + K for search
    if ((e.ctrlKey || e.metaKey) && e.keyCode === 75) {
        e.preventDefault();
        $('#tableSearch, #searchInput').focus();
    }
    
    // Escape to close modals
    if (e.keyCode === 27) {
        $('.modal').modal('hide');
    }
});

/**
 * Print functionality
 */
function printPage() {
    window.print();
}

/**
 * Export to CSV (for future use)
 */
function exportToCSV(data, filename) {
    var csv = data.map(row => row.join(',')).join('\n');
    var blob = new Blob([csv], { type: 'text/csv' });
    var url = window.URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
}

// Console message
console.log('%c🚀 Tech Skills Checker', 'color: #667eea; font-size: 20px; font-weight: bold;');
console.log('%cBuilt with ❤️ using Flask + Bootstrap', 'color: #764ba2; font-size: 14px;');
console.log('%cHappy skill tracking! 💪', 'color: #28a745; font-size: 14px;');