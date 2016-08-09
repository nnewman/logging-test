(function($) {
    'use strict';

    $('#trigger-warning').on('click', function(event) {
        $.ajax({
            url: "/warning",
            context: document.body
        }).done(function() {
            console.log('info');
        });
    });

    $('#trigger-error').on('click', function(event) {
        $.ajax({
            url: "/error",
            context: document.body
        }).done(function() {
            console.log('info');
        });
    });

    $('#trigger-exception').on('click', function(event) {
        $.ajax({
            url: "/exception",
            context: document.body
        }).done(function() {
            console.log('info');
        });
    });

    $('#trigger-success').on('click', function(event) {
        $.ajax({
            url: "/success",
            context: document.body
        }).done(function() {
            console.log('info');
        });
    });

})(jQuery);