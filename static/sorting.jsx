
dir = 1;

function setDir(newdir)
{
    var change = (dir != newdir);
    dir = newdir;
    if(lastAttr != null && change)
        sortBy(lastAttr, lastList)
}

lastAttr = null
lastList = null

function sortBy(attr, list)
{
    lastAttr = attr;
    lastList = list;
    // sort
    var cmp = function(a, b) {
        if((isNaN(a[attr]) || isNaN(b[attr])))
            return dir * (a[attr] > b[attr]);
        else
            return dir * (parseInt(a[attr]) - parseInt(b[attr]));
    };
    
    list.sort(cmp);

    // update element
    document.getElementById("grid_location").innerHTML="";


    renderTable(buildModels(list, false), document.getElementById("grid_location"), 2);
}