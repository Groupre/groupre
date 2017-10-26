	
$(document).ready(function() {

	function StatsProcessor() {	
		var newStats = new Stats();
		//Call Methods
		newStats.init();	
		newStats.processLine();	
		newStats.collectStats();
		//Update View
		updateDom();
	};

	//Create Stats class
	var Stats = function(inputData){
		this.inputData = inputData;
		this.dataCount = dataCount;
	
	};
	
	// initialize and set all to int
	Stats.prototype.init = function(){

		// // Format data
		// for (i = 0; i < data.length; i++) {		
		// 	data[i] = data[i].filter(Number)		
		// 	data[i] = data[i].map(function (x) { 
		// 		return parseInt(x, 10); 
		// 	});
		// }
		
		//Set default values
		inputData = [];	
		dataCount = 0;				
	};

	// 	processLine method - create array to store length value of each row
	Stats.prototype.processLine = function() {
		
		rowLength = [];
	
		for (i = 0; i < data.length; i++) { 		
			var rowDataLength = data[i].length;
			rowLength.push(rowDataLength);						
		}	
	};

	// Calculate and output the required statistics
	Stats.prototype.collectStats = function() {

		// Combine all data into single arrays
		mergedData = [].concat.apply([], data);;		
			
	};

	//Update DOM with stat values
	var updateDom = function() {
		function viewModel() {
			this.doAnalysisThingy = ko.observable(dataCount);
			
		};
		ko.applyBindings(new viewModel()); 
	};

	//File Upload

	// Confirm browser supports HTML5 File API
	var browserSupportFileUpload = function() {
		var isCompatible = false;
		if(window.File && window.FileReader && window.FileList && window.Blob) {
			isCompatible = true;
		}
		return isCompatible;
	};

	// Upload selected file and create array
	var uploadFile = function(evt) {
		var file = evt.target.files[0];
		var reader = new FileReader();
		reader.readAsText(file);
		reader.onload = function(event) {
			//Jquery.csv
			createArray($.csv.toArrays(event.target.result));			
		};
	};

	// Validate file import
	var createArray = function(data) {	
		if(data !== null && data !== "" && data.length > 1) {
			this.data = data;
			doAnalysisThingy(data);
			$("#statOutPut").removeClass( "hidden" );			
			$("#errorOutPut").addClass( "hidden" );			
		} else {
			$("#errorOutPut").removeClass( "hidden" );
			$("#statOutPut").addClass( "hidden" );
			$("#errorOutPut li").html('There is no data to import');	
		}	
	};
	
	// event listener for file upload
	if (browserSupportFileUpload()) {
			document.getElementById('txtFileUpload').addEventListener('change', uploadFile, false);
		} else {
			$("#introHeader").html('The File APIs is not fully supported in this browser. Please use another browser.');
		}	
});