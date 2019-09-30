var me = {};
me.avatar = "http://www.clker.com/cliparts/P/V/A/d/g/T/male-md.png";

var you = {};
you.avatar = "https://i.imgur.com/lLO0jhI.jpg";

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text, score, time){
    if (time === undefined){
        time = 0;
    }
    var control = "";
    var date = formatAMPM(new Date());
    // console.log(who);
    if (who == "Customer"){ //Left Message
        control = '<li style="width:100%">' +
                        '<div class="chatMessage">' +
                            '<div class="msj macro">' +
                            '<div class="avatar"><img class="img-circle" style="width:100%;" src="'+ me.avatar +'" /></div>' +
                                '<div class="text text-l">' +
                                    '<p title=\"'+ score +'\">'+ text +'</p>' +
                                    '<p><small>'+date+'</small></p>' +
                                '</div>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{ // Right message
        control = '<li style="width:100%;">' +
                        '<div class="chatMessage">' +
                            '<div class="msj-rta macro">' +
                                '<div class="text text-r">' +
                                    '<p title=\"'+ score +'\">'+ text +'</p>' +
                                    '<p><small>'+date+'</small></p>' +
                                '</div>' +
                            '<div class="avatar" style="padding:0px 0px 0px 5px !important"><img class="img-circle" style="width:100%;" src="'+you.avatar+'" /></div>' +
                        '</div>' +
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control).scrollTop($("ul").prop('scrollHeight'));
        }, time);
    
}

function resetChat(){
    $("ul").empty();
}

$(".mytext").on("keydown", function(e){
    if (e.which == 13){
        var text = $(this).val();
        if (text !== ""){
            insertChat("me", text);              
            $(this).val('');
        }
    }
});



//-- Clear Chat
resetChat();

// //-- Print Messages
// insertChat("me", "Hello Tom...", 0);  
// insertChat("you", "Hi, Pablo", 1500);
// insertChat("me", "What would you like to talk about today?", 3500);
// insertChat("you", "Tell me a joke",7000);
// insertChat("me", "Spaceman: Computer! Computer! Do we bring battery?!", 9500);
// insertChat("you", "LOL", 12000);

