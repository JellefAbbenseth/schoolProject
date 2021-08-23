function openExSheet(inspectId){
    id = inspectId.slice(8);
    link = "/inspect_exercise_sheet/"+id;
    window.location.href = link;
}

function chooseEx(themesId){
    id = themesId.slice(7);
    link = "/chooseExercises/"+id;
    window.location.href = link;
}