
// Output functions are configurable.  This one just appends some text
// to a pre element.

function sendEmail() {
  window.location = "mailto:pythonsandladders@gmail.com?subject=[FEEDBACK]&Body=Square number: %0d%0dIssue or Suggestion: %0d%0dExpected behaviour: ";
}

function reportBug() {
  window.location = "mailto:pythonsandladders@gmail.com?subject=[REPORT BUG]&Body=Date encountered: %0d%0dBug description: %0d%0dExpected behaviour: ";
}

function featureRequest() {
  window.location = "mailto:pythonsandladders@gmail.com?subject=[FEATURE REQUEST]&Body=Feature description: %0d%0dCurrent behaviour: %0d%0dAffected pages: ";
}

function requestGuidance() {
  window.location = "mailto:pythonsandladders@gmail.com?subject=[GUIDANCE REQUEST]&Body=Square number: %0d%0dProblem(s) encountered: %0d%0dYour current solution attempt: ";
}


// ----------
// Run Skulpt
// ----------
function outf(text) { 
    var mypre = document.getElementById("output"); 
    mypre.innerHTML = mypre.innerHTML + text; 
} 
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}
// Here's everything you need to run a Python program in Skulpt
// 1. Grab the code from your textarea
// 2. Get a reference to your pre element for output
// 3. Configure the output function
// 4. Call Sk.importMainWithBody()
function runit() { 
   var prog = document.getElementById("yourcode").value; 
   var mypre = document.getElementById("output"); 
   mypre.innerHTML = ''; 
   Sk.pre = "output";
   Sk.configure({output:outf, read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       console.log('success');
   },
       function(err) {
       console.log(err.toString());
   });
}

// ---------------------------------
// Submit/test feature for user code
// ---------------------------------
// function range(start, count) {
//   return Array.apply(0, Array(count))
//     .map(function (element, index) { 
//       return index + start;  
//   });
// }

// function outf1(text) { 
//     var mypre = document.getElementById("output"); 

//     if (text == '4') {
//       mypre.innerHTML = mypre.innerHTML + "Expected output:\t4\n" + "Your output:\t\t" + text + "  &#10003;\n";
//     }
// } 

// function submitForTests(testNum) {

//   var prog = document.getElementById("yourcode").value; 
//   var testcase = document.getElementById("myInput" + testNum).value;

//   var mypre = document.getElementById("output");
//   var appendedTest = prog + testcase;
//   mypre.innerHTML = appendedTest;

//    mypre.innerHTML = 'TEST RESULTS:\n\n' + testcase + '\n'; 
//    Sk.pre = "output";
//    Sk.configure({output:outf1, read:builtinRead}); 
//    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
//    var myPromise = Sk.misceval.asyncToPromise(function() {
//        return Sk.importMainWithBody("<stdin>", false, appendedTest, true);
//    });
//    myPromise.then(function(mod) {
//        console.log('success');
//    },
//        function(err) {
//        console.log(err.toString());
//    });
// }

// --------------------------------
// Clear feature for the output div
// --------------------------------
function clearBox() {
    document.getElementById('output').innerHTML = "";
}

// --------------------------------
// Save as feature for the textarea
// --------------------------------
function saveTextAsFile() {
    
    var textToWrite = document.getElementById('yourcode').value;
    var textFileAsBlob = new Blob([textToWrite], {
        type: 'text/plain'
    });
    var fileNameToSaveAs = "progress_pythonsandladders.txt";

    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    if (window.webkitURL != null) {
        // Chrome allows the link to be clicked
        // without actually adding it to the DOM.
        downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
    } else {
        // Firefox requires the link to be added to the DOM
        // before it can be clicked.
        downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);
    }

    downloadLink.click();
}
var button = document.getElementById('save');
button.addEventListener('click', saveTextAsFile);

function destroyClickedElement(event) {
    // remove the link from the DOM
    document.body.removeChild(event.target);
}
// --------------------------------