"use strict";

function toggleDisplay(dom_element_id, display = "flex")
{
    var the_element = document.getElementById(dom_element_id);

    if (the_element.style.display == "none")
    {
        the_element.style.display = display;
    }
    else
    {
        the_element.style.display = "none";
    }

    return the_element.style.display;
}

function setInnerHTML(the_text, element_id)
{
    let dom_element = document.getElementById(element_id);
    dom_element.innerHTML = the_text;
    return true;
}

function setValue(the_value, element_id)
{
    let dom_element = document.getElementById(element_id);
    dom_element.value = the_value;
    return true;
}

