
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

function requestSolution() {
  window.location = "mailto:pythonsandladders@gmail.com?subject=[SOLUTION REQUEST]&Body=Square number: %0d%0dProblem(s) encountered: %0d%0dYour current solution attempt: ";
}

function outf(text) { 
    var mypre = document.getElementById("output"); 
    mypre.innerHTML = mypre.innerHTML + text; 
} 
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}
// Here's everything you need to run a python program in skulpt
// grab the code from your textarea
// get a reference to your pre element for output
// configure the output function
// call Sk.importMainWithBody()
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