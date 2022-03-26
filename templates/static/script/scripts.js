$(document).ready(function(){
    const win = $(window).offsetParent().width();
    if(win < 400){
        $('#logo').text('Crônicas do Pufzilla')
    };
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass('stick')
        } else {
            $('.navbar').removeClass('stick')
        }
    });
    $('.menu_toggler').click(function(){
        $(this).toggleClass('active')
        $('.navbar_menu').toggleClass('active')
    });
});
