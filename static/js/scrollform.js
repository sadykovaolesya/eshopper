
$(function () {
    var x = document.getElementsByName('form1');
    $(x).submit(function () {
        let id = $(this).attr('id');
        document.getElementById('parent_id').value = id
           
            const el = document.getElementById('replay-box')
            el.scrollIntoView();
            return false;
    });
});