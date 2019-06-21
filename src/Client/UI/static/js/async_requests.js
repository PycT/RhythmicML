function asyncGetRequest(request_url, dom_element_id)
{
    var async_request = new XMLHttpRequest();
    async_request.onreadystatechange = function()
    {
        document.getElementById(dom_element_id).innerHTML = this.responseText;
    }

    async_request.open("GET", request_url + "?anti_cache = " + Math.random(), true);
    async_request.send();
}

function asyncPostRequest(request_url, data, dom_element_id)
{
    var async_request = new XMLHttpRequest();
    async_request.onreadystatechange = function()
    {
        document.getElementById(dom_element_id).innerHTML = this.responseText;
    }

    async_request.open("POST", request_url + "?anti_cache = " + Math.random(), true);
    async_request.send(data);
}