# GitHub Pull Request Template

## Developer Checklist
- [ ] **Clear Description**: What is the change and why it was implemented.
- [ ] **Branch Linked to Jira**: The branch is linked to the corresponding Jira ticket.
- [ ] **Clean Code**: Remove any console.log statements, debugging comments, and temporary code.
- [ ] **Code Standards**: Follow project-specific coding conventions, including naming conventions, indentation, and file structure.

---

## Reviewer Checklist

### Design
- [ ] is this the right approach?
- [ ] does the code make sense?
- [ ] does the code belong where it is?
- [ ] does it integrate well with the rest of the code?

### Functionality
- [ ] does the code do what it's supposed to do?
- [ ] does the code cover edge cases? (ones that you can think of)
- [ ] how does the code handle errors? are they treated with the correct response code/message?
- [ ] get the code and see it in action or ask for a demo
- [ ] check for obvious performance bottlenecks

### Complexity
- [ ] how fast can I read and understand what the code does?
- [ ] can I still understand it in 3 months?
- [ ] how easy can I modify or add something?
- [ ] over simplified vs. unnecessary complex
- [ ] too abstract vs. hardcoded use cases
- [ ] many small functions vs. one big function

### Tests
- [ ] unit / integration / end-to-end
- [ ] correct and **useful**
- [ ] tests also need code review

### Naming
- [ ] long enough to explain what it is or does
- [ ] short enough so it's easy to read

### Comments
- [ ] code should be self documenting
- [ ] should explain WHY code is there
- [ ] on rare / complex occasions, it explains WHAT
- [ ] too many vs. too few comments
- [ ] TODO - decide if now or later

### Security
- [ ] are all inputs properly validated? (e.g., use of schema validators)
- [ ] is all output properly escaped/sanitized?
- [ ] are authorization checks in place for protected actions?
- [ ] are secrets or credentials hardcoded? (they should not be)
- [ ] is error handling user-friendly without exposing internal details?
- [ ] are CSRF and XSS protections applied where needed?
- [ ] are new dependencies reviewed for trustworthiness and security?
- [ ] are security-related headers or middleware  present where applicable?
