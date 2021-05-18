$("button").click(function() {
  var value = $(this).parent().parent().find("input").val();
  $("#output").html(value + "<br>&lt;time datetime='" + value + "'>&lt;/time>");
  console.log(value);
});