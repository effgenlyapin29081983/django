window.onload = function () {
    $('.product_list').on('click', 'button[type="button"]', function () {
        var target = event.target;
        console.log(target.name); // ID of basket object
        //console.log(target.value); // quantity of basket object

        $.ajax({
            url: '/baskets/add/' + target.name + '/',
            success: function (data) {
                //$('.basket_list').html(data.result);
            },
        });
    });
}