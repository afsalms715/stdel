$(document).ready(function(){
    $("#submit-form").validate({
        rules:{
            name:{
                required:true,
                minlength:4
            },
            email:{
                required:true,
                email:true
            },
            phNo:{
                required:true,
                number:true,
                minlength:10,
                maxlength:12
            }
        }
    })
})