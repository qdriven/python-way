var vizData = {};
var lineGraph = {};
var vizId = null;

window.onload = function(){
	vizId = document.location.search.split("=")[1];

	// creates the elements needed for the visualization with correct id's for usage throughout vizserve.
	initializeDocument();

	fetchConfig();
}

// Init the document for this visualization. For now assumes the presence of the parent error handler.
// Two panels are added: error_panel for displaying any errors that my occur, and a viz_panel for the visualization itself.
function initializeDocument(){
	var body = document.querySelector("#container");
	var fragment = document.createDocumentFragment();

	var error_panel = document.createElement("div");
	error_panel.classList = "hidden error_panel";
	error_panel.id = vizId + "_error_panel";
	fragment.appendChild(error_panel);

	var viz_panel = document.createElement("div");
	// for viz-panel, prefix the id, as an id with leading zero leads to issues with 
	// query selector
	viz_panel.id = "viz_panel_" + vizId;

	fragment.appendChild(viz_panel);

	body.appendChild(fragment);
}

function fetchConfig(){
	var request = new XMLHttpRequest();
	request.open('GET', parent.vizServeConfig.apiUrl + "/viz/" + vizId, true);

	request.onload = function(){
		if(request.status >= 200 && request.status < 400){
			vizData.config = JSON.parse(request.responseText);
			fetchData();
		}
	}

	request.onerror = function() {
	  // There was a connection error of some sort
		    parent.errorHandler.serverError(vizId + "_error_panel", "Network error, could not connect to server.")
	};

	try{
		request.send();
	} catch(e){
		parent.errorHandler.serverError(vizId + "_error_panel", "Network error, could not connect to server.")	
	}
}

function fetchData(){
	var request = new XMLHttpRequest();
	request.open('GET', parent.vizServeConfig.apiUrl + "/data/" + vizId, true);

	request.onload = function() {
	  if (request.status >= 200 && request.status < 400) {
	    // Success!
	    // TODO: hack by adding ['data']. This should be fixed in the db call, rather than here.
	    vizData.data = JSON.parse(request.responseText)['data'];

	    // TODO: add config in backend for the viz. i.e. axes etc.
	    vizData.config = {};
	    vizData.config.hor_axis = "x";
	    vizData.config.ver_axis = "y";
	    vizData.config.grid_lines = true;
		populateControls();
	    drawLineGraph();
	  } else {
	    // We reached our target server, but it returned an error
	    parent.errorHandler.serverError(vizId + "_error_panel", "Could not fetch data for this visualization")
	  }
	};

	request.onerror = function() {
	  // There was a connection error of some sort
		    parent.errorHandler.serverError(vizId + "_error_panel", "Network error, could not connect to server.")
	};

	try{
		request.send();
	} catch(e){
		parent.errorHandler.serverError(vizId + "_error_panel", "Network error, could not connect to server.")	
	}
}

// initial line graph drawing function, should only be used on first use.
// assumes data has been fetched and can be found in vizData.data
function drawLineGraph(){
	console.log(vizData);
	// TODO: inconsistent naming of axes. Should be referred to as either: hor and ver axis or x and y axis.
	// TODO: these sizes need to be relative to the size of the iframe to prevent scrolling
	lineGraph.margin = {top: 20, right: 20, bottom: 30, left: 50};
	lineGraph.width = 700 - lineGraph.margin.left - lineGraph.margin.right;
	lineGraph.height = 400 - lineGraph.margin.top - lineGraph.margin.bottom;
	// var margin = {top: 20, right: 20, bottom: 30, left: 50},
	//     width = 700 - margin.left - margin.right,
	//     height = 400 - margin.top - margin.bottom;

	// TODO: type of axis scale should be fetched from config, not hardcoded to linear.
	lineGraph.x = d3.scale.linear()
					.range([0, lineGraph.width])

	lineGraph.y = d3.scale.linear()
					.range([lineGraph.height, 0]);

	lineGraph.xAxis = d3.svg.axis()
						.scale(lineGraph.x)
						.orient("bottom");

	lineGraph.yAxis = d3.svg.axis()
						.scale(lineGraph.y)
						.orient("left");

	if(vizData.config.grid_lines){
		drawGridLines();
	}

	// TODO: should be possible to define multiple lines?
	lineGraph.line = d3.svg.line()
						.x(function(d) {return lineGraph.x(d[vizData.config.hor_axis]); })
						.y(function(d) {return lineGraph.y(d[vizData.config.ver_axis]); })

	lineGraph.svg = d3.select("#viz_panel_" + vizId).append("svg")
						.attr("width", lineGraph.width + lineGraph.margin.left + lineGraph.margin.right)
						.attr("height", lineGraph.height + lineGraph.margin.top + lineGraph.margin.right)
					.append("g")
					.attr("transform", "translate(" + lineGraph.margin.left + "," + lineGraph.margin.top + ")");

	lineGraph.x.domain(d3.extent(vizData.data, function(d){ return d[vizData.config.hor_axis]; }));
	lineGraph.y.domain(d3.extent(vizData.data, function(d){ return d[vizData.config.ver_axis]; }));


	// TODO: some hardcoded offset values here.
	lineGraph.svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + lineGraph.height + ")")
		.call(lineGraph.xAxis);
		// .append("text")
		// .attr("dy", "-.71em")
		// .attr("x", 650)
		// .attr("text-anchor", "end")
		// .text(vizData.config.hor_axis)
	// svg.append("g")
	// 	.attr("class", "x axis")
	// 	.attr("transform", "translate(0," + height + ")")
	// 	.call(xAxis)
	// 	.append("text")
	// 	.attr("dy", "-.71em")
	// 	.attr("x", 650)
	// 	.style("text-anchor","end")
	// 	.text("X");


	lineGraph.svg.append("g")
		.attr("class", "y axis")
		.call(lineGraph.yAxis);
		// .append("text")
		// .attr("transform", "rotate(-90)")
		// .attr("y", 6)
		// .attr("dy", ".71em")
		// .attr("text-anchor", "end")
		// .text(vizData.config.ver_axis)
	// svg.append("g")
	// 	.attr("class", "y axis")
	// 	.call(yAxis)
	// 	.append("text")
	// 	.attr("transform", "rotate(-90)")
	// 	.attr("y", 6)
	// 	.attr("dy", ".71em")
	// 	.style("text-anchor", "end")
	// 	.text("y");

	lineGraph.svg.append("path")
		.datum(vizData.data)
		.attr("class", "line")
		.attr("d", lineGraph.line);
}

