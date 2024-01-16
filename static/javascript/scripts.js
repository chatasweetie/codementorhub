"use strict";


//////////////////////////////////////////
// Generates Problem (easy, medium or hard)
//////////////////////////////////////////

$(document).ready(function() {
  // Function to handle button click and make AJAX request
  function getProblemText(difficulty) {
    // Show the spinner when the AJAX request starts
    $('#ajaxSpinner').removeClass('d-none');
    document.getElementById("problem").innerHTML = "";
    $.ajax({
      type: "POST",
      url: "/get_problem",  
      data: { difficulty: difficulty },
      success: function(response) {
        // Hide spinner and update textarea with the received problem text
        $('#ajaxSpinner').addClass('d-none');
        $("#problem").val(response.code_problem);

        // Add a timestamp to the audio file URL to prevent caching
        const timestamp = new Date().getTime();
        const audioFileUrl = response.audio_file + '?' + timestamp;

        $('#audioSource').attr('src', audioFileUrl);
        // Load the new audio source
        $('#audioPlayer')[0].load();
        $('#audioPlayer')[0].play();
      },
      error: function(error) {
        console.error("Error fetching problem text:", error);
      }
    });
  }

  $("#easyBtn").click(function() {
    getProblemText("easy");
  });

  $("#mediumBtn").click(function() {
    getProblemText("medium");
  });

  $("#hardBtn").click(function() {
    getProblemText("hard");
  });
});



//////////////////////////////////////////
// Provides Feedback
//////////////////////////////////////////

// Function to handle the Get Hint button click
$('#getHint').click(function() {
  feedbackRequest('/get_hint', $('#problem').val(), $('#userSolution').val());
});

// Function to handle the Get Feedback button click
$('#getFeedback').click(function() {
  feedbackRequest('/get_feedback', $('#problem').val(), $('#userSolution').val());
});

// AJAX request function
function feedbackRequest(endpoint, problemText, userSolutionText) {
  $('#feedbackSpinner').removeClass('d-none');
  document.getElementById("feedback").innerHTML = "";
  $.ajax({
    url: endpoint,
    type: 'POST',
    data: {
      problem: problemText,
      userSolution: userSolutionText
    },
    success: function(response) {
      $('#feedbackSpinner').addClass('d-none');
      // Update the feedback section with the received text
      $('#feedback').text(response.feedback);

      // Add a timestamp to the audio file URL to prevent caching
      const timestamp = new Date().getTime();
      const audioFileUrl = response.audio_file + '?' + timestamp;

      $('#feedback-audioSource').attr('src', audioFileUrl);
      // Load the new audio source
      $('#feedback-audioPlayer')[0].load();
      $('#feedback-audioPlayer')[0].play();
    },
    error: function(error) {
      console.error('Error:', error);
    }
  });
}


//////////////////////////////////////////
// Big O
//////////////////////////////////////////

// Function to handle the Submit Big O button click
$('#submitBigO').click(function() {
  console.log("Submit Big O button clicked");
  // Get the selected radio button value
  var selectedBigO = $('input[name="bigO"]:checked').val();
  var user_solution = $('#userSolution').val();
  $('#feedbackSpinner').removeClass('d-none');
  document.getElementById("feedback").innerHTML = "";

  // Make an AJAX request to the Flask app
  $.ajax({
    url: '/submit_big_o',
    type: 'POST',
    data: {
      bigOValue: selectedBigO,
      user_solution: user_solution
    },
    success: function(response) {
      $('#feedbackSpinner').addClass('d-none');
      // Update the feedback section with the received text
      $('#feedback').text(response.feedback);

      // Add a timestamp to the audio file URL to prevent caching
      const timestamp = new Date().getTime();
      const audioFileUrl = response.audio_file + '?' + timestamp;

      $('#feedback-audioSource').attr('src', audioFileUrl);
      // Load the new audio source
      $('#feedback-audioPlayer')[0].load();
      $('#feedback-audioPlayer')[0].play();
    },
    error: function(error) {
      console.error('Error:', error);
    }
  });
});