document.querySelectorAll('.article-item p').forEach(p => {
    p.addEventListener('click', () => {
        p.style.webkitLineClamp = 'unset';
        p.style.maxHeight = 'none';
    });
});