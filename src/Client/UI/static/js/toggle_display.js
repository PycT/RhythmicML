function toggle_display(dom_element_id, display = "flex")
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