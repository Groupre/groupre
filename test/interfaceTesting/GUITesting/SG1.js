$(function drag() {
  var isMouseDown = false,
    isHighlighted;
  $("#groupreTable td")
    .mousedown(function () {
      isMouseDown = true;
      $(this).toggleClass("highlighted");
      isHighlighted = $(this).hasClass("highlighted");
      return false;
    })
    .mouseover(function () {
      if (isMouseDown) {
        $(this).toggleClass("highlighted", isHighlighted);
      }
    });

  $(document)
    .mouseup(function () {
      isMouseDown = false;
    });
});