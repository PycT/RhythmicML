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

function setVisible(dom_element_id, display = "flex")
{
    var the_element = document.getElementById(dom_element_id);

    the_element.style.display = display;

    return the_element.style.display;
}

function setInvisible(dom_element_id)
{
    var the_element = document.getElementById(dom_element_id);

    the_element.style.display = "none";

    return the_element.style.display;
}
