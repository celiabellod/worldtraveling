jQuery(function($) {

    checkCookie_eu();

    function checkCookie_eu()
    {

        var consent = getCookie_eu("cookies_consent");

        if (consent == null || consent == "" || consent == undefined)
        {

            $('#cookie_directive_container').show();
        }

    }

    function setCookie_eu(c_name,value,exdays)
    {

        var exdate = new Date();
        exdate.setDate(exdate.getDate() + exdays);
        var c_value = escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
        document.cookie = c_name + "=" + c_value+"; path=/";

        $('#cookie_directive_container').hide();
    }


    function getCookie_eu(c_name)
    {
        var i,x,y,ARRcookies=document.cookie.split(";");
        for (i=0;i<ARRcookies.length;i++)
        {
            x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
            y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
            x=x.replace(/^\s+|\s+$/g,"");
            if (x==c_name)
            {
                return unescape(y);
            }
        }
    }

    $("#cookie_accept").click(function(){
        setCookie_eu("cookies_consent", 1, 30);
    });

    $('#cookie_refuse').click(function(){
            $('#cookie_directive_container').hide();
    });

});