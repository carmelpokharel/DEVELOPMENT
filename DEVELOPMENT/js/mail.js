// ------------
// Mail buttons
// ------------
function sendEmail() {
  window.location = "mailto:info@pythonsandladders.com?subject=[FEEDBACK]&Body=Square number: %0d%0dIssue or Suggestion: %0d%0dExpected behaviour: ";
}
function reportBug() {
  window.location = "mailto:info@pythonsandladders.com?subject=[REPORT BUG]&Body=Date encountered: %0d%0dBug description: %0d%0dExpected behaviour: ";
}