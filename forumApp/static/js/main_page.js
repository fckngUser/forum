document.addEventListener('DOMContentLoaded', function() {
    const articleItems = document.querySelectorAll('.article-item');
    
    articleItems.forEach(item => {
        const header = item.querySelector('.article-header');
        
        header.addEventListener('click', function() {
            // Переключаем класс expanded у родительского элемента
            item.classList.toggle('expanded');
            
            // Закрываем другие открытые статьи (опционально)
            if (item.classList.contains('expanded')) {
                articleItems.forEach(otherItem => {
                    if (otherItem !== item && otherItem.classList.contains('expanded')) {
                        otherItem.classList.remove('expanded');
                    }
                });
            }
        });
    });
    
    // Закрытие статьи при клике вне её области (опционально)
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.article-item')) {
            articleItems.forEach(item => {
                item.classList.remove('expanded');
            });
        }
    });
});