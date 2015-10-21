function insertPixels(column_id, x, y) { 
	  var body = document.getElementById(column_id);
	  var canvas     = document.createElement("table");
	  var canvasBody = document.createElement("tbody");

	  for (var i = 0; i < x; i++)
	  {
	    var row = document.createElement("tr");
	    for (var j = 0; j < y; j++) 
	    {
	      var cell = document.createElement("td");
	      var cellText = document.createTextNode("");
	      cell.appendChild(cellText);
	      row.appendChild(cell);
	    }
	    canvasBody.appendChild(row);
	  }
	  canvas.appendChild(canvasBody);
	  body.appendChild(canvas);

}

function paintCell(cell) {
	if(painting) 
	{
    	cell.style.backgroundColor = "white";
	}
	else if(erasing) {
		cell.style.backgroundColor = "#111";
	}
}

function getCanvasValues() {
	var result = "";
	for (var i = 0; i < canvas.rows.length; i++) 
    {
    	for (var j = 0; j < canvas.rows[i].cells.length; j++)
    	{
	        var color = canvas.rows[i].cells[j].style.backgroundColor;
	        switch(color)
	        {
	        	case "white": result += "1"; break;
	        	default: result += "0"; 
	        }
    	}
    }
    return result;
}

function predict() {
    results = getCanvasValues();

    $.post("recognizer/",
    {
        data: results
    },
    function(data, status){
    	var result = document.getElementById("resultsField");
        result.innerHTML = ("<h4> I predict it is: " + data + "</h4>");
    });
}

function eraseCanvas() {
	for (var i = 0; i < canvas.rows.length; i++) 
    {
    	for (var j = 0; j < canvas.rows[i].cells.length; j++)
	        canvas.rows[i].cells[j].style.backgroundColor = "#111";
    }
    var result = document.getElementById("resultsField");
    result.innerHTML = "";
}

function setUpMouseControl() {
	if (canvas != null) 
	{
	    for (var i = 0; i < canvas.rows.length; i++) 
	    {
	    for (var j = 0; j < canvas.rows[i].cells.length; j++)
	        canvas.rows[i].cells[j].onmouseover = function () 
		    {
		        paintCell(this); 
		    };
	    }
	}

	canvas.onmousedown = function(event) 
	{
	    switch (event.which) {
	        case 1:
	            painting = true;
	            break;
	        case 3:
	            erasing = true;
	            break;
	        default:
	            console.log('You have a strange Mouse!');
	    }
	    return false;
	};
	canvas.onmouseup = function() 
	{ 
		painting = false; 
		erasing = false;
	};

	canvas.oncontextmenu = function() {
		return false;
	};
}

var painting = false;
var erasing = false;
var httpRequest;
insertPixels("pixels", 20, 20);
var canvas = document.getElementsByTagName("table")[0];
setUpMouseControl();