// script.js
document.getElementById('submitBtn').addEventListener('click', function() {
    var answers = [];
    for (var i = 1; i <= 6; i++) {
        var question = document.getElementsByName('q' + i);
        for (var j = 0; j < question.length; j++) {
            if (question[j].checked) {
                answers.push('Question ' + i + ': ' + question[j].value);
                break;
            }
        }
    }
    // Save to file (this part depends on your environment; it's different for server-side JS and client-side JS)
    console.log(answers); // For demonstration purposes
});
document.getElementById('quizForm').addEventListener('click', function(event) {
    event.stopPropagation(); // Prevents the click event from reaching the parent collapsible div
});