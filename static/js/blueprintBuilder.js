// Courtesy of https://dan.forys.uk/experiments/mesmerizer/

// NOTE Similar in design to the template builder. Will allow user to create a room blueprint and specify locked-in attributes such as aisle chairs, room layout, and the like.

// TODO Add dimension editing (X/Y sizes for the grid).
// TODO Add JSON saving formatter and automatic attribute allocation based on room front and given chair attributes.
// TODO Add way to specify room front, or make it permanently in one location (likely the bottom side).

// Main portion of canvas setup.
$(document).ready(function () {
	pixelCanvas = $('#blueprintBuilder');
	canvasContext = document.getElementById('blueprintBuilder').getContext('2d');
	row = new Array;
	blocks = new Array;
	blocksSequence = new Array;
	targetColor = new Color(255, 0, 0);
	colToUse = new Color(222, 222, 222);
	baseColor = new Color(255, 255, 255);
	spirals = Array();
	lastX = -1; // Last hit coords
	lastY = -1;
	colorMode = true;
	animators = Array();
	message = '';
	originX = 0; // 350 is default
	originY = 0; // 350 is default

	grid = new Grid;
	grid.init();

	selectedBlocks = [];

	renameMode = false;

	var mouseIsDown = false;

	isDown = false;

	mouseOffset = 0; // was 102 now is 0

	// Below functions mainly deal with input via mouse and keyboard for selection and actions taken on canvas grid.
	pixelCanvas.mousedown(function (e) {
		console.log('down');

		e.stopPropagation();
		e.preventDefault();
		var x = e.pageX - $(this).offset().left - mouseOffset;
		var y = e.pageY - $(this).offset().top - mouseOffset;
		mouseX = Math.floor(x / grid.totalBlockWidth);
		mouseY = Math.floor(y / grid.totalBlockWidth);

		// Put your mousedown stuff here.
		startX = mouseX;
		startY = mouseY;
		isDown = true;
	});

	pixelCanvas.mouseup(function (e) {
		console.log('up');

		e.stopPropagation();
		e.preventDefault();
		var x = e.pageX - $(this).offset().left - mouseOffset;
		var y = e.pageY - $(this).offset().top - mouseOffset;
		mouseX = Math.floor(x / grid.totalBlockWidth);
		mouseY = Math.floor(y / grid.totalBlockWidth);

		// Put your mouseup stuff here.
		isDown = false;
		console.log('x1: ' + startX + ', y1: ' + startY + ', x2: ' + mouseX + ', y2: ' + mouseY);
		topLeftX = Math.min(startX, mouseX);
		topLeftY = Math.min(startY, mouseY);
		botRightX = Math.max(startX, mouseX);
		botRightY = Math.max(startY, mouseY);
		var xRange = botRightX - topLeftX;
		var yRange = botRightY - topLeftY;

		// Clear past selection.
		selectedBlocks.forEach(function (item, index, array) {
			item.unselect();
		});
		selectedBlocks = [];

		// Do our click.
		for (var i = topLeftY; i <= botRightY; i++) {
			// i = Y = row
			for (var j = topLeftX; j <= botRightX; j++) {
				// j = X = col
				grid.blocks[i][j].handleClick();
			}
		}
	});

	pixelCanvas.mousemove(function (e) {
		console.log('move');

		if (!isDown) return;

		e.stopPropagation();
		e.preventDefault();
		var x = e.pageX - $(this).offset().left - mouseOffset;
		var y = e.pageY - $(this).offset().top - mouseOffset;
		mouseX = Math.floor(x / grid.totalBlockWidth);
		mouseY = Math.floor(y / grid.totalBlockWidth);

		// Put your mousemove stuff here.
		topLeftX = Math.min(startX, mouseX);
		topLeftY = Math.min(startY, mouseY);
		botRightX = Math.max(startX, mouseX);
		botRightY = Math.max(startY, mouseY);
		var xRange = botRightX - topLeftX;
		var yRange = botRightY - topLeftY;
		for (var i = topLeftY; i <= botRightY; i++) {
			// i = Y = row
			for (var j = topLeftX; j <= botRightX; j++) {
				// j = X = col
				grid.blocks[i][j].hit();
			}
		}
	});

	pixelCanvas.mouseout(function (e) {
		console.log('out');
	});

	$(document).keypress(function (e) {
		console.log("keycode pressed: " + e.keyCode);

		// r is 114 - Rename
		if (e.keyCode == 114) {
			renameMode = true;
		} else {
			renameMode = false;
		}

		// Send keypress to each selected block.
		selectedBlocks.forEach(function (item, index, array) {
			item.sendKeypress(e);
		});
	})

	// NOTE keydown and keyup seem to not be active, at least in Chrome.
	// As such, getting information such as whether shift is held down or not may not be possible.

	t = setInterval('tick()', 30);
});

