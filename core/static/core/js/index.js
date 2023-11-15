document.getElementById("converter_form").addEventListener("submit", (e) => {
  e.preventDefault();

  $.ajax({
    url: converterApiUrl,
    method: "post",
    headers: { "X-CSRFToken": csrftoken },
    data: {
      value: document.getElementById("id_value").value,
      from_coin: document.getElementById("id_from").value,
      to_coin: document.getElementById("id_to").value,
    },
    success: function (response) {
      document.getElementById("id_result").value = response["result"];
    },
    error: function (error) {
      console.log(error);
    },
  });
});
