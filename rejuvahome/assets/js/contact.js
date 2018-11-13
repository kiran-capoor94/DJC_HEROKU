$(document).ready(function () {
    // Contact Form Handler
  
    var contactForm = $(".contact-form")
    var contactFormMethod = contactForm.attr("method")
    var contactFormEndpoint = contactForm.attr("action") // /abc/
  
  
    function displaySubmitting(submitBtn, defaultText, doSubmit) {
      if (doSubmit) {
        submitBtn.addClass("disabled")
        submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
      } else {
        submitBtn.removeClass("disabled")
        submitBtn.html(defaultText)
      }
    }
  
  
    contactForm.submit(function (event) {
      event.preventDefault()
  
      var contactFormSubmitBtn = contactForm.find("[type='submit']")
      var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
  
  
      var contactFormData = contactForm.serialize()
      var thisForm = $(this)
      displaySubmitting(contactFormSubmitBtn, "", true)
      $.ajax({
        method: contactFormMethod,
        url: contactFormEndpoint,
        data: contactFormData,
        success: function (data) {
          contactForm[0].reset()
          $.alert({
            title: "Success!",
            content: data.message,
            theme: "modern",
          })
          setTimeout(function () {
            displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
          }, 500)
        },
        error: function (error) {
          console.log(error.responseJSON)
          var jsonData = error.responseJSON
          var msg = ""
  
          $.each(jsonData, function (key, value) { // key, value  array index / object
            msg += key + ": " + value[0].message + "<br/>"
          })
  
          $.alert({
            title: "Oops!",
            content: msg,
            theme: "modern",
          })
  
          setTimeout(function () {
            displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
          }, 500)
  
        }
      })
    })
})