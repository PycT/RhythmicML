function asyncGetRequest(request_url, dom_element_id, to_innerHTML = true)
{
    var async_request = new XMLHttpRequest();
    
    async_request.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            if (to_innerHTML)
            {
                document.getElementById(dom_element_id).innerHTML = this.responseText;
            }
            else 
            {
                document.getElementById(dom_element_id).value = this.responseText;
            }
        }
    }

    async_request.open("GET", request_url + "?anti_cache = " + Math.random(), true);
    async_request.send();
}

function asyncPostRequest(request_url, data, dom_element_id, to_innerHTML = true)
{
    var async_request = new XMLHttpRequest();
    async_request.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            if (to_innerHTML)
            {
                document.getElementById(dom_element_id).innerHTML = this.responseText;
            }
            else 
            {
                document.getElementById(dom_element_id).value = this.responseText;
            }
        }
    }

    async_request.open("POST", request_url + "?anti_cache = " + Math.random(), true);
    async_request.send(data);
}