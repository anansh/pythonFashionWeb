  $(function () {

    // MENU
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('toggle');
    });

    // AOS ANIMATION
    AOS.init({
      disable: 'mobile',
      duration: 800,
      anchorPlacement: 'center-bottom'
    });


    // SMOOTHSCROLL NAVBAR
    $(function() {
      $('.navbar a, .hero-text a').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
        }, 1000);
        event.preventDefault();
      });
    });

  });

 $(document).ready(function(){
    $("#post_form").submit(function(e){
      e.preventDefault();
      $(".btnClick").prop('disabled', true);
      $(".btnClick").text('Processing...');
      var $form = $(this);
      var name = $("#name").val();
      var taskAdd = $("#taskAdd").val();
      var email = $("#email").val();
      var mobile = $("#mobile").val();
      var message = $("#message").val();
      var data = [{
            "name" : name,
            "taskAdd" : taskAdd,
            "email" : email,
            "mobile" : mobile,
            "message" : message
      }];
      var serializedData = JSON.stringify(data);
      var $res_message = $(".resmessage");
      var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

      $res_message.hide();
      $.ajax({
          url: '/registerUser/',
          type: "POST",
          data: {
            'data': serializedData,
            'csrfmiddlewaretoken': csrftoken
          },
          dataType: 'json',
          success: function (data) {
            if(data.response == 'Success'){
                $('#successMessage').show(0).delay(5000).hide(0);
                $("#registeredUsers").text(data.registeredUsersCount);
                $("#membershipForm").modal("hide");
                $("#post_form").trigger("reset");
            } else {
                alert("Something went wrong : "+ data.message);
            }
          }
        });
    });

    $("#put_form").submit(function(e){
        e.preventDefault();
        var name = $("#updateName").val();
        var email = $("#updateEmail").val();
        var mobile = $("#updateMobile").val();
        var message = $("#updateMessage").val();
        var pk =  $("#pk").val();
        var data = [{
            "name" : name,
            "email" : email,
            "mobile" : mobile,
            "message" : message,
            "pk" : pk
        }];
        var serializedData = JSON.stringify(data);
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
              url: '/updateThisUser/',
              type: "POST",
              dataType: 'json',
              data: {
                'data': serializedData,
                'csrfmiddlewaretoken': csrftoken
              },
              success: function (data) {
                $("#updateMembershipForm").modal("hide");
                $('#successMessage').show(0).delay(5000).hide(0);
              }
        });
    });
  });

 function loadRegisteredUsers(self) {
    data = "";
    $.ajax({
          url: '/loadRegisteredUser/',
          type: "GET",
          dataType: 'json',
          success: function (data) {
            if(data.response == 'Success'){
               var finalData = JSON.parse(data.users);
               for(var i = 0; i < finalData.length; i++) {
                   data += "<tr><td>"+finalData[i].fields.name+"</td><td>"+finalData[i].fields.mobile+"</td><td>"+
                   finalData[i].fields.email+"</td><td>"+finalData[i].fields.message+"</td><td><button type='button' "+
                   "class='btn btn-warning' onclick='updatePopup(this,"+finalData[i].pk+")'>Update</button></td><td>"+
                   "<button type='button' class='btn btn-danger' onclick='deleteRow(this, "+finalData[i].pk+")'>"+
                   "Delete</button></td></tr>"
               }
               $("#userList").empty().append(data);
               $("#listOfRegisteredUsers").modal("show");
            } else {
                alert("Something went wrong : "+ data.message);
            }
          }
    });
 }

 function deleteRow(obj, pk) {
    var data = [{
            "pk" : pk
      }];
    var serializedData = JSON.stringify(data);
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
          url: '/deleteThisUser/',
          type: "POST",
          dataType: 'json',
          data: {
            'data': serializedData,
            'csrfmiddlewaretoken': csrftoken
          },
          success: function (data) {
            $('#successMessage').show(0).delay(4000).hide(0);
            $("#listOfRegisteredUsers").modal("hide");
            $("#registeredUsers").text(data.registeredUsersCount);
          }
    });
 }

function updatePopup(obj, pk) {
    data = "";
    var data = [{
            "pk" : pk
      }];
    var serializedData = JSON.stringify(data);
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
          url: '/getRegisteredUser/',
          type: "POST",
          dataType: 'json',
          data: {
            'data': serializedData,
            'csrfmiddlewaretoken': csrftoken
          },
          success: function (data) {
            if(data.response == 'Success'){
               var finalData = JSON.parse(data.userData);
               $("#updateName").val(finalData[0].fields.name);
               $("#updateEmail").val(finalData[0].fields.email);
               $("#updateMobile").val(finalData[0].fields.mobile);
               $("#updateMessage").val(finalData[0].fields.message);
               $("#pk").val(pk);
               $("#listOfRegisteredUsers").modal("hide");
               $("#updateMembershipForm").modal("show");
            } else {
                alert("Something went wrong : "+ data.message);
            }
          }
    });
}