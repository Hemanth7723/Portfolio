document.addEventListener('DOMContentLoaded', () => {
    console.log('Cyberpunk effects initialized');

    // Random glitch effect on elements with 'glitch-hover' class
    const glitchElements = document.querySelectorAll('.project, .resume-wrap');
    glitchElements.forEach(el => {
        el.addEventListener('mouseover', () => {
            el.style.filter = 'hue-rotate(' + Math.random() * 90 + 'deg)';
        });
        el.addEventListener('mouseout', () => {
            el.style.filter = 'none';
        });
    });
});
