# GitHub Project setup

Create a **User-owned or repository-owned Project** named `System Design Interview Learning`.

## Views

### Board

Group by Status:

`Backlog`, `Reading`, `Code Investigation`, `Lab in Progress`, `Review`, `Done`

### Table

Add these fields:

| Field | Type | Values |
|---|---|---|
| Status | Single select | Backlog, Reading, Code Investigation, Lab in Progress, Review, Done |
| Session | Number | 1-11 |
| Track | Single select | Foundations, Data, Delivery, Communication, Security, Capstone |
| Priority | Single select | Must, Should, Nice |
| Platform | Single select | GitHub, Azure, Local |
| Evidence | Text | Link to evidence, commit, or PR |

## Automation

Enable built-in workflows:

- New issues -> `Backlog`
- Issue assigned -> `Code Investigation`
- Pull request opened -> `Review`
- Pull request merged -> `Done`
- Issue closed -> `Done`

Use the issue templates in `.github/ISSUE_TEMPLATE/` so assignments carry consistent acceptance criteria.
