var c = document.getElementById('Questions').rows.length;
for (var z = 0; z < c; z++) {
    var options = document.getElementById('s' + (z) + '_' + (z)).options;
    for (var i = 0; i < options.length; i++) {
        if (options[i].value == z) {
            options[i].selected = true;
            break;
        }
    }
}
CheckAnswers()
HideFeedback()