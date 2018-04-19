// Courtesy of http://interactjs.io/

// Dragging
// target elements with the "draggable" class
interact('.draggable')
	.draggable({
		// enable inertial throwing
		inertia: true,
		// keep the element within the area of it's parent
		restrict: {
			restriction: "parent",
			endOnly: true,
			elementRect: {
				top: 0,
				left: 0,
				bottom: 1,
				right: 1
			}
		},
		// enable autoScroll
		autoScroll: true,

		// call this function on every dragmove event
		onmove: dragMoveListener,
		// call this function on every dragend event
		onend: function (event) {
			var textEl = event.target.querySelector('p');

			textEl && (textEl.textContent =
				'moved a distance of ' +
				(Math.sqrt(Math.pow(event.pageX - event.x0, 2) +
					Math.pow(event.pageY - event.y0, 2) | 0))
				.toFixed(2) + 'px');
		}
	});

function dragMoveListener(event) {
	var target = event.target,
		// keep the dragged position in the data-x/data-y attributes
		x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
		y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

	// translate the element
	target.style.webkitTransform =
		target.style.transform =
		'translate(' + x + 'px, ' + y + 'px)';

	// update the posiion attributes
	target.setAttribute('data-x', x);
	target.setAttribute('data-y', y);
}

// this is used later in the resizing and gesture demos
window.dragMoveListener = dragMoveListener;

// Drag and drop
/* The dragging code for '.draggable' from the demo above
 * applies to this demo as well so it doesn't have to be repeated. */

// enable draggables to be dropped into this
interact('.dropzone').dropzone({
	// only accept elements matching this CSS selector
	accept: '#yes-drop',
	// Require a 75% element overlap for a drop to be possible
	overlap: 0.75,

	// listen for drop related events:

	ondropactivate: function (event) {
		// add active dropzone feedback
		event.target.classList.add('drop-active');
	},
	ondragenter: function (event) {
		var draggableElement = event.relatedTarget,
			dropzoneElement = event.target;

		// feedback the possibility of a drop
		dropzoneElement.classList.add('drop-target');
		draggableElement.classList.add('can-drop');
		draggableElement.textContent = 'Dragged in';
	},
	ondragleave: function (event) {
		// remove the drop feedback style
		event.target.classList.remove('drop-target');
		event.relatedTarget.classList.remove('can-drop');
		event.relatedTarget.textContent = 'Dragged out';
	},
	ondrop: function (event) {
		event.relatedTarget.textContent = 'Dropped';
	},
	ondropdeactivate: function (event) {
		// remove active dropzone feedback
		event.target.classList.remove('drop-active');
		event.target.classList.remove('drop-target');
	}
});

// Snapping
var element = document.getElementById('grid-snap'),
	x = 0,
	y = 0;

interact(element)
	.draggable({
		snap: {
			targets: [
				interact.createSnapGrid({
					x: 30,
					y: 30
				})
			],
			range: Infinity,
			relativePoints: [{
				x: 0,
				y: 0
			}]
		},
		inertia: true,
		restrict: {
			restriction: element.parentNode,
			elementRect: {
				top: 0,
				left: 0,
				bottom: 1,
				right: 1
			},
			endOnly: true
		}
	})
	.on('dragmove', function (event) {
		x += event.dx;
		y += event.dy;

		event.target.style.webkitTransform =
			event.target.style.transform =
			'translate(' + x + 'px, ' + y + 'px)';
	});

// Resizing
interact('.resize-drag')
	.draggable({
		onmove: window.dragMoveListener,
		restrict: {
			restriction: 'parent',
			elementRect: {
				top: 0,
				left: 0,
				bottom: 1,
				right: 1
			}
		},
	})
	.resizable({
		// resize from all edges and corners
		edges: {
			left: true,
			right: true,
			bottom: true,
			top: true
		},

		// keep the edges inside the parent
		restrictEdges: {
			outer: 'parent',
			endOnly: true,
		},

		// minimum size
		restrictSize: {
			min: {
				width: 100,
				height: 50
			},
		},

		inertia: true,
	})
	.on('resizemove', function (event) {
		var target = event.target,
			x = (parseFloat(target.getAttribute('data-x')) || 0),
			y = (parseFloat(target.getAttribute('data-y')) || 0);

		// update the element's style
		target.style.width = event.rect.width + 'px';
		target.style.height = event.rect.height + 'px';

		// translate when resizing from top or left edges
		x += event.deltaRect.left;
		y += event.deltaRect.top;

		target.style.webkitTransform = target.style.transform =
			'translate(' + x + 'px,' + y + 'px)';

		target.setAttribute('data-x', x);
		target.setAttribute('data-y', y);
		target.textContent = Math.round(event.rect.width) + '\u00D7' + Math.round(event.rect.height);
	});

// Tap, doubletap and hold (?)
interact('.tap-target-i')
	.on('tap', function (event) {
		console.log('tapped')
		event.currentTarget.classList.toggle('switch-bg');
		event.preventDefault();
	})
	.on('doubletap', function (event) {
		event.currentTarget.classList.toggle('large');
		event.currentTarget.classList.remove('rotate');
		event.preventDefault();
	})
	.on('hold', function (event) {
		event.currentTarget.classList.toggle('rotate');
		event.currentTarget.classList.remove('large');
	});