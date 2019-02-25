$(document).ready(() => {
    $('.scroll-top-button').click(e => {
        $('body, html').animate({scrollTop: 0}, 500)
    })
})