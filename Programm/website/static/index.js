function openExSheet(inspectId){
    id = inspectId.slice(8);
    link = "/inspect_exercise_sheet/"+id;
    window.location.href = link;
}