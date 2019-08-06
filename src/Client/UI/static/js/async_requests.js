function asyncGetRequest(request_url, dom_element_id, to_innerHTML = true)
{
    var the_element = document.getElementById(dom_element_id);
    var async_request = new XMLHttpRequest();
    
    async_request.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            if (to_innerHTML)
            {
                the_element.innerHTML = this.responseText;
            }
            else 
            {
                the_element.value = this.responseText;
            }
        }
    }

    if (to_innerHTML)
    {
        the_element.innerHTML = "<div class = 'wait_blinker'>Please wait...</div>";
    }

    async_request.open("GET", request_url + "?anti_cache=" + Math.random(), true);
    async_request.send();
}

function asyncPostRequest(request_url, data, dom_element_id, to_innerHTML = true)
{
    var the_element = document.getElementById(dom_element_id);
    var async_request = new XMLHttpRequest();
    async_request.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            if (to_innerHTML)
            {
                the_element.innerHTML = this.responseText;
            }
            else 
            {
                the_element.value = this.responseText;
            }
        }
    }

    if (to_innerHTML)
    {
        the_element.innerHTML = "<div class = 'wait_blinker'>Please wait...</div>";
    }

    async_request.open("POST", request_url + "?anti_cache=" + Math.random(), true);
    async_request.send(data);
}

function asyncPostRequestWithRefresh(request_url, data, dom_element_id, refresh_ok = "Success")
{
    var the_element = document.getElementById(dom_element_id);
    var async_request = new XMLHttpRequest();
    async_request.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            if (this.responseText == refresh_ok)
            {
                window.location.reload(true);
            }
            else 
            {
                the_element.innerHTML = this.responseText;
            }
        }
    }

    if (dom_element_id)
    {
        the_element.innerHTML = "<div class = 'wait_blinker'>Please wait...</div>";
    }

    async_request.open("POST", request_url + "?anti_cache=" + Math.random(), true);
    async_request.send(data);
}