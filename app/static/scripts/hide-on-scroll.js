$(document).ready(() => {
    var position = 0;

    $(window).scroll(e => {
        var $element = $('#header');
        var scrollTop = $(this).scrollTop();
        if (scrollTop <= 0)
            {$element.removeClass('hide').removeClass('scrolling');
        } else if (scrollTop < position) {
            $element.removeClass('hide');
        } else if (scrollTop > position) {
            $element.addClass('scrolling');
            if (scrollTop + $(window).height() >= $(document).height() - $element.height()) {
                $element.removeClass('hide');
            } else if (Math.abs($element.position().top) < $element.height()) {
                $element.addClass('hide');
            }
        }
        position = scrollTop;
    })
})