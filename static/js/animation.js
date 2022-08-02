function delay(n) {
    n = n || 2000;
    return new Promise((done) => {
        setTimeout(() => {
            done();
        }, n);
    });
}

function pageTransition() {
    var tl = gsap.timeline();
    
    tl.to(".loading-screen", {
        opacity:1,
        duration: 0.6,
    });

    
}

function contentAnimation() {
    var tl = gsap.timeline();   
    tl.to(".loading-screen", {
        opacity: 0,
        duration:1.2,
    });
}


$(function () {
    barba.init({
        sync: true,

        transitions: [
            {
                async leave(data) {
                    const done = this.async();

                    pageTransition();
                    await delay(800);
                    done();
                },
                async enter(data) {
                    contentAnimation();
                },

                async once(data) {
                    contentAnimation();
                },

            },
        ],
    });
});