function autoAdd(num) {
	for (index = 0; index < num; index++) {
		blockNum = rand(grid.blocksSequence.length);
		grid.blocksSequence[blockNum].hit();
	}
}

function tick() {
	if (typeof gridRotate == 'undefined') gridRotate = 0;
	canvasContext.clearRect(0, 0, 700, 700);
	canvasContext.save();
	canvasContext.translate(350, 350);
	if (gridRotate > 0) {
		canvasContext.rotate((Math.PI / 180) * gridRotate);
		gridRotate += 0.2;
		if (gridRotate > 360) gridRotate = 0;
	}

	for (block = 0; block < grid.blocksSequence.length; block++) {
		grid.blocksSequence[block].magic();
		grid.blocksSequence[block].draw();
	}
	canvasContext.restore();
}

function averageColors(col1, col2) {
	newCol = new Color;
	if (col1.r < col2.r) newCol.r = col1.r + 1;
	else if (col1.r > col2.r) newCol.r = col1.r - 1;
	else newCol.r = col1.r;

	if (col1.g < col2.g) newCol.g = col1.g + 1;
	else if (col1.g > col2.g) newCol.g = col1.g - 1;
	else newCol.g = col1.g;

	if (col1.b < col2.b) newCol.b = col1.b + 1;
	else if (col1.b > col2.b) newCol.b = col1.b - 1;
	else newCol.b = col1.b;

	return newCol;
}

function rand(n) {
	return (Math.floor(Math.random() * n));
}

