function async_get_request(request_url, dom_element_id)
{
    xhttp.onreadystatechange = function()
    {
        document.getElementById(dom_element_id).innerHTML = this.responseText;
    }

    xhttp.open("GET", request_url + "?anti_cache = " + Math.random(), true);
    xhttp.send();
}