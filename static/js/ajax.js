function scrollPage() {
    'use strict';
    let formId = $('form').attr('id');
    let formNm = $('#' + formId);
    $.ajax({
        type:"POST",
        data: id ,
        success: function(data){
            console.log(data);   /* выведет "Ошибка" */
        },
        
    });
    const el = document.getElementById('replay-box')
    el.scrollIntoView();
    return false;
}

$(document).ready(function () {
    $('form').submit(function () {
        var formID = $(this).attr('id'); // Получение ID формы
        var formNm = $('#' + formID);
        $.ajax({
            type: 'POST',
           
            data: formNm.serialize(),
            success: function (data) {
                // Вывод текста результата отправки в текущей форме
                $(formNm).html(data);
            }
        });
        return false;
    });
});



$(document).ready(function () {
    $('form').submit(function () {
        let id = $(this).attr('id');
        let p = $('#form-comment [name="parent_id"]').val(id);      
            $.ajax({
                type: 'GET',         
                data: {p:p},
                
            });
            const el = document.getElementById('replay-box')
            el.scrollIntoView();
            return false;
    });
});