// Primary piece of representation in the grid.
function Block(context, x, y, grid) {
	this.neighbours = Array();
	// this.color = getColor();
	this.color = new Color(0, 0, 0)
	this.nextColor = this.color;
	this.ink = 0;
	this.lastSizeDiff = 0;
	this.x = x;
	this.y = y;
	this.ctx = context;
	this.rotate = 0;
	this.grid = grid;
	this.xPixels = x * grid.totalBlockWidth;
	this.yPixels = y * grid.totalBlockWidth;
	this.baseColor = new Color(0, 0, 0);

	// For Chairs
	this.notAChair = false;
	this.aisle = false;
	this.leftHanded = false;
	this.acceptingInput = false;
	this.selected = false;

	console.log('x:', this.x, 'y:', this.y);

	this.label;
	this.bareLabel;
	if (this.x == 0 && this.y == 0) {
		this.bareLabel = '';
		this.label = '';
	} else if (this.x == 0) {
		this.bareLabel = this.y;
		this.label = 'r: ' + this.bareLabel;
	} else if (this.y == 0) {
		this.bareLabel = this.x;
		this.label = 'c: ' + this.bareLabel;
	} else {
		var xLabel = this.x;
		var yLabel = this.y;
		this.bareLabel = '(' + xLabel + ',' + yLabel + ')';
		this.label = '(' + xLabel + ',' + yLabel + ')';
	}

	this.setNeighbours = function (neighbours) {
		this.neighbours = neighbours;
	}

	this.setColor = function (newCol) {
		this.color.r = newCol.r;
		this.color.g = newCol.g;
		this.color.b = newCol.b;
	}

	this.setBaseColor = function (newCol) {
		this.baseColor.r = newCol.r;
		this.baseColor.g = newCol.g;
		this.baseColor.b = newCol.b;
	}

	this.magic = function () {
		this.setColor(this.nextColor);

		// Work out which neighbour has the most ink
		var bestNeighbour = this.neighbours[0];
		for (index = 1; index < this.neighbours.length; index++) {
			if (this.neighbours[index].ink > bestNeighbour.ink) bestNeighbour = this.neighbours[index];
		}

		// Only do something if the best neighbour has more ink than me
		if (bestNeighbour.ink > this.ink && bestNeighbour.ink > 1) {
			this.setColor(averageColors(this.color, bestNeighbour.color));
			this.ink = Math.round(bestNeighbour.ink * 0.7);
			bestNeighbour.ink = bestNeighbour.ink - Math.round(this.ink / 50);
			if (bestNeighbour.ink < 0) bestNeighbour.ink = 0;
		} else if (this.ink > 0) this.ink--;

		// If the ink is 0, return to white
		if (this.ink == 0) this.setColor(averageColors(this.color, this.baseColor));

		// Change the size of the el
		sizeDiff = Math.round(15 * (this.ink / this.grid.maxInk));
		this.lastSizeDiff = sizeDiff;
	}

	this.draw = function () {
		var ctx = this.ctx;

		borderColor = new Color(this.color.r, this.color.g, this.color.b);
		borderColor.add(20);

		ctx.fillStyle = this.color.toRgba(1);
		ctx.strokeStyle = 'rgba(255,255,255, 0.2)';

		ctx.save();

		// NOTE Change offset to remove margin.
		// was 248 now is 350

		ctx.translate((this.xPixels) + this.grid.halfBlockWidth - 350, (this.yPixels) + this.grid.halfBlockWidth - 350);
		if (this.rotate > 0) ctx.rotate((Math.PI / 180) * this.rotate);
		ctx.fillRect(-this.grid.halfBlockWidth, -this.grid.halfBlockWidth, this.grid.blockWidth, this.grid.blockWidth);

		sizeDiff = Math.round((Math.floor(this.grid.blockWidth / 2)) * (this.ink / this.grid.maxInk));

		ctx.lineWidth = sizeDiff;

		if (sizeDiff > 0) ctx.strokeRect(-this.grid.halfBlockWidth + (sizeDiff / 2), -this.grid.halfBlockWidth + (sizeDiff / 2), this.grid.blockWidth - (sizeDiff), this.grid.blockWidth - (sizeDiff));
		if (this.rotate > 0) this.rotate += 10;
		if (this.rotate > 90) this.rotate = 0;

		// Text will be inverse of block color.
		inverseHex = rgbToHex(255 - this.baseColor.r, 255 - this.baseColor.g, 255 - this.baseColor.b);
		ctx.lineWidth = 1;
		// ctx.fillStyle = '#CC00FF';
		ctx.fillStyle = inverseHex;
		ctx.lineStyle = '#ffff00';
		ctx.font = '18px sans-serif';
		ctx.textAlign = 'center';

		labelText = this.label;

		ctx.fillText(labelText, 0, -(this.grid.halfBlockWidth / 3));

		infoText = '';
		if (this.notAChair) {
			infoText += 'NaC';
		}
		if (this.leftHanded) {
			infoText += 'L';
		}
		if (this.aisle) {
			infoText += 'A';
		}

		ctx.fillText(infoText, 0, 2 * this.grid.halfBlockWidth / 3);

		ctx.restore();
	}

	this.hit = function () {
		this.setColor(new Color(102, 204, 255)); // Light-blue for selection?
	}

	this.unhit = function () {
		this.setColor(this.baseColor);
	}

	this.toggleNotAChair = function () {
		this.notAChair = !this.notAChair;
		this.handleAppearance();
	}

	this.toggleLeftHanded = function () {
		this.leftHanded = !this.leftHanded;

		if (!this.leftHanded) {} else {
			this.aisle = false;
		}

		this.handleAppearance();
	}

	this.toggleAisle = function () {
		this.aisle = !this.aisle;

		if (!this.aisle) {} else {
			this.leftHanded = false;
			this.notAChair = false;
		}

		this.handleAppearance();
	}

	this.sendKeypress = function (e) {
		// x is 120 - NaC (Not a Chair) - In this context, we will make the chair not exist, rather than forbid it.
		// l is 108 - left-handed
		// a is 97 - aisle

		switch (e.keyCode) {
			case 120: // NaC (Not a Chair)
				this.toggleNotAChair();
				break;
			case 108: // left-handed
				this.toggleLeftHanded();
				break;
			case 97: // aisle
				this.toggleAisle();
				break;
			default:
				break;
		}
	}

	this.select = function () {
		this.selected = true;
		this.handleAppearance();

		selectedBlocks.push(this);
	}

	this.unselect = function () {
		this.selected = false;
		this.handleAppearance();
	}

	this.handleClick = function () {
		if (this.x == 0 || this.y == 0) {
			// A column or row identifier was clicked, or we are at the top left corner.
			if (this.x == 0 && this.y == 0) {
				// Corner.
			} else if (this.x == 0) {
				// Row.
				this.rowClick();
			} else {
				// Column.
				this.columnClick();
			}
		} else {
			// We are clicking on a chair-slot.
			this.standardClick();
		}
	}

	this.handleAppearance = function () {
		if (this.selected) {
			this.setBaseColor(new Color(0, 0, 255));
			this.setColor(new Color(0, 0, 255));
		} else if (this.notAChair) {
			this.setBaseColor(new Color(255, 255, 255));
			this.setColor(new Color(255, 255, 255));
		} else if (this.aisle) {
			this.setBaseColor(new Color(0, 255, 0));
			this.setColor(new Color(0, 255, 0));
		} else if (this.leftHanded) {
			this.setBaseColor(new Color(255, 0, 0));
			this.setColor(new Color(255, 0, 0));
		} else if (this.acceptingInput) {
			this.setBaseColor(new Color(255, 255, 102));
			this.setColor(new Color(255, 255, 102));
		} else {
			this.setBaseColor(new Color(0, 0, 0));
			this.setColor(new Color(0, 0, 0));
		}
	}

	this.standardClick = function () {
		this.select();
	}

	this.rowClick = function () {
		if (renameMode) {
			this.acceptingInput = true;
			this.handleAppearance();

			var input = prompt("Please enter the label you'd like to use for this row.", this.y);
			this.bareLabel = input;
			this.label = 'r: ' + this.bareLabel;

			this.acceptingInput = false;
			this.handleAppearance();

			for (let block of grid.blocks[this.y]) {
				block.updateLabel();
			}
		} else {
			for (let block of grid.blocks[this.y]) {
				block.select();
			}
		}
	}

	this.columnClick = function () {
		if (renameMode) {
			this.acceptingInput = true;
			this.handleAppearance();

			var input = prompt("Please enter the label you'd like to use for this column.", this.x);
			this.bareLabel = input;
			this.label = 'c: ' + this.bareLabel;

			this.acceptingInput = false;
			this.handleAppearance();

			for (let row of grid.blocks) {
				row[this.x].updateLabel();
			}
		} else {
			for (let row of grid.blocks) {
				row[this.x].select();
			}
		}
	}

	this.updateLabel = function () {
		if (this.x == 0 || this.y == 0) return;

		var xLabel = grid.blocks[this.y][0].bareLabel;
		var yLabel = grid.blocks[0][this.x].bareLabel;
		this.bareLabel = '' + xLabel + yLabel;
		this.label = '(' + xLabel + ',' + yLabel + ')';
	}
}

