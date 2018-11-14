/** This file is used as server side logic for a basic custom-built Google
 ** form that will upload files into a specific folder. It will also record
 ** any form data into a given Google Sheet.
 */

function doGet(e) {
  var template = HtmlService.createHtmlOutputFromFile('form.html');
  return template.setSandboxMode(HtmlService.SandboxMode.IFRAME);
}


function uploadFiles(form) {

  try {
    // get the folder we want by name. If it doesn't exist, then create it
    var dropbox = "FOLDER_NAME";
    var folder, folders = DriveApp.getFoldersByName(dropbox);

    if (folders.hasNext()) {
      folder = folders.next();
    } else {
      folder = DriveApp.createFolder(dropbox);
    }

    // retrieve the attached file from the form, change its name and set description
    var blob = form.myFile;
    var file = folder.createFile(blob);
    file.setName(form.myName.replace(/\s/g, "") + form.itemDescription);
    file.setDescription("Uploaded/ Requested by " + form.myName + " on " + new Date());

    // get all required form values into an array
    var vals = [];
    vals.push("");
    vals.push(form.eventDate);
    vals.push(new Date());
    vals.push(file.getUrl());
    vals.push("E - Receipt");
    vals.push("");
    vals.push(form.myName);
    vals.push(form.itemDescription);
    vals.push(form.myAmount);
    vals.push(form.myProgram);
    vals.push(form.bankDetails);

    // open google sheet by id and append values to it
    SpreadsheetApp.openById("GOOGLE_SHEET_ID_HERE").appendRow(vals);

    return "File uploaded successfully. " + file.getUrl();

  } catch (error) {

    return error.toString();

  }

}
