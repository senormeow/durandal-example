define(['jquery', 'durandal/app', 'knockout'], function ($, app, ko) {

    return function() {
        this.users = ko.observableArray([]);
    
        this.getData = function(){
            that = this;
            return $.ajax('/api/users').done(function(data) {
                console.log(data);
                that.users(data); 
        });
    };
    
        this.activate = function() {
            this.getData();  
        };
    
   };
});