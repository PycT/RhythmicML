"use strict";

//general manipulations with DOM elements

function popElement(dom_element_id)
{
    if (typeof window.elements_listened == "undefined")
    {
        window.elements_listened = [];
        window.elements_listened_ids = [];
    }

    var element_index = elements_listened_ids.indexOf(dom_element_id);
    var element_instance;

    if (element_index == -1)
    {
        element_instance = document.getElementById(dom_element_id);
        window.elements_listened.push(element_instance);
        window.elements_listened_ids.push(dom_element_id);
    }
    else
    {
        element_instance = window.elements_listened[element_index];
    }

    return element_instance;
}

function toggleDisplay(dom_element_id, display = "flex")
{
    var the_element = popElement(dom_element_id);

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
    var the_element = popElement(dom_element_id);

    the_element.style.display = display;

    return the_element.style.display;
}

function setInvisible(dom_element_id)
{
    var the_element = popElement(dom_element_id);

    the_element.style.display = "none";

    return the_element.style.display;
}

function inputValueHasChanged(dom_element_id, initial_value)
{
    var the_input = popElement(dom_element_id);

    if (the_input.value == initial_value)
    {
        return false;
    }

    return true;
}

function elementIsDisabled(dom_element_id)
{
    var the_element = popElement(dom_element_id);

    return the_element.disabled;
}

function enableElement(dom_element_id)
{
    var the_element = popElement(dom_element_id);
    the_element.disabled = false;
    return true;
}

function disableElement(dom_element_id)
{
    var the_element = popElement(dom_element_id);
    the_element.disabled = true;
    return true;
}