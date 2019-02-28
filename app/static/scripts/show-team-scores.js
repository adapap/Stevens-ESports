$(document).ready(() => {
    $nav = $('.game-nav .game-name')
    $nav.click(e => {
        $nav.removeClass('selected')
        $(e.target).addClass('selected')
        $game = $(e.target).data('game')
        $('[data-game-info]').removeClass('selected')
        $games = $('[data-game-info="' + $game + '"]')
        $games.addClass('selected')
    })
})