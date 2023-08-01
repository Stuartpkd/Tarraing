$(document).ready(function () {
    $('.toggle-switch input[type="radio"]').change(function () {
        $('.toggle-content').hide();
        $('#' + $(this).attr('id') + '_content').show();
    });
});