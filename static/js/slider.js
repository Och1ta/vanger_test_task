$(document).ready(function(){
    $('.main-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        fade: true,
        asNavFor: '.thumbnail-slider'
    });
    $('.thumbnail-slider').slick({
        slidesToShow: slides,
        slidesToScroll: 1,
        asNavFor: '.main-slider',
        dots: true,
        centerMode: true,
        focusOnSelect: true
    });

    const modalItems = document.querySelectorAll('.carousel-item');
    const mainImages = document.querySelectorAll('.main-image');
    mainImages.forEach((item, index) => {
        item.addEventListener('click', () => handleImageClick(index));
    });
    const handleImageClick = (index) => {
        modalItems.forEach(item => item.classList.remove('active'));
        modalItems[index].classList.add('active');
    };

    const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(function(navLink) {
            navLink.addEventListener('click', function() {
                const navbarCollapse = document.querySelector('.navbar-collapse');
                navbarCollapse.classList.remove('show');
            });
        });
});