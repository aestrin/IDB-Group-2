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
