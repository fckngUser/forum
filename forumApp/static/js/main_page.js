document.addEventListener('DOMContentLoaded', function() {
    const articles = document.querySelectorAll('.article-item');
    
    articles.forEach(article => {
        const content = article.querySelector('.article-content');
        const initialHeight = content.scrollHeight + "px";
        
        content.style.maxHeight = '0';
        
        article.addEventListener('click', function() {
            if (this.classList.contains('expanded')) {
                content.style.maxHeight = '0';
            } else {
                content.style.maxHeight = initialHeight;
               
                setTimeout(() => {
                    if (this.classList.contains('expanded')) {
                        content.style.maxHeight = 'none';
                    }
                }, 300);
            }
            this.classList.toggle('expanded');
        });
    });
});