var ready = false;
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
    if (a[3]=="portfolio")
        change[1].classList.add('current');
    if (a[3]=="szolgaltatasok")
        change[2].classList.add('current');
    if (a[3]=="kapcsolat")
        change[3].classList.add('current');
    if (a[3]=="admin")
        change[4].classList.add('current');


    //Load
    /*const anchors = document.querySelectorAll('a');
    const transition_el = document.querySelector('.transition');
    
    setTimeout(() => {
        transition_el.classList.remove('is-active');
    }, 500);
    


        for (let i = 0; i < anchors.length; i++) {
            const anchor = anchors[i];
        anchor.addEventListener('click', e => {
            console.log(e.currentTarget)
            let secondtarget = e.currentTarget.href;
            e.preventDefault();
            let target = e.target.href;
            
            transition_el.classList.add('is-active');
            
 

            setInterval(() => {
                window.location.href = target;
            }, 500);
            
            
            
        })
    }
    setTimeout(() => {
        const kep = document.querySelectorAll(".imageholder");
        for (let i = 0; i < kep.length; i++) 
        {
            kep[i].addEventListener("click", e => {
                
                e.preventDefault();
                transition_el.classList.add('is-active');

                setInterval(() => {
                    window.location.href = "/projekt/" + kep[i].getAttribute('value');
                }, 500);
                
                
            });
        }
    }, 1200);

*/
      
}