function updateLineGraph(){
	var localSvg = lineGraph.svg.transition()

	lineGraph.x = d3.scale.linear()
			.range([0, lineGraph.width])

	lineGraph.y = d3.scale.linear()
					.range([lineGraph.height, 0]);


	lineGraph.xAxis = d3.svg.axis()
						.scale(lineGraph.x)
						.orient("bottom");

	lineGraph.yAxis = d3.svg.axis()
						.scale(lineGraph.y)
						.orient("left");

	if(vizData.config.grid_lines){
		drawGridLines();
	}

	// TODO: should be possible to define multiple lines?
	lineGraph.line = d3.svg.line()
						.x(function(d) {return lineGraph.x(d[vizData.config.hor_axis]); })
						.y(function(d) {return lineGraph.y(d[vizData.config.ver_axis]); })
	lineGraph.x.domain(d3.extent(vizData.data, function(d){ return d[vizData.config.hor_axis]; }));
	lineGraph.y.domain(d3.extent(vizData.data, function(d){ return d[vizData.config.ver_axis]; }));


	// TODO: some hardcoded offset values here.
	localSvg.select(".x.axis")
				.duration(750)
				.call(lineGraph.xAxis);
	localSvg.select(".y.axis")
				.duration(750)
				.call(lineGraph.yAxis);
	lineGraph.svg.select("path.line").remove()
	lineGraph.svg.append("path")
		.datum(vizData.data)
		.attr("class", "line")
		.attr("d", lineGraph.line);

	// lineGraph.svg.append("g")
	// 	.attr("class", "x axis")
	// 	.attr("transform", "translate(0," + lineGraph.height + ")")
	// 	.call(lineGraph.xAxis)
	// 	.append("text")
	// 	.attr("dy", "-.71em")
	// 	.attr("x", 650)
	// 	.attr("text-anchor", "end")
	// 	.text(vizData.config.hor_axis)


	// lineGraph.svg.append("g")
	// 	.attr("class", "y axis")
	// 	.call(lineGraph.yAxis)
	// 	.append("text")
	// 	.attr("transform", "rotate(-90)")
	// 	.attr("y", 6)
	// 	.attr("dy", ".71em")
	// 	.attr("text-anchor", "end")
	// 	.text(vizData.config.ver_axis)

	// lineGraph.svg.append("path")
	// 	.datum(vizData.data)
	// 	.attr("class", "line")
	// 	.attr("d", lineGraph.line);

}

function drawGridLines(){
	lineGraph.xAxis
		.innerTickSize(-lineGraph.height)
		.outerTickSize(0)
		.tickPadding(10);

	lineGraph.yAxis
		.innerTickSize(-lineGraph.width)
		.outerTickSize(0)
		.tickPadding(10);
}

function populateControls(){
	// this function is called once data has been fetched. The idea is that the control elements should be populated with sensible values/options given the input data.
	var hor_axis_select = document.getElementById("control_hor_axis");
	var ver_axis_select = document.getElementById("control_ver_axis");

	// for both dropdowns the same axes should be available.
	
	var options = Object.keys(vizData.data[0]);

	var fragment = document.createDocumentFragment();
	var option;
	for (var i = options.length - 1; i >= 0; i--) {
		option = document.createElement("option");
		option.value = options[i];
		option.innerHTML = options[i];
		fragment.appendChild(option);
	}
	var fragment_copy = fragment.cloneNode(true);

	ver_axis_select.appendChild(fragment);
	hor_axis_select.appendChild(fragment_copy);

	// set the value to the current config value.
	ver_axis_select.value = vizData.config.ver_axis;
	hor_axis_select.value = vizData.config.hor_axis;

	document.getElementById("control_grid").checked = vizData.config.grid_lines;

	initializeControlListeners();
}

function initializeControlListeners(){
	document.getElementById("control_hor_axis").addEventListener("change", function(){
		vizData.config.hor_axis = this.value;
		updateLineGraph();
	});
	document.getElementById("control_ver_axis").addEventListener("change", function(){
		vizData.config.ver_axis = this.value;
		updateLineGraph();
	});

	document.getElementById("control_grid").addEventListener("change", function(){
		vizData.config.grid_lines = this.checked;
		updateLineGraph();
	});
}