function Color(r, g, b) {
	this.r = r;
	this.g = g;
	this.b = b;

	this.add = function (num) {
		this.r += num;
		this.g += num;
		this.b += num;
		if (this.r > 255) r = 255;
		if (this.g > 255) g = 255;
		if (this.b > 255) b = 255;
	}

	this.toRgba = function (alpha) {
		return 'rgba(' + this.r + ', ' + this.g + ', ' + this.b + ', ' + alpha + ')';
	}
}

function getColor() {
	if (colorMode) {
		if (colToUse.r == targetColor.r && colToUse.g == targetColor.g && colToUse.b == targetColor.b) targetColor = new Color(rand(255), rand(255), rand(255));
		colToUse = averageColors(colToUse, targetColor);
	} else colToUse = new Color(rand(255), rand(255), rand(255));
	return colToUse;
}

// Contains Blocks within canvas.
function Grid() {
	this.rows = 32;
	this.cols = 32;
	this.blockWidth = 50;
	this.blockSpacing = 1;
	this.maxInk = 200;
	this.blocks = Array();
	this.blocksSequence = Array();
	var canvasContext = document.getElementById('blueprintBuilder').getContext('2d');

	// Do some maths to speed up the calculations later
	this.totalBlockWidth = this.blockWidth + this.blockSpacing;
	this.halfBlockWidth = Math.floor(this.totalBlockWidth / 2);

	// NOTE Resizing based on this seems to break centering?
	canvasContext.canvas.width = this.totalBlockWidth * this.cols;
	canvasContext.canvas.height = this.totalBlockWidth * this.rows;

	this.init = function () {
		// initialise the blocks
		for (rows = 0; rows < this.rows; rows++) {
			row = new Array;
			for (cols = 0; cols < this.cols; cols++) {
				row[cols] = new Block(canvasContext, cols, rows, this);
			}
			this.blocks[rows] = row;
		}

		// Loop through all the blocks and assign neighbours
		for (rows = 0; rows < this.rows; rows++) {
			for (cols = 0; cols < this.cols; cols++) {
				neighbours = Array();
				if (cols < (this.cols - 2)) {
					neighbours.push(this.blocks[rows][cols + 1]);
				}
				if (rows < (this.rows - 2)) {
					neighbours.push(this.blocks[rows + 1][cols]);
				}
				if (cols > 0) {
					neighbours.push(this.blocks[rows][cols - 1]);
				}
				if (rows > 0) {
					neighbours.push(this.blocks[rows - 1][cols]);
				}
				this.blocks[rows][cols].setNeighbours(neighbours);
				this.blocksSequence.push(this.blocks[rows][cols]);
			}
		}
	}
}

function fadeText() {
	$('.fade').fadeTo('slow', 0);
}

var t = setTimeout('fadeText()', 10000);

function rgbToHex(r, g, b) {
	return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function componentToHex(c) {
	var hex = c.toString(16);
	return hex.length == 1 ? "0" + hex : hex;
}
