function open(){
    $('.overlay').addClass(open);
}
window.addEventListener('scroll',function(){
    const offset = window.pageYOffset;
    if (offset> 60)
    {
        $('nav').addClass('scrolled');
        $('.inner').first().addClass('little');
    }
    else{
        $('nav').removeClass('scrolled');
        $('.inner').first().removeClass('little');

    }
})
window.onload = (event) => {
    let a = window.location.href.split('/');
    var change = document.getElementsByClassName('nav_li');
    if (a[3]=="")
        change[0].classList.add('current');
}