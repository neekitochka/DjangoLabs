$(document).ready(function () {
  $(".one-post").hover(
    function (event) {
      $(event.currentTarget)
        .find(".one-post-highlight")
        .animate({ opacity: "0.1" }, 300);
    },
    function (event) {
      $(event.currentTarget)
        .find(".one-post-highlight")
        .animate({ opacity: "0" }, 300);
    },

    $("img").hover(
      function (event) {
        $(event.currentTarget).animate({ width: 338, height: 328 }, 300);
      },
      function (event) {
        $(event.currentTarget).animate({ width: 318, height: 308 }, 300);
      }
    )
  );
});