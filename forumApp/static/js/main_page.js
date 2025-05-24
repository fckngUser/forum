document.addEventListener('DOMContentLoaded', function() {
    const articleTexts = document.querySelectorAll('.article-item p');
    
    articleTexts.forEach(text => {
        text.addEventListener('click', function() {
            this.classList.toggle('expanded');
        });
    });
});