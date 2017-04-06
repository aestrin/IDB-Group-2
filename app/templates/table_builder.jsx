var size = 6;

function load(error, response)
{
    if(error == null)
    {
        console.log(response);
        document.getElementById("grid_location").innerHTML = "";
        size = response.length;
        renderTable(buildModels(response, true), document.getElementById("grid_location"), 3);
    }
}

// common code
var filter = null;
var filterBy = null;
var sort = null;
var up = 1;
var page = 1;

function buildURL()
{
    var url = baseUrl;
    url += "?page="+page;
    if(filter != null)
        url += "&filterBy="+filterBy+"&filter="+filter;
    if(sort != null)
    {
        if(up)
            url +="&sortUp="+sort;
        else
            url +="&sortDown="+sort;
    }
    url += "&raw";

    console.log(url);
    return url;
}

function reload()
{
    var url = buildURL();
    var req = new XMLHttpRequest();
    req.open('GET', url, true);
    req.responseType = 'json';
    req.onload = function() {
      var status = req.status;
      if (status == 200) {
        load(null, req.response);
      } else {
        load(status);
      }
    };
    req.send();
}

function sortBy(value)
{
    sort = value;
    page = 1;
    reload();
}

function sortDir(value)
{
    up = value;
    page = 1;
    reload();
}

function nextPage()
{
    page += 1;
    reload();
}

function prevPage()
{
    if(page != 1)
        page -= 1;
    reload();
}

function filterPage(filtBy, filt)
{
    filterBy = filtBy;
    filter = filt;
    page = 1;
    reload();
}

function GenericList(props) {
    var list = props.list;
    var listItems = list.map((ele) => <li>{ele}</li>);
    return (<ul>{listItems}</ul>);
}

function RefList(props) {
    var list = props.list;

    var listItems = list.map((ele) => <li><a href={"/"+props.reftype+"/"+ele.index}>{ele.description}</a></li>);
    return (<ul>{listItems}</ul>);
}

var panelPicStyle = {width: '600px', height: '300px',padding:'20px', 'padding-bottom': '0px'};

function PanelNode(props){
    <div style={s = {padding: '20px', height: '100%',}}>
        <div className = {"panel panel-default"} style={s = {height: '100%',}}>
                    <div className = {"panel-content"}>
                        {props.displayElement}
                    </div>
        </div>
    </div>
}

function renderTable(list, container, columns) {
    var blocks = [];
    for(i = 0; i < list.length; i++)
    {
        blocks.push(<div className={"col-md-"+Math.floor(12/columns)} id={"ele"+i}>{list[i]}</div>);
    }
    console.log(blocks);
    for(i = 0; i < list.length; i+=columns)
    {
        var row = document.createElement("div");
        row.id = "row"+i;
        container.appendChild(row);
        ReactDOM.render(<div><div className={"row"}>{blocks.slice(i, i+columns)}</div></div>, row);
        // resize to fit row
        console.log(row.offsetHeight);
        for(x = i; x < i+columns; x++)
        {
            if(x<list.length)
            {
                document.getElementById("ele"+x).setAttribute("style","height:"+row.offsetHeight+"px");
            }
        }
    }
